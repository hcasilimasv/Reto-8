n = int(input("Escriba un número natural positivo "))
if n < 1:
    print("El numero escrito no es valido. Debe ser mayor o igual a 1")
else:
    print("Numero   Factorial")
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j
        print("" + str(i) + "        " + str(fact) + "")