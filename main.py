import pandas as pd 
# import numpy as np 
from src.calculator import calculator

if __name__=='__main__':

    testing_string = "2 + 8,3 * 7,4 / 6,1.2 - 2.4"

    # print(testing_string)

    calculator(test_mode='test', test_string = testing_string)




