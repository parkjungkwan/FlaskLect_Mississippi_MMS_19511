from ai_calc.model import CalcModel
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)
import os


if __name__ == '__main__':
    calc = CalcModel()

    if not os.path.exists('saved_add/checkpoint'):
        calc.create_add_model()

    if not os.path.exists('saved_sub/checkpoint'):
        calc.create_sub_model()

    if not os.path.exists('saved_mul/checkpoint'):
        calc.create_mul_model()

    if not os.path.exists('saved_div/checkpoint'):
        calc.create_div_model()
