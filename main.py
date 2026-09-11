from pathlib import Path

from data_loader import load_attachment_one

ATTACHMENT_ONE = Path(__file__).resolve().parents[2] / "附件" / "附件1.xlsx"


def main() -> None:
    temperature_data, moisture_data = load_attachment_one(ATTACHMENT_ONE)

    print(f"已读取 {len(temperature_data)} 个数据点")
    print("温度数据 [time, temperature]：")
    print(temperature_data)
    print("水分数据 [time, moisture]：")
    print(moisture_data)


if __name__ == "__main__":
    main()
