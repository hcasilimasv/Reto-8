for n in range(1, 10):
    print("Tabla de multiplicar del " + str(n) + "")
    for i in range(1, 11):
        operacion = n * i
        print("" + str(n) + " x " + str(i) + " = " + str(operacion) + "")
    print()