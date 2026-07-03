# Day02 学习记录

## 概述

今天主要练习了音频与文本的常见预处理和统计脚本：读取 WAV 文件信息、绘制波形、文本到 CSV/JSON 的转换以及文本统计。

## 脚本清单与功能

- `describe_audio.py`
  - 使用 `soundfile.read()` 读取 `data/audio/day01` 下的所有 WAV 文件。
  - 输出：采样率（sample rate）、总采样点数（frames）、时长（秒）、声道数（channels）、数据类型（dtype）。
  - 汇总并打印最短、最长、平均时长。

- `plot_waveform.py`
  - 使用 `librosa.load(path, sr=None)` 保持原始采样率加载音频，绘制前 1 秒的波形图（使用 `matplotlib`）。

- `text_to_csv_json.py`
  - 将 `Day01/sample_text.txt`（每行：`utt_id text`）读取为两列：`utt_id` 和 `text`。
  - 使用 `pandas.DataFrame` 保存为 `sample_text.csv`（UTF-8，无行号）和 `sample_text.json`（`orient='records'`）。
  - 演示如何从 CSV 反向读取为字典列表。

- `data_statistics.py`
  - 读取 `Day02/sample_text.csv`，计算每条文本的字符数并添加 `char_count` 列。
  - 输出总样本数、字符数平均值/最小/最大值。
  - 将字符数大于 10 的样本另存为 `long_sentences.csv`。

## 运行示例

在工作区根目录下运行：

```bash
python Day02/describe_audio.py
python Day02/plot_waveform.py
python Day02/text_to_csv_json.py
python Day02/data_statistics.py
```

## 依赖

- 必需：`python3`。
- 推荐安装（脚本中有的功能需要）：
  - `librosa`（用于加载音频并绘图）
  - `matplotlib`（绘图）
  - `pandas`（CSV/JSON 读写与表格操作）
  - `soundfile`（高效读取 WAV 信息；若未安装，脚本可能需要回退实现或报错）

安装示例：

```bash
pip install librosa matplotlib pandas soundfile
```

## 注意

- 路径默认假设仓库结构保持为：`data/audio/day01`、`Day01/sample_text.txt` 等。如有改动请在脚本中调整路径。
- `librosa.load(..., sr=None)` 用于避免默认重采样到 22050 Hz，保留原采样率。

---

如果你希望，我可以：
- 为每个脚本添加命令行参数（如：指定文件/目录），
- 或把依赖写入 `requirements.txt` 并创建一个简单的安装说明。
