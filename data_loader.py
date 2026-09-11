from openpyxl import load_workbook
import numpy as np


def load_attachment_one(path):
    workbook = load_workbook(path, read_only=True, data_only=True)
    worksheet = workbook.active

    data = np.array([
        row
        for row in worksheet.iter_rows(
            min_row=2,
            min_col=1,
            max_col=3,
            values_only=True,
        )
        if row[0] is not None
    ], dtype=float)

    workbook.close()

    #均为{[time,temperature]},{[time,moisture]}，便于后续的线性插值
    temperature_data = data[:, [0,1]]
    moisture_data = data[:, [0,2]]

    return temperature_data, moisture_data



def interpolate_every_second(data):
    original_time = data[:, 0]
    original_value = data[:, 1]

    # 生成从起始时间到结束时间、间隔为 1 秒的时间数组
    target_time = np.arange(
        original_time[0],
        original_time[-1] + 1,
        1,
    )

    # 线性插值
    target_value = np.interp(
        target_time,
        original_time,
        original_value,
    )

    # 合并成 [time, value] 格式
    return target_value


