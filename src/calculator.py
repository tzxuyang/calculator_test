# import pandas as pd
# import numpy as np 



def calculator(test_mode = 'it', test_string = ''):
    continue_in = 1
    test_string_list = test_string.split(',')
    # print(test_string_list)
    while(continue_in):
        if (test_mode == 'it'):
            equation = input('Please enter equation with number separated with space such as [2 + 8] ')
        else:
            equation = test_string_list.pop()
            # print(equation)
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
        elif (operator == '/'):
            result = num1 / num2
        else:
            result = 'wrong inputs'
        
        print("result is: {}".format(result))
        
        if (test_mode == 'it'):
            stop = input("do you want to stop [Y/N]")
        else:
            if (len(test_string_list)==0):
                stop = 'Y'
            else:
                stop = 'N'


        if (stop == 'Y'):
            continue_in = 0
        else:
            continue_in = 1



if __name__ =="__main__":
    calculator(test_mode = 'it')


