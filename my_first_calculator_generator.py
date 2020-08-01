#my_first_calculator_generator by https://github.com/ju8crafter-jaXnein
#inspired by https://github.com/AceLewis/my_first_calculator.py/blob/master/my_first_calculator.py

import os
LOCAL_DIR = os.path.dirname(__file__)
SIGNS = ["+", "-", "/", "*"]

print("WARNING: Generating with a number larger than 100 can cause perfromance issues")
num = int(input("Choose to what positive number \"my_first_calculator.py\" should be able to calculate: "))

f=open(os.path.join(LOCAL_DIR,"my_first_calculator.py"),"w")
f.write("#my_first_calculator_generator by https://github.com/ju8crafter-jaXnein \n #inspired by https://github.com/AceLewis/my_first_calculator.py/blob/master/my_first_calculator.py")
f.close()

f=open(os.path.join(LOCAL_DIR,"my_first_calculator.py"),"a")
f.write("""
print('Welcome to this calculator!')
print('It can add, subtract, multiply and divide whole numbers from 0 to """+str(num)+"""')
num1 = int(input('Please choose your first number: '))
sign = input('What do you want to do? +, -, /, or *: ')
num2 = int(input('Please choose your second number: '))
""")

def sign_calc(number_1, number_2, operator):
    if operator == '+':
        return (num1+num2)
    elif operator == '-':
        return (num1-num2)
    elif operator == '/':
        if not (num1 == 0 or num2 == 0):
            return (num1/num2)
        else:
            return "Inf"
    elif operator == '*':
        return (num1*num2)

for sign in SIGNS:
    for num1 in range(num+1):
        for num2 in range(num+1):
            f.write("""
if num1 == """+str(num1)+""" and sign == \'"""+sign+"""\' and num2 == """+str(num2)+""":
    print(\""""+str(num1)+sign+str(num2)+""" = """+str(sign_calc(num1, num2, sign))+"""\")""")

f.write("""
print("Thanks for using this calculator, goodbye :)")""")
f.close()