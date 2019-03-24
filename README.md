使用re爬取古诗文的信息
compile：
对于一些经常要用到的正则表达式，可以使用compile进行编译，后期再使用的时候可以直接拿过来用，执行效率会更快。而且compile还可以指定flag=re.VERBOSE，在写正则表达式的时候可以做好注释。示例代码如下：

text = "the number is 20.50"
r = re.compile(r"""
                \d+ # 小数点前面的数字
                \.? # 小数点
                \d* # 小数点后面的数字
                """,re.VERBOSE)
ret = re.search(r,text)
print(ret.group())
