"""Пример hw7_main.py."""

def calc_abs_value(value):
    if not isinstance(value, int):
        return None
    if value > 0:
        return value
    else:
        return -1 * value