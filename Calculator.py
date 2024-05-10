import CalculatorFunctions

#Variables:
choices = [None, None]
values = [None, None, None]

#Calculator:
while True:

    #Input First Value:
    while True:
        try:
            values[1] = float(input("Sistema: Insira 1° Valor: "))
            CalculatorFunctions.Clean()
            break
        except:
            print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
            pass

    while True:
        #Input operation:
        while True:
            try:
                print("|------------------------------------------------------------------------------------------------------------------------------------------------|")
                print("| '+' = Adição | '-' = Subtração | 'x' = Multiplicação | '/' = Divisão | 'p' = Potenciação | 'r' = Radiciação | 'l' = Logaritmo | '!' = Fatorial |")
                print("|------------------------------------------------------------------------------------------------------------------------------------------------|")
                values[0] = str(input("\nSistem: Insira Operação: ").lower())
                if values[0] != '+' and values[0] != '-' and values[0] != 'x' and values[0] != '/' and values[0] != 'p' and values[0] != 'r' and values[0] != 'l' and values[0] != '!':
                    print("Sistema: 3RR0R! \nSistema: Operação Invalida! \n")
                    pass
                else:
                    CalculatorFunctions.Clean()
                    break
            except:
                print("Sistema: 3RR0R! \nSistema: Operação Invalida! \n")
                pass

        #Addition:
        if values[0] == "+":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            Result = CalculatorFunctions.Addition(values[1], values[2])
            print(f"Sistema: {values[1]} + {values[2]} = {Result}")
        
        #Subtraction:
        elif values[0] == "-":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            Result = CalculatorFunctions.Subtraction(values[1], values[2])
            print(f"Sistema: {values[1]} - {values[2]} = {Result}")

        #Multiplication:
        elif values[0] == "x":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            Result = CalculatorFunctions.Multiplication(values[1], values[2])
            print(f"Sistema: {values[1]} x {values[2]} = {Result}")

        #Division:
        elif values[0] == "/":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            if values[2] != 0:
                Result = CalculatorFunctions.Division(values[1], values[2])
                print(f"Sistema: {values[1]} ÷ {values[2]} = {Result}")
            else:
                print(f"Sistema: {values[1]} ÷ {values[2]} = Indeterminado")
                break

        #Exponentiation:
        elif values[0] == "p":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            Result = CalculatorFunctions.Exponentiation(values[1], values[2])
            print(f"Sistema: {values[1]} ^ {values[2]} = {Result}")

        #Radiciation:
        elif values[0] == "r":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            if values[1] == 0:
                print(f"Sistema: Raiz {values[2]}° de {values[1]} = 0")
                break
            elif values[1] < 0:
                print(f"Sistema: Raiz {values[2]}° de {values[1]} ∉ ℝ")
                break
            elif values[1] == 1 and values[2] == 0:
                print(f"Sistema: Raiz {values[2]}° de {values[1]} = 1")
            elif values[1] != 1 and values[2] == 0:
                print(f"Sistema: Raiz {values[2]}° de {values[1]} = Inexistente")
                break
            else:
                Result = CalculatorFunctions.Radiciation(values[1], values[2])
                print(f"Sistema: Raiz {values[2]}° de {values[1]} = {Result}")

        #logarithm:
        elif values[0] == "l":

            #Input Second Value:
            while True:
                try:
                    values[2] = float(input("Sistema: Insira 2° Valor: "))
                    CalculatorFunctions.Clean()
                    break
                except:
                    print("Sistema: 3RR0R! \nSistema: Valor Invalido! \n")
                    pass
            
            #Performing Operation:
            if values[1] > 0 and values[2] > 0 and values[2] != 0:
                Result = CalculatorFunctions.logarithm(values[1], values[2])
                print(f"Sistema: log({values[1]}) na base {values[2]} = {Result}")
            else:
                print(f"Sistema: log({values[1]}) na base {values[2]} = Inexistente")
                break

        #Factorial:
        elif values[0] == "!":

            #Performing Operation:
            if values[1] > 0 and values[1] == round(values[1], 0):
                if values[1] == 0 or values[1] == 1:
                    Result = 1
                else:
                    Result = CalculatorFunctions.Factorial(int(values[1]))
                print(f"Sistema: {values[1]}! = {Result}")
            else:
                print(f"Sistema: {values[1]}! = Inexistente")
        
        try:
            while True:
                try:
                    choices[0] = str(input("Sistema: Deseja Finalizar O Calculo?: ").lower())
                    if choices[0] != "s" and choices[0] != "sim" and choices[0] != "claro" and choices[0] != "y" and choices[0] != "yes" and choices[0] and "yeah" and choices[0] != "ok" and choices[0] != "bl" and choices[0] != "blz" and choices[0] != "n" and choices[0] != "nao" and choices[0] != "não" and choices[0] != "no" and choices[0] != "not":
                        print("Sistema: 3RR0R! \nSistema: Resposta Invalida! \n")
                        pass
                    else:
                        break
                except:
                    print("Sistema: 3RR0R! \nSistem: ERRO DESCONHECIDO! \n")
            if choices[0] == "s" or choices[0] == "sim" or choices[0] == "claro" or choices[0] == "y" or choices[0] == "yes" or choices[0] == "yeah" or choices[0] == "ok" or choices[0] == "bl" or choices[0] == "blz":
                break
            else:
                values[1] = Result
                CalculatorFunctions.Clean()
                pass
        except:
            print("Sistema: 3RR0R! \nSistem: ERRO DESCONHECIDO! \n")
            pass

    try:
        while True:
            try:
                choices[0] = str(input("Sistema: Deseja Finalizar O Sistema?: ").lower())
                if choices[0] != "s" and choices[0] != "sim" and choices[0] != "claro" and choices[0] != "y" and choices[0] != "yes" and choices[0] and "yeah" and choices[0] != "ok" and choices[0] != "bl" and choices[0] != "blz" and choices[0] != "n" and choices[0] != "nao" and choices[0] != "não" and choices[0] != "no" and choices[0] != "not":
                    print("Sistema: 3RR0R! \nSistema: Resposta Invalida! \n")
                    pass
                else:
                    break
            except:
                print("Sistema: 3RR0R! \nSistem: ERRO DESCONHECIDO! \n")
        if choices[0] == "s" or choices[0] == "sim" or choices[0] == "claro" or choices[0] == "y" or choices[0] == "yes" or choices[0] == "yeah" or choices[0] == "ok" or choices[0] == "bl" or choices[0] == "blz":
            print("Finalizando Sistema... \nSistema Finalizado. \n")
            break
        else:
            pass
    except:
        print("Sistema: 3RR0R! \nSistem: ERRO DESCONHECIDO! \n")
        pass