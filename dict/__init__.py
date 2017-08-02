#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    dict字典
    ~~~~

    Chinese/English Translation 中英翻译

    :date:      09/12/2013  日期
    :author:    Feei <feei@feei.cn> 作者
    :homepage:  https://github.com/wufeifei/dict  主页
    :license:   MIT, see LICENSE for more details. 许可
    :copyright: Copyright (c) 2017 Feei. All rights reserved 版权
"""
from __future__ import unicode_literals
import sys  # 调用系统命令
import json  # 用于网络文本的格式转换
import re  # 提供对正则表达式的支持

__name__ = 'dict-cli'  # 软件名称
__version__ = '1.3.4'  # 版本号
__description__ = '命令行下中英文翻译工具（Chinese and English translation tools in the command line）'  # 描述
__keywords__ = 'Translation English2Chinese Chese2English Command-line'  # 关键字
__author__ = 'Feei'  # 作者
__contact__ = 'feei@feei.cn'  # 联系
__url__ = 'https://github.com/wufeifei/dict'  # 网址
__license__ = 'MIT'  # 许可证

try:  # 进行兼容性的导入
    # For Python 3.0 and later  python3.0或更新的版本
    from urllib.request import urlopen  # 打开字符串网址,来请求网络响应
    from urllib.parse import quote  # 将所引用的文本解析为合法的网址格式
except ImportError:
    # Fall back to Python 2's urllib2  回到python2中,使用urllib2
    from urllib2 import urlopen
    from urllib import quote


class Dict:  # 字典类
    key = '716426270'  # 密码
    keyFrom = 'wufeifei'  # 用户名
    api = 'http://fanyi.youdao.com/openapi.do'  \
          '?keyfrom=wufeifei&key=716426270&type=data&doctype=json&version=1.1&q='  # api接口(现在不完整)
    content = None  # 变量定义.其实是先起个名字,留着备用

    def __init__(self, argv):  # 构造函数,这里传入一个参数
        message = ''  # 指定一个空的字符串,用来进行字符串的拼接
        if len(argv) > 0:  # 判断是否存在命令行参数
            for s in argv:  # 对命令行参数进行迭代
                message = message + s + ' '  # 通过命令行参数来构造一个字符串信息,这里的字符串带空格
            self.api = self.api + quote(message.encode('utf-8'))  # 对字符串规范化之后,拼接到api中
            self.translate()  # 调用类中另外一个方法,专门用于处理翻译功能
        else:
            print('Usage: dict test')  # 如果没有提供命令行参数,就提示使用方法

    def translate(self):  # 专门处理翻译的方法
        try:  # 试图从网络中导入数据
            content = urlopen(self.api).read()   # 这是个局部变量
            # 由于导入中使用了from,这里可以直接使用方法,方法返回的是实例,read之后返回的是字符串,即api网页的内容
            self.content = json.loads(content.decode('utf-8'))  # 使用json的loads方法重新格式化下载的文本,之前先对文件进行编码.
            self.parse()  # 类中专门用来解析的方法
        except Exception as e:  # 异常处理,这个处理只跟网络有关,只处理第一句就可以了吧?
            print('ERROR: Network or remote service error!')  # 网络或远程服务错误
            print(e)  # 输出错误信息

    def parse(self):  # 专门处理文本解析的方法
        code = self.content['errorCode']  # 从文本中提取错误代码的值
        if code == 0:  # 错误代码值为0,代表成功,正常
            c = None  # 对c赋初值,c用于存放中文发音
            try:  # 对发音部分进行处理
                u = self.content['basic']['us-phonetic']  # 美国发音
                e = self.content['basic']['uk-phonetic']  # 英国发音
            except KeyError:  # 找不到英文发音的关键字
                try:
                    c = self.content['basic']['phonetic']  # 中文发音
                except KeyError:  # 找不到中文发音的关键字
                    c = 'None'
                u = 'None'
                e = 'None'

            try:  # 对解释部分进行处理
                explains = self.content['basic']['explains']
            except KeyError:  # 找不到解释的关键字
                explains = 'None'

            try:  # 对网络解释部分进行处理
                phrase = self.content['web']  # 这里对应的是个list
            except KeyError:  # 没有遭到web关键字
                phrase = 'None'  # 这里对应的是str

            print('\033[1;31m################################### \033[0m')  # 特殊部分是控制前景色和背景色的
            # \033[1;31m表示颜色控制开始,前景色31,背景色1;  \033[0m表示颜色控制结束
            print('\033[1;31m# \033[0m {0} {1}'.format(  # 进行格式化输出,0和1分别代表两个位置,用format的两个参数替代
                self.content['query'], self.content['translation'][0]))  # 通过关键字来提取相应的值
            if u != 'None':  # 有英语发音的情况
                print('\033[1;31m# \033[0m (U: {0} E: {1})'.format(u, e))
            elif c != 'None':  # 有中文发音的情况
                print('\033[1;31m# \033[0m (Pinyin: {0})'.format(c))
            else:  # 没有发音的情况下  输出空
                print('\033[1;31m# \033[0m')

            print('\033[1;31m# \033[0m')  # 为什么还有空出一行呢,分割?

            if explains != 'None':  # 处理解释部分的内容
                for i in range(0, len(explains)):  # 在多条解释中进行迭代
                    print('\033[1;31m# \033[0m {0}'.format(explains[i]))  # 格式化输出一条解释
            else:
                print('\033[1;31m# \033[0m Explains None')  # 解释部分为空的情况

            print('\033[1;31m# \033[0m')  # 空出一行

            if phrase != 'None':  # 这是网络解释的那部分内容
                for p in phrase:  # phrase返回的是list ,p就是其下面的一项,这项是个dict
                    print('\033[1;31m# \033[0m {0} : {1}'.format(  # 格式化输出键值对
                        p['key'], p['value'][0]))  # 这里取了键和第一个解释

                    # 对于多于一个解释的情况,进行分行显示
                    if len(p['value']) > 0:  # 我觉得这里不应该是0,而是1
                        if re.match('[ \u4e00 -\u9fa5]+', p['key']) is None:  # 关键字中包含特殊字符
                            """
                        # match ：只从字符串的开始与正则表达式匹配，匹配成功返回matchobject，否则返回none；
                        # search ：将字符串的所有字串尝试与正则表达式匹配，如果所有的字串都没有匹配成功，返回none，否则返回matchobject；
                        # [\u4e00-\u9fa5]正则表达式
                        1、至少匹配一个汉字的写法。 
                        2、这两个unicode值正好是Unicode表中的汉字的头和尾。 
                        3、"[]"代表里边的值出现一个就可以，后边的“+”代表至少出现1次，合起来即至少匹配一个汉字。
                        """
                            blank = len(p['key'].encode('gbk'))  # 关键字重新编码后取长度
                        else:
                            blank = len(p['key'])  # 根据关键字长度,留出空白,解释分行显示,解释进行列对齐
                        for i in p['value'][1:]:  # 第二个元素到最后,需要换行显示
                            print('\033[1;31m# \033[0m {0} {1}'.format(
                                ' ' * (blank + 3), i))  # 先输出多个空格后,再输出解释,对齐显示

            print('\033[1;31m################################### \033[0m')  # 翻译结束
            # Phrase  解析
            # for i in range(0, len(self.content['web'])):  在web部分内容中进行迭代
            #     print self.content['web'][i]['key'], ':'  打印其中一项的关键字
            #     for j in range(0, len(self.content['web'][i]['value'])):  关键字的值是个list,所以要进行迭代输出
            #         print self.content['web'][i]['value'][j]  迭代输出相应关键字的解释

        # 针对各种错误代码,输出相应的提示信息
        elif code == 20:  # Text to long  文本太长?
            print('WORD TO LONG')
        elif code == 30:  # Trans error  翻译错误
            print('TRANSLATE ERROR')
        elif code == 40:  # Don't support this language  不支持这种语言
            print('CAN\'T SUPPORT THIS LANGUAGE')
        elif code == 50:  # Key failed  关键字错误
            print('KEY FAILED')
        elif code == 60:  # Don't have this word  没有这个单词
            print('DO\'T HAVE THIS WORD')


def main():  # 主函数
    Dict(sys.argv[1:])  # 使用命令行参数对类进行实例化


if __name__ == '__main__':  # 使用本程序运行的话,直接调用main方法
    main()

    '''
程序中存在的问题:
43行:
    \ 后面不能有空格

120行:
    if re.match('[ \u4e00 -\u9fa5]+', p['key']) is None: 
    去掉里面的空格, [\u4e00-\u9fa5]
    
129行和131行对换:                        
    blank = len(p['key'].encode('gbk')) 
    blank = len(p['key']) 
    因为条件给的是匹配不成立的情况
    
134行:    
    ' ' * (blank + 3), i)) 
   115行隔了3格,133行隔了1空格,所以这里补偿的是2,这样才能显示对齐 
    '''
