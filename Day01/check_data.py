import os
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
text_path = os.path.join(base_dir, "sample_text.txt")
data_dir = os.path.join(base_dir, "..", "data")

# 读取 sample_text.txt，构造 {音频ID: 文字} 字典
text_data = {}
with open(text_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) >= 2:
            audio_id, text = parts[0], parts[1]
            text_data[audio_id] = text

# 获取 audio/day01/ 下所有 wav 文件名（去掉 .wav 后作为 ID）
os.chdir(data_dir)
wav_files = glob.glob("audio/day01/*.wav")
audio_ids = {os.path.splitext(os.path.basename(wav_file))[0] for wav_file in wav_files}

# 对比两个集合
text_ids = set(text_data.keys())
missing_audio = text_ids - audio_ids
missing_text = audio_ids - text_ids

# 打印统计结果
print("Text entries:", len(text_data))
print("Audio files:", len(audio_ids))
print("Missing audio:", sorted(missing_audio))
print("Missing text:", sorted(missing_text))

# 把结果写入 report.txt
report_path = os.path.join(base_dir, "report.txt")
with open(report_path, "w", encoding="utf-8") as report_file:
    report_file.write(f"Text entries: {len(text_data)}\n")
    report_file.write(f"Audio files: {len(audio_ids)}\n")
    report_file.write(f"Missing audio: {sorted(missing_audio)}\n")
    report_file.write(f"Missing text: {sorted(missing_text)}\n")

print(f"Report written to: {report_path}")
