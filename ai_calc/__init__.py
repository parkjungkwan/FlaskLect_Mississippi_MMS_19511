from ai_calc.model import CalcModel
from warnings import simplefilter
simplefilter(action='ignore', category=FutureWarning)

if __name__ == '__main__':
    calc = CalcModel()
    calc.create_add_model()
"""
    calc.create_sub_model()
    calc.create_mul_model()
    calc.create_div_model()
"""
