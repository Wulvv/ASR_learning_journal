import os
import glob


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


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(base_dir, "sample_text.txt")
    audio_dir = os.path.join(base_dir, "..", "data", "audio")
    checker = DataChecker(text_path=text_path, audio_dir=audio_dir, output_report="report.txt")
    checker.check()
