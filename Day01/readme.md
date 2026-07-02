# Day01 学习记录

## 今日学习内容

### 1. 文件读取与写入
- 学习了使用 `open()` 读取文本文件
- 了解了 `with` 语句在文件操作中的使用方式
- 使用了 `for line in file` 逐行读取内容
- 学习了 `strip()` 去除换行和空白，`split()` 分割文本

### 2. 路径与文件遍历
- 学习了使用 `os.path` 处理文件路径
- 使用了 `glob.glob()` 查找指定类型文件
- 了解了如何通过路径获取文件名和扩展名

### 3. 数据集检查与集合对比
- 读取 `sample_text.txt` 中的 `utt_id` 和文本内容
- 从 `audio/` 目录中获取所有 `.wav` 文件名
- 使用集合运算比较文本标注和音频文件之间的差异
- 找出缺失音频和缺失标注
- 将检查结果写入 `report.txt`

### 4. 面向对象封装
- 将检查逻辑封装为 `DataChecker` 类
- 通过 `load_text()`、`load_audio_ids()`、`check()` 三个方法完成数据检查
- 使用 `main.py` 作为运行入口

## 今日完成的脚本
- `read_text.py`：逐行读取文本文件并打印行号和内容
- `list_wavs.py`：列出音频文件路径和文件名
- `check_data.py`：检查文本和音频 ID 是否匹配
- `data_checker.py`：封装成可复用的 `DataChecker` 类
- `main.py`：调用 `DataChecker` 执行检查

## 备注
- 本次学习主要聚焦于 Python 基础文件操作、路径处理和简单数据集校验流程。
- 这也是 ASR 入门学习的第一天，重点是掌握基本的数据准备和检查思路。
