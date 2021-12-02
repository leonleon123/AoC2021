import os
from typing import Any, Callable


def read_input(
        line_transform: Callable[[str], Any], 
        file_path: str,
        input_file_name: str = 'input.txt'
    ) -> list[Any]:
    with open(f'{os.path.abspath(os.path.dirname(file_path))}/{input_file_name}') as file:
        data = [line_transform(x) for x in file.readlines()]
    return data
