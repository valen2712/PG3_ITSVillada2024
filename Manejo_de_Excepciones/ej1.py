def suma_num():
    seguir = True
    while seguir:
        try:
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            suma = num1 + num2
            print("La suma de los dos números es:", suma)
        except ValueError:
            print("Error: Debes ingresar solo números enteros.")
        finally:
            respuesta = input("¿Desea seguir sumando valores? (s/n): ")
            if respuesta.lower() != 's':
                seguir = False

suma_num()