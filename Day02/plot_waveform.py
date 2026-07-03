import glob
import os

import librosa
import matplotlib.pyplot as plt


def main():
    base_dir = os.path.join(os.path.dirname(__file__), os.pardir, "data", "audio", "day01")
    base_dir = os.path.abspath(base_dir)

    wav_paths = sorted(glob.glob(os.path.join(base_dir, "*.wav")))
    if not wav_paths:
        print(f"没有找到 WAV 文件：{base_dir}")
        return

    path = wav_paths[0]
    y, sr = librosa.load(path, sr=None)

    duration = len(y) / sr
    end_sample = min(len(y), sr)
    y_first_second = y[:end_sample]
    t = [i / sr for i in range(len(y_first_second))]

    plt.figure(figsize=(10, 4))
    plt.plot(t, y_first_second, linewidth=0.8)
    plt.title(f"Waveform: {os.path.basename(path)} (first 1 second)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.xlim(0, min(1.0, duration))
    plt.tight_layout()
    plt.show()

    print(f"Loaded: {path}")
    print(f"sample rate: {sr}")
    print(f"total duration: {duration:.3f} s")


if __name__ == "__main__":
    main()
