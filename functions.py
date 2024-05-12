#Clear Terminal:
def Clean():
    import os
    sistema_operacional = os.name
    if sistema_operacional == 'posix':  # Para sistemas UNIX (Linux, macOS)
        os.system('clear')
    elif sistema_operacional == 'nt':  # Para Windows
        os.system('cls')

#Addition:
def Addition(x, y):
    return (x + y)

#Subtraction:
def Subtraction(x, y):
    return (x - y)

#Multiplication:
def Multiplication(x, y):
    return (x * y)

#Division:
def Division(x, y):
    return (x / y)
    
#Exponentiation:
def Exponentiation(x, y):
    return (x ** y)

#Radiciation:
def Radiciation(x, y):
    return (x ** (1 / y))

#logarithm:
def logarithm(x, y):
    from math import log
    return log(x, y)

#Factorial:
def Factorial(x):
    result = x
    for i in range(x - 1, 0, -1):
        result *= i
    return result
