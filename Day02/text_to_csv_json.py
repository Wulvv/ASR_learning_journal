import os

import pandas as pd


def read_text_file(path):
    rows = []
    with open(path, "r", encoding="utf-8") as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            parts = line.split(" ", 1)
            if len(parts) != 2:
                raise ValueError(f"行格式错误，应为 utt_id 和 text: {line}")
            utt_id, text = parts
            rows.append({"utt_id": utt_id, "text": text})
    return rows


def main():
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "Day01", "sample_text.txt"))
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sample_text.csv"))
    json_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sample_text.json"))

    rows = read_text_file(input_path)
    df = pd.DataFrame(rows, columns=["utt_id", "text"])

    df.to_csv(csv_path, index=False, encoding="utf-8")
    print(f"已保存 CSV: {csv_path}")

    df.to_json(json_path, orient="records", force_ascii=False)
    print(f"已保存 JSON: {json_path}")

    df_from_csv = pd.read_csv(csv_path, encoding="utf-8")
    restored = df_from_csv.to_dict(orient="records")
    print("从 CSV 恢复的数据:")
    for item in restored:
        print(item)

    return restored


if __name__ == "__main__":
    main()
