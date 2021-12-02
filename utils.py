import os
from typing import Any, Callable


def read_input_lines(
        line_f: Callable, 
        file_path: str,
        split: str = None,
        input_file_name: str = 'input.txt',
    ) -> list[Any]:
    with open(f'{os.path.abspath(os.path.dirname(file_path))}/{input_file_name}') as file:
        data = [line_f(*x.split(split)) if split else line_f(x) for x in file.readlines()]
    return data
