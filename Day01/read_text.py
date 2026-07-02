# read_text.py
# 逐行读取 Day01/sample_text.txt 文件，并打印行号和内容

import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "sample_text.txt")

with open(file_path, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        # 去除行末换行符和多余空白
        stripped_line = line.strip()
        # 将行内容按空白分割为单词列表
        words = stripped_line.split()
        print(f"Line {line_number}: {stripped_line}")
        # 如果需要，还可以打印本行的单词数量或第一个单词
        if words:
            print(f"  Words: {len(words)}, First word: {words[0]}")
