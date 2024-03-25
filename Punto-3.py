n = int(input("Escriba un numero natural par mayor o igual que dos"))
if n < 2:
    print("El numero escrito no es válido. Debe ser mayor o igual a 2")
else:
    print("Los numeros pares descendentes hasta 2 son:")
    for i in range(n, 1, -1):
        if i % 2 == 0:
            print("" + str(i) + "")