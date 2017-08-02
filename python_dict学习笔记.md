# dict的学习笔记

1. 通过api接口来访问 有道词典的数据
    api = 'http://fanyi.youdao.com/openapi.do?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='

2. 通过命令行参数 获取查询关键字,字符串
需要对字符串进行拼接,utf-8编码encode,urllib.quote转换成合法的网址格式,再与api进行拼接

3. 通过urlopen(api).read()来获取网络返回的内容,utf-8解码decode,进行json.loads()处理.

4. 按照关键字进行提取相应的值

5. 各种异常情况的处理

6. 正则表达式[\u4e00-\u9fa5] 可以匹配汉字
