n = int(input("Escriba un numero positivo que va ser el exponente de 2"))
if n < 0:
    print("El exponente debe ser un numero entero no negativo")
else:
    exp = 1
    for n in range(n):
        exp *= 2
    print("2 elevado a la potencia " + str(n + 1) + " es igual a: " + str(exp) + "")