import os
import glob

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "..", "data")
os.chdir(data_dir)

# 查找 data/audio/day01 目录下所有 .wav 文件
wav_files = glob.glob("audio/day01/*.wav")

for wav_path in wav_files:
    base_name = os.path.basename(wav_path)
    name_without_ext = os.path.splitext(base_name)[0]
    print(f"path: {wav_path}")
    print(f"name: {name_without_ext}")
