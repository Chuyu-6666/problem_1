from pathlib import Path
from data_loader import load_attachment_one,interpolate_every_second
from geometry import generate_geometry
from heat_transfer import calculate_temperature_change


ATTACHMENT_ONE = Path(__file__).resolve().parents[2] / "附件" / "附件1.xlsx"


def main() -> None:
    #数据插值
    temperature_data, moisture_data = load_attachment_one(ATTACHMENT_ONE)
    temperature = interpolate_every_second(temperature_data)
    moisture = interpolate_every_second(moisture_data)

    print(f"温度：{temperature}")
    print(len(temperature))


if __name__ == "__main__":
    main()
