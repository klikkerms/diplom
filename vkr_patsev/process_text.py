# coding=utf-8
# Copyright 2016 Ottokar Tilk and Tanel Alumäe
# The following code is available on:
# https://github.com/ottokart/punctuator2/blob/master/example/dont_run_me_run_the_other_script_instead.py
# In it, functions are defined to exchange all punctuation marks in a dataset for
# descriptors of said punctuations.

from __future__ import division, print_function
from nltk.tokenize import word_tokenize

import nltk
import os
from io import open
import re
import sys

nltk.download("punkt")

NUM = "<NUM>"

EOS_PUNCTS = {".": ".PERIOD", "?": "?QUESTIONMARK", "!": "!EXCLAMATIONMARK"}
INS_PUNCTS = {",": ",COMMA", ";": ";SEMICOLON", ":": ":COLON", "-": "-DASH"}

forbidden_symbols = re.compile(r"[\[\]\(\)\/\\\>\<\=\+\_\*]")
numbers = re.compile(r"\d")
multiple_punct = re.compile(r"([\.\?\!\,\:\;\-])(?:[\.\?\!\,\:\;\-]){1,}")

is_number = lambda x: len(numbers.sub("", x)) / len(x) < 0.6

def process_line(line):

    tokens = word_tokenize(line)
    output_tokens = []

    for token in tokens:

        if token in INS_PUNCTS:
            output_tokens.append(INS_PUNCTS[token])
        elif token in EOS_PUNCTS:
            output_tokens.append(EOS_PUNCTS[token])
        elif is_number(token):
            output_tokens.append(NUM)
        else:
            output_tokens.append(token.lower())

    return " ".join(output_tokens) + " "


# import re
#
# def process_line(line):
#     line = line.lower() # Приводим строку к нижнему регистру
#     line = re.sub(r'[^\w\s]','',line) # Удаляем все знаки препинания
#     line = re.sub(r'\d+', '', line) # Удаляем все числа
#     return line


# import re
#
#
# EOS_PUNCTS = {".": ".PERIOD", "?": "?QUESTIONMARK", "!": "!EXCLAMATIONMARK"}
# INS_PUNCTS = {",": ",COMMA", ";": ";SEMICOLON", ":": ":COLON", "-": "-DASH"}
#
#
# def process_line(line):
#     line = line.strip()
#
#     # Заменяем конечные знаки препинания
#     for k, v in EOS_PUNCTS.items():
#         if len(k) > 1:
#             line = line.replace(k, v)
#         else:
#             line = line.replace(k, ' ' + v)
#
#     # Заменяем вставочные знаки препинания
#     for k, v in INS_PUNCTS.items():
#         if len(k) > 1:
#             line = line.replace(k, v + ' ')
#         else:
#             line = line.replace(k, ' ' + v + ' ')
#
#     # Заменяем двойные пробелы на одинарные
#     line = re.sub(r'\s+', ' ', line)
#
#     return line
