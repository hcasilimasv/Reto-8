import math
def aprox_arcotan(x, n):
    aprox = 0
    for k in range(n):
        termino = ((-1) ** k) * (x ** (2 * k + 1)) / (2 * k + 1)
        aprox += termino
    return aprox
def main():
    x = float(input("Escribe un numero real entre [-1, 1]: "))
    if x < -1 or x > 1:
        print("El valor debe estar en el rango [-1, 1].")
        return
    n = int(input("Ingrese el número de términos a ejecutar: "))
    aprox = aprox_arcotan(x, n)
    v_real = math.atan(x)
    print("Aproximación de arctan(x): " + str(aprox))
    print("El valor real de arctan(x): " + str(v_real))
    print("Diferencia: " + str(abs(aprox - v_real)))
    error = abs((aprox - v_real) / v_real) * 100
    while error >= 0.1:
        n += 1
        aprox = aprox_arcotan(x, n)
        error = abs((aprox - v_real) / v_real) * 100
    print("Se obtiene menos del 0.1% de error con " + str(n) + " términos.")
if __name__ == "__main__":
    main()