import glob
import os
import soundfile as sf


def describe_wav(path):
    data, samplerate = sf.read(path)
    frames = len(data)
    duration = frames / samplerate
    channels = data.shape[1] if data.ndim > 1 else 1
    dtype = data.dtype
    return {
        "path": path,
        "sample_rate": samplerate,
        "frames": frames,
        "duration": duration,
        "channels": channels,
        "dtype": dtype,
    }


def main():
    base_dir = os.path.join(os.path.dirname(__file__), os.pardir, "data", "audio", "day01")
    base_dir = os.path.abspath(base_dir)

    wav_paths = sorted(glob.glob(os.path.join(base_dir, "*.wav")))
    if not wav_paths:
        print(f"没有找到 WAV 文件：{base_dir}")
        return

    descriptions = [describe_wav(path) for path in wav_paths]

    for desc in descriptions:
        print(f"文件: {os.path.basename(desc['path'])}")
        print(f"  采样率: {desc['sample_rate']}")
        print(f"  总采样点数: {desc['frames']}")
        print(f"  时长（秒）: {desc['duration']:.6f}")
        print(f"  声道数: {desc['channels']}")
        print(f"  数据类型: {desc['dtype']}")
        print()

    durations = [desc["duration"] for desc in descriptions]
    print("统计:")
    print(f"  最短时长: {min(durations):.6f} 秒")
    print(f"  最长时长: {max(durations):.6f} 秒")
    print(f"  平均时长: {sum(durations) / len(durations):.6f} 秒")


if __name__ == "__main__":
    main()
