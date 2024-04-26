def nombre_mes():
    meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
    try:
        numero_mes = int(input("Ingrese el número de mes (1-12): "))
        nomb_mes = meses[numero_mes - 1]
        print("El nombre del mes es:", nomb_mes)
    except IndexError:
        print("Error: El número de mes ingresado está fuera de rango.")

nombre_mes()