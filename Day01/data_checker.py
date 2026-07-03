import os
import glob
import wave

try:
    import pandas as pd
except Exception:
    pd = None

try:
    import soundfile as sf
except Exception:
    sf = None


class DataChecker:
    def __init__(self, text_path, audio_dir, output_report="report.txt"):
        self.text_path = text_path
        self.audio_dir = audio_dir
        self.output_report = output_report

    def load_text(self):
        text_data = {}
        with open(self.text_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(maxsplit=1)
                if len(parts) >= 2:
                    utt_id, text = parts[0], parts[1]
                    text_data[utt_id] = text
        return text_data

    def load_audio_ids(self):
        wav_files = glob.glob(os.path.join(self.audio_dir, "day01", "*.wav"))
        audio_ids = [os.path.splitext(os.path.basename(wav_file))[0] for wav_file in wav_files]
        return audio_ids

    def check(self):
        text_data = self.load_text()
        audio_ids = self.load_audio_ids()

        text_ids = set(text_data.keys())
        audio_id_set = set(audio_ids)

        missing_audio = sorted(text_ids - audio_id_set)
        missing_text = sorted(audio_id_set - text_ids)

        print(f"Total text entries: {len(text_data)}")
        print(f"Total audio files: {len(audio_ids)}")
        print(f"Missing audio count: {len(missing_audio)}")
        print(f"Missing text count: {len(missing_text)}")
        print("Missing audio IDs:")
        for utt_id in missing_audio[:10]:
            print(f"  - {utt_id}")
        print("Missing text IDs:")
        for utt_id in missing_text[:10]:
            print(f"  - {utt_id}")

        output_path = os.path.join(os.path.dirname(self.text_path), self.output_report)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("Data Check Report\n")
            f.write("=================\n")
            f.write(f"Text file: {self.text_path}\n")
            f.write(f"Audio directory: {self.audio_dir}\n")
            f.write(f"Total text entries: {len(text_data)}\n")
            f.write(f"Total audio files: {len(audio_ids)}\n")
            f.write(f"Missing audio count: {len(missing_audio)}\n")
            f.write(f"Missing text count: {len(missing_text)}\n")
            f.write("\nMissing audio IDs:\n")
            if missing_audio:
                for utt_id in missing_audio:
                    f.write(f"- {utt_id}\n")
            else:
                f.write("None\n")
            f.write("\nMissing text IDs:\n")
            if missing_text:
                for utt_id in missing_text:
                    f.write(f"- {utt_id}\n")
            else:
                f.write("None\n")

        print(f"Report written to: {output_path}")

    def generate_stats(self, csv_path=None, summary_name="dataset_summary.txt"):
        """Generate dataset statistics:
        - count audio files and total duration (using soundfile)
        - compute average and max text character counts from CSV (or text file fallback)
        - report missing audio/text entries (reuse check logic)
        - write all info to `dataset_summary.txt` next to the text file
        """
        # locate CSV
        if csv_path is None:
            possible_csv = os.path.join(os.path.dirname(self.text_path), "sample_text.csv")
            if not os.path.exists(possible_csv):
                possible_csv = os.path.abspath(os.path.join(os.path.dirname(self.text_path), "..", "Day02", "sample_text.csv"))
        else:
            possible_csv = csv_path

        df = None
        if os.path.exists(possible_csv):
            if pd is not None:
                try:
                    df = pd.read_csv(possible_csv, encoding="utf-8")
                except Exception:
                    df = None
            else:
                df = None

        # audio files under audio_dir/day01
        wav_pattern = os.path.join(self.audio_dir, "day01", "*.wav")
        wav_files = sorted(glob.glob(wav_pattern))
        audio_count = len(wav_files)
        total_duration = 0.0
        for w in wav_files:
            # Prefer soundfile if available
            if sf is not None:
                try:
                    info = sf.info(w)
                    total_duration += info.frames / info.samplerate
                    continue
                except Exception:
                    pass
            # Fallback to wave (std lib)
            try:
                with wave.open(w, "rb") as wf:
                    frames = wf.getnframes()
                    sr = wf.getframerate()
                    if sr > 0:
                        total_duration += frames / sr
            except Exception:
                # unable to read duration for this file
                continue

        # text statistics
        if df is not None and "text" in df.columns:
            df["char_count"] = df["text"].astype(str).apply(len)
            avg_chars = df["char_count"].mean()
            max_chars = int(df["char_count"].max())
            text_ids = set(df["utt_id"].astype(str).tolist()) if "utt_id" in df.columns else set()
        else:
            text_data = self.load_text()
            lengths = [len(t) for t in text_data.values()]
            avg_chars = float(sum(lengths) / len(lengths)) if lengths else 0.0
            max_chars = int(max(lengths)) if lengths else 0
            text_ids = set(text_data.keys())

        audio_ids = set([os.path.splitext(os.path.basename(w))[0] for w in wav_files])
        missing_audio = sorted(text_ids - audio_ids)
        missing_text = sorted(audio_ids - text_ids)

        summary_path = os.path.join(os.path.dirname(self.text_path), summary_name)
        with open(summary_path, "w", encoding="utf-8") as outf:
            outf.write("Dataset Summary\n")
            outf.write("================\n")
            outf.write(f"Text file: {self.text_path}\n")
            outf.write(f"Audio dir: {self.audio_dir}\n")
            outf.write(f"Audio file count: {audio_count}\n")
            outf.write(f"Total audio duration (s): {total_duration:.6f}\n")
            outf.write("\nText statistics:\n")
            outf.write(f"  Average chars: {avg_chars:.2f}\n")
            outf.write(f"  Max chars: {max_chars}\n")
            outf.write("\nMissing information:\n")
            outf.write(f"  Missing audio count: {len(missing_audio)}\n")
            outf.write(f"  Missing text count: {len(missing_text)}\n")
            outf.write("\nMissing audio IDs:\n")
            if missing_audio:
                for uid in missing_audio:
                    outf.write(f"- {uid}\n")
            else:
                outf.write("None\n")
            outf.write("\nMissing text IDs:\n")
            if missing_text:
                for uid in missing_text:
                    outf.write(f"- {uid}\n")
            else:
                outf.write("None\n")

        print(f"Dataset summary written to: {summary_path}")
        return {
            "audio_count": audio_count,
            "total_duration": total_duration,
            "avg_chars": avg_chars,
            "max_chars": max_chars,
            "missing_audio": missing_audio,
            "missing_text": missing_text,
            "summary_path": summary_path,
        }


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(base_dir, "sample_text.txt")
    audio_dir = os.path.join(base_dir, "..", "data", "audio")
    checker = DataChecker(text_path=text_path, audio_dir=audio_dir, output_report="report.txt")
    checker.check()
