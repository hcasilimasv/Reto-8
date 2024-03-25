import math
def aprox_seno(x, n):
    aprox = 0
    for k in range(n):
        aprox += ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    return aprox
def main():
    x = float(input("Escribe un numero real "))
    n = int(input("Ingrese el número de términos a ejecutar"))
    aprox = aprox_seno(x, n)
    v_real = math.sin(x)
    print("Aproximación de sin(x) " + str(aprox) + "")
    print("El valor real de sin(x): " + str(v_real) + "")
    print("Diferencia: " + str(abs(aprox - v_real)) + "")
if __name__ == "__main__":
    main()