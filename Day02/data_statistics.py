import os

import pandas as pd


def main():
    csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "sample_text.csv"))
    if not os.path.exists(csv_path):
        print(f"CSV 文件不存在: {csv_path}")
        return

    df = pd.read_csv(csv_path, encoding="utf-8")
    df["char_count"] = df["text"].astype(str).apply(len)

    total_samples = len(df)
    avg_chars = df["char_count"].mean()
    min_chars = df["char_count"].min()
    max_chars = df["char_count"].max()

    print(f"总样本数: {total_samples}")
    print(f"字符数平均值: {avg_chars:.2f}")
    print(f"字符数最小值: {min_chars}")
    print(f"字符数最大值: {max_chars}")

    long_df = df[df["char_count"] > 10]
    long_csv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "long_sentences.csv"))
    long_df.to_csv(long_csv_path, index=False, encoding="utf-8")
    print(f"已保存字符数大于 10 的样本: {long_csv_path}")

    return df, long_df


if __name__ == "__main__":
    main()
