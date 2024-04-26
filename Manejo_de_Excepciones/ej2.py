def division_num():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        division = num1 / num2
        print("La división del primer número respecto al segundo es:", division)
    except ValueError:
        print("Error: Debes ingresar números.")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

division_num()