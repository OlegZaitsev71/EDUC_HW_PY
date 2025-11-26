"""_summary_Тестовый модуль, пример."""

import sys
sys.path.append('../src')

import hw7_main

def test_calc_abs_value():
    assert hw7_main.calc_abs_value(-5) == 5

def test_calc_abs_value2():
    assert hw7_main.calc_abs_value('ABC') is None