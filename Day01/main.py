import os
from data_checker import DataChecker


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    text_path = os.path.join(base_dir, "sample_text.txt")
    audio_dir = os.path.join(base_dir, "..", "data", "audio")

    checker = DataChecker(text_path=text_path, audio_dir=audio_dir, output_report="report.txt")
    checker.check()
