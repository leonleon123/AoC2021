import os
import re
from typing import Callable


def read_input_lines(
    line_f: Callable,
    file_path: str,
    split: str = None,
    input_file_name: str = 'input.txt',
) -> list:
    with open(f'{os.path.abspath(os.path.dirname(file_path))}/{input_file_name}') as file:
        return [line_f(*re.split(split, x)) if split else line_f(x) for x in file.readlines()]

def read_input(
    file_path: str,
    input_file_name: str = 'input.txt'
) -> str:
    with open(f'{os.path.abspath(os.path.dirname(file_path))}/{input_file_name}') as file:
        return file.read()
