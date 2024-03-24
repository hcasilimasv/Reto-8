# Reto-8


#### 1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
for n in range(1, 101):
    print("Numero " + str(n) + " , Cuadrado = " + str(n*n) +  " ")
```


#### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

``` python
print("Numeros impares del 1 al 999:")
for n_par in range(1, 1000, 2):
    print("" + str(n_par) + "")
print("Numeros pares del 2 al 1000:")
for n_impar in range(2, 1001, 2):
    print("" + str(n_impar) + "")
```


#### 3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

``` python
n = int(input("Escriba un numero natural par mayor o igual que dos"))
if n < 2:
    print("El numero escrito no es válido. Debe ser mayor o igual a 2")
else:
    print("Los numeros pares descendentes hasta 2 son:")
    for i in range(n, 1, -1):
        if i % 2 == 0:
            print("" + str(i) + "")
```


#### 4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

``` python
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
```


#### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

``` python
n = int(input("Escriba un numero positivo que va ser el exponente de 2"))
if n < 0:
    print("El exponente debe ser un numero entero no negativo")
else:
    exp = 1
    for n in range(n):
        exp *= 2
    print("2 elevado a la potencia " + str(n + 1) + " es igual a: " + str(exp) + "")
```


#### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

``` python
def pot(x, n):
  exp = 1
  for n in range(n):
    exp *= x
  return exp
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))
pot_x_n = pot(x, n)
print("El resultado de " + str(x) + "  elevado a " + str(n) + " es  " + str(pot_x_n) + "")
```


#### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

``` python
for n in range(1, 10):
    print("Tabla de multiplicar del " + str(n) + "")
    for i in range(1, 11):
        operacion = n * i
        print("" + str(n) + " x " + str(i) + " = " + str(operacion) + "")
    print()
```


#### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.

[![Captura4.png](https://i.postimg.cc/52gY443K/Captura4.png)](https://postimg.cc/ts1CDH8F)

``` python
import math
def aprox_exp(x, n):
    aprox = 0
    for k in range(n):
        aprox += (x ** k) / math.factorial(k)
    return aprox
def main():
    x = float(input("Escribe un numero real"))
    n = int(input("Escribe el numero del terminos a ejecutar"))
    aprox = aprox_exp(x, n)
    v_real = math.exp(x)
    print("Aproximación de e elevado a " + str(x) + ": " + str(aprox) + "")
    print("El valor real de e elevado a " + str(x) + ": " + str(v_real) + "")
    print("Diferencia: " + str(abs(aprox - v_real)) + "")
if __name__ == "__main__":
    main()
```


#### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

[![Captura5.png](https://i.postimg.cc/PxgN3PXJ/Captura5.png)](https://postimg.cc/ftvwkW0Q)

``` python
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
```


#### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

[![Captura6.png](https://i.postimg.cc/5NM68YKk/Captura6.png)](https://postimg.cc/G9qLC2Ck)

``` python
import math
def aprox_arcotan(x, n):
    aprox = 0
    for k in range(n):
        termino = ((-1) ** k) * (x ** (2 * k + 1)) / (2 * k + 1)
        aprox += termino
    return aprox
def main():
    x = float(input("Escribe un numero real entre [-1, 1] "))
    if x < -1 or x > 1:
        print("El valor debe estar en el rango [-1, 1].")
        return
    n = int(input("Ingrese el número de términos a ejecutar"))
    aprox = aprox_arcotan(x, n)
    v_real = math.atan(x)
    print("Aproximación de arctan(x) " + str(aprox) + "")
    print("El valor real de arctan(x): " + str(v_real) + "")
    print("Diferencia: " + str(abs(aprox - v_real)) + "")
if __name__ == "__main__":
    main()
```
