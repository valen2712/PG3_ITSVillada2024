try:
    with open("archivo.txt", "w") as archivo:
        archivo.write(123) 
except TypeError as e:
    print("Error:", e)