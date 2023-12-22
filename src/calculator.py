# import pandas as pd
# import numpy as np 



def calculator():
    continue_in = 1
    while(continue_in):
        equation = input('Please enter equation with number separated with space such as [2 + 8] ')
        equation_list = equation.split(' ')
        num1 = float(equation_list[0])
        num2 = float(equation_list[2])
        operator = equation_list[1]

        if (operator == '+'):
            result = num1 + num2
        elif (operator == '-'):
            result = num1 - num2
        elif (operator == '*'):
            result = num1 * num2
        elif (operator == '-'):
            result = num1 / num2
        else:
            result = 'wrong inputs'
        
        print("result is: {}".format(result))
        
        stop = input("do you want to stop [Y/N]")

        if (stop == 'Y'):
            continue_in = 0
        else:
            continue_in = 1



if __name__ =="__main__":
    calculator()


