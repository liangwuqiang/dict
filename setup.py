#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    cobra
    ~~~~~

    Implements cobra main

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
import codecs
import dict
# import setuptools.command.test
import setuptools

# -*- Long Description -*-  长描述


def long_description():
    try:
        return codecs.open('README.md', 'r', 'utf-8').read()
        # 自然语言编码转换模块
    except IOError:
        return 'Long description error: Missing README.rst file'  # 长描述错误:丢失文件


setuptools.setup(
    name=dict.__name__,  # 名称
    version=dict.__version__,  # 版本号
    description=dict.__description__,  # 描述
    long_description=long_description(),  # 长描述,也就是前面定义的那个函数
    keywords=dict.__keywords__,  # 关键字定义
    author=dict.__author__,  # 作者
    author_email=dict.__contact__,  # 作者的电子邮箱
    url=dict.__url__,  # 网址
    license=dict.__license__,  # 许可证
    platforms=['any'],  # 平台
    classifiers=[  # 分类器
        # How mature is this project? Common values are  该项目的完成情况? 普通的值是
        #   3 - Alpha
        #   4 - Beta  测试
        #   5 - Production/Stable  产品/稳定
        'Development Status :: 5 - Production/Stable',  # 开发状态

        # Indicate who your project is intended for  你的项目所面向的人群
        'Intended Audience :: Developers',  # 面向的群众,开发者
        'Natural Language :: Chinese (Simplified)',  # 自然语言,中文
        'Natural Language :: English',  # 自然语言,英文
        'Topic :: Utilities',  # 主题, 实用程序
        'Topic :: Terminals',  # 主题, 终端
        "Topic :: System :: Distributed Computing",  # 主题, 系统, 分发

        # Pick your license as you wish (should match "license" above) 选择你希望的许可证,应该和上面的许可证相匹配
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # 在这里标识出你所支持的python版本,特别是,要确定
        # that you indicate whether you support Python 2, Python 3 or both.
        # 你要标识出是否支持python2,python3或者两者都支持.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=setuptools.find_packages(exclude=['tests']),  # 软件包,排除掉test部分
    include_package_data=True,  # 包含包数据
    package_data={   # 包数据
        '': ['*.py']
    },
    entry_points={  # 程序入口
        'console_scripts': [
            'dict = dict:main',
        ],
    },
)
