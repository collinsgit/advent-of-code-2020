import inspect
import os
import re
from typing import List


def clean_data(str) -> str:
    return str.strip('\n')


def get_input() -> List[str]:
    frame = inspect.stack()[1]
    file_path = frame[0].f_code.co_filename
    file_name = os.path.basename(file_path)

    file_format = re.compile(r"day(\d+)\.py")
    m = re.match(file_format, file_name)
    assert m and m.group(1)

    data_file = f"input{m.group(1)}.txt"
    data_path = os.path.join(os.path.dirname(__file__), "..", "..", "input_data", data_file)
    return list(map(clean_data, open(data_path).readlines()))
