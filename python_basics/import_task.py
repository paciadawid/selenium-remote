from python_basics.calculator import Calculator
from python_basics.functions import calculate_fuel


a_tuple = (1, 2, 3)

try:
    a_tuple[0] = 1
except TypeError as err:
    print(err)