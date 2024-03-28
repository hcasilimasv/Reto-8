import math
def aprox_exp(x, n):
    aprox = 0
    for k in range(n):
        aprox += (x ** k) / math.factorial(k)
    return aprox
def main():
    x = float(input("Escribe un numero real: "))
    n = int(input("Escribe el numero de términos a ejecutar: "))
    aprox = aprox_exp(x, n)
    v_real = math.exp(x)
    error = abs((aprox - v_real) / v_real) * 100
    print("Aproximación de e elevado a " + str(x) + ": " + str(aprox))
    print("El valor real de e elevado a " + str(x) + ": " + str(v_real))
    print("Diferencia: " + str(abs(aprox - v_real)))
    while error >= 0.1:
        n += 1
        aprox = aprox_exp(x, n)
        error = abs((aprox - v_real) / v_real) * 100 
    print("Se obtiene menos del 0.1% de error con " + str(n) + " términos.")
if __name__ == "__main__":
    main()