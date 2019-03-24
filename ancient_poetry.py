#!/usr/bin/env python3
# --*-- coding:utf-8 --*--
# __Author__ Aaron

import requests
import re


def parse_page(url):
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    text = response.text
    titles = re.findall(r'<div\sclass="sons".*?<b>(.*?)</b>',
                        text, re.DOTALL)  # .不能匹配换行符,加re.DOALL 可以匹配所有字符 re.DOALL == re.S
    dynasties = re.findall(r'<p class="source".*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source".*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.S)
    contents = []
    for content in content_tags:
        x = re.sub("<.*?>","",content)
        # print(x.strip())
        contents.append(x.strip())
    poems = []
    for value in zip(titles,dynasties,authors,contents):
        title,dynastie,author,content = value
        poem = {
            'title':title,
            'dynastie':dynastie,
            'author':author,
            'content':content
        }
        poems.append(poem)

    for poem in poems:
        print(poem)
        print("#"*60)


def main():
    url = 'https://www.gushiwen.org/default_{}.aspx'
    for index in range(1,11):
        url = url.format(index)
        parse_page(url)


if __name__ == '__main__':
    main()
