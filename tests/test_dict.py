#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    test_dict
    ~~~~~~~~~

    Test Dict

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/wufeifei/dict
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
from __future__ import unicode_literals
from dict import Dict


def test_e2c_words(capfd):  # 所继承的capfd不知道是哪里来的?
    Dict(['Test'])  # 通过关键字来调用程序
    out, err = capfd.readouterr()  # 捕获到的输出和错误,返回的应该是个列表或字典什么的
    assert '测试' in out  # 验证是否在输出中包含了所要测试的内容


def test_e2c_sentences(capfd):
    Dict(['I', 'Love', 'You'])
    out, err = capfd.readouterr()
    assert '我爱你' in out


def test_c2e_words(capfd):
    Dict(['测试'])
    out, err = capfd.readouterr()
    assert 'Test' in out


def test_c2e_sentences(capfd):
    Dict(['我爱你'])
    out, err = capfd.readouterr()
    assert 'I love you' in out
