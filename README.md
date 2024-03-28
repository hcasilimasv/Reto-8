# Reto-8


#### 1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

```python
#Se define el ciclo for y el rango
for n in range(1, 101):
    print("Numero " + str(n) + " , Cuadrado = " + str(n*n) +  " ")
```


#### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

``` python
print("Numeros impares del 1 al 999:")

#se define el ciclo for y el rango para numeros pares e imprimimos
for n_par in range(1, 1000, 2):
    print("" + str(n_par) + "")
print("Numeros pares del 2 al 1000:")

#se define el ciclo for y el rango para numero impares e imprimos
for n_impar in range(2, 1001, 2):
    print("" + str(n_impar) + "")
```


#### 3.Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado.

``` python
#se solicita al usuario a ingrese un numero
n = int(input("Escriba un numero natural par mayor o igual que dos"))

#Se verifica si el número ingresado es menor que 2
if n < 2:
    print("El numero escrito no es válido. Debe ser mayor o igual a 2")
else:
    print("Los numeros pares descendentes hasta 2 son:")

#Se recorre sobre los números descendentes desde n hasta 2 con un paso de -1
    for i in range(n, 1, -1):

#Se verifica si el número actual (i) es par e imprimimos
        if i % 2 == 0:
            print("" + str(i) + "")
```


#### 4.Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial.

``` python
#Se solicita al usuario que ingrese un número natural positivo
n = int(input("Escriba un número natural positivo "))

#Se verifica si el número ingresado es menor que 1
if n < 1:
    print("El numero escrito no es valido. Debe ser mayor o igual a 1")
else:
    print("Numero   Factorial")
#Se recorre sobre los números desde 1 hasta el número ingresado por el usuari
    for i in range(1, n + 1):

#Se inicializa el factorial como 1 para cada número
        fact = 1

#Se recorre sobre los números desde 1 hasta el número actual (inclusive)
        for j in range(1, i + 1):

# Se calcula el factorial del número actual
            fact *= j
        print("" + str(i) + "        " + str(fact) + "")
```


#### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.

``` python
#Se solicita al usuario que ingrese un número que será el exponente de 2
n = int(input("Escriba un numero positivo que va ser el exponente de 2"))

#Se verifica si el exponente ingresado es menor que 0
if n < 0:
    print("El exponente debe ser un numero entero no negativo")
else:

#Si el exponente es válido, se inicializa la variable de la exponenciación como 1
    exp = 1

#Se recorre n veces
    for n in range(n):

#Se calcula la exponenciación de 2 elevado a n
        exp *= 2

#Se imprime el resultado de la exponenciación
    print("2 elevado a la potencia " + str(n + 1) + " es igual a: " + str(exp) + "")
```


#### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).

``` python
#Se define una función llamada "pot" que calcula la potencia de un número x elevado a n
def pot(x, n):

#Se inicializa la variable de la exponenciación como 1
  exp = 1

#Se recorre n veces
  for n in range(n):

#Se calcula la exponenciación de x elevado a n y se devuelve el resultado de la exponenciación
    exp *= x
  return exp

#Se solicita al usuario que ingrese un número real y uno natural
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))

#Se llama a la función "pot" para calcular x elevado a n y se imprime el resultado
pot_x_n = pot(x, n)
print("El resultado de " + str(x) + "  elevado a " + str(n) + " es  " + str(pot_x_n) + "")
```


#### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.

``` python
#Se recorre sobre los números del 1 al 9
for n in range(1, 10):
    print("Tabla de multiplicar del " + str(n) + "")

#Se recorren los números del 1 al 10
    for i in range(1, 11):

#Se multiplica n * i y se imprime
        operacion = n * i
        print("" + str(n) + " x " + str(i) + " = " + str(operacion) + "")

#Se imprime una línea en blanco para separar las tablas de multiplicar
    print()
```


#### A partir de este punto, los códigos no admiten un número mayor a 150. Es decir, "Ingresar un número real = 456", al intentar ingresar un valor mayor o menor a 150 en algunos códigos del punto 8 al 10, se generará un error. Esto se debe a la cantidad de cálculos que se realizan, los cuales son tantos que provocan un error.
[![Captura11.png](https://i.postimg.cc/DmVHmbCb/Captura11.png)](https://postimg.cc/FkZDB1X9)
#### Aunque es posible que se puedan ingresar números grandes, pero lo más probable es que marque error. Gracias por leer esta pequeña información.



#### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.


``` python
#Se importa el módulo math para utilizar la función factorial y la función exponencial
import math

#Se Inicializa la aproximación como 0
def aprox_exp(x, n):
    aprox = 0

#Se recorre los primeros n términos de la serie de Maclaurin para la exponencial
    for k in range(n):

#Utilizamos esta formula para calcular cada término de la serie y los suma a la aproximación y regresamos la funcion
        aprox += (x ** k) / math.factorial(k)
    return aprox
def main():

#Se solicita al usuario que ingrese un número real y el número de términos a ejecutar
    x = float(input("Escribe un numero real: "))
    n = int(input("Escribe el numero de términos a ejecutar: "))

#Se calcula la aproximación de "e" elevado a "x" utilizando la función definida
    aprox = aprox_exp(x, n)
    
#Se calcula el valor real de "e" elevado a "x" utilizando la función de exponencial de math
    v_real = math.exp(x)

#Se calcula el valor del error obtenido
    error = abs((aprox - v_real) / v_real) * 100

#Imprimimos
    print("Aproximación de e elevado a " + str(x) + ": " + str(aprox))
    print("El valor real de e elevado a " + str(x) + ": " + str(v_real))
    print("Diferencia: " + str(abs(aprox - v_real)))

#Creamos un bucle para calcular que el error no se mayor a 0.1%
    while error >= 0.1:
        n += 1
        aprox = aprox_exp(x, n)

#Imprimimos y se Llamamos a la función main si el script es ejecutado directamente
        error = abs((aprox - v_real) / v_real) * 100 
    print("Se obtiene menos del 0.1% de error con " + str(n) + " términos.")
if __name__ == "__main__":
    main()
```


#### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.

[![Captura5.png](https://i.postimg.cc/PxgN3PXJ/Captura5.png)](https://postimg.cc/ftvwkW0Q)

``` python
#Se importa el módulo math para utilizar la función factorial y la función seno
import math
def aprox_seno(x, n):

#Se inicializa la aproximación como 0
    aprox = 0

#Se recorre los primeros n términos de la serie de Maclaurin para el seno
    for k in range(n):

#Utilizamos esta formula para calcular cada término de la serie y los suma a la aproximación
        aprox += ((-1) ** k) * (x ** (2 * k + 1)) / math.factorial(2 * k + 1)
    return aprox
def main():

#Solicitamos al usuario que ingrese un número real y el número de términos a ejecutar
    x = float(input("Escribe un numero real: "))
    n = int(input("Ingrese el número de términos a ejecutar: "))

#Se calcula la aproximación del seno de x utilizando la función definida
    aprox = aprox_seno(x, n)

#Se calcula el valor real del seno de x utilizando la función de seno de math
    v_real = math.sin(x)

#Se imprime
    print("Aproximación de sin(x): " + str(aprox))
    print("El valor real de sin(x): " + str(v_real))
    print("Diferencia: " + str(abs(aprox - v_real)))

#Se calcula el valor del error obtenido
    error = abs((aprox - v_real) / v_real) * 100

#Creamos un bucle para calcular que el error no se mayor a 0.1% e imprimimos
    while error >= 0.1:
        n += 1
        aprox = aprox_seno(x, n)
        error = abs((aprox - v_real) / v_real) * 100
    print("Se obtiene menos del 0.1% de error con " + str(n) + " términos.")

#Se Llamamos a la función main si el script es ejecutado directamente
if __name__ == "__main__":
    main()
```


#### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.

[![Captura6.png](https://i.postimg.cc/5NM68YKk/Captura6.png)](https://postimg.cc/G9qLC2Ck)

``` python
#Se importa el módulo math para utilizar la función arcotangente
import math
def aprox_arcotan(x, n):

#Inicializamos la aproximación como 0
    aprox = 0

#Se recorre los primeros n términos de la serie de Maclaurin para la arcotangente
    for k in range(n):

#Calculamos cada término de la serie y suma del término actual a la aproximación
        termino = ((-1) ** k) * (x ** (2 * k + 1)) / (2 * k + 1)
        aprox += termino
    return aprox
def main():

#Se solicita al usuario que ingrese un número real en el rango [-1, 1]
    x = float(input("Escribe un numero real entre [-1, 1]: "))

#Se verifica si el número está dentro del rango permitido
    if x < -1 or x > 1:
        print("El valor debe estar en el rango [-1, 1].")
        return
    
#Solicitamos al usuario que ingrese el número de términos a ejecutar
    n = int(input("Ingrese el número de términos a ejecutar: "))

#Calculamos la aproximación de la arcotangente de x utilizando la función definida
    aprox = aprox_arcotan(x, n)

#Calculamos el valor real de la arcotangente de x utilizando la función de arcotangente de math
    v_real = math.atan(x)

#Se imprime
    print("Aproximación de arctan(x): " + str(aprox))
    print("El valor real de arctan(x): " + str(v_real))
    print("Diferencia: " + str(abs(aprox - v_real)))

#Se calcula el valor del error obtenido
    error = abs((aprox - v_real) / v_real) * 100

#Creamos un bucle para calcular que el error no se mayor a 0.1% e imprimimos
    while error >= 0.1:
        n += 1
        aprox = aprox_arcotan(x, n)
        error = abs((aprox - v_real) / v_real) * 100
    print("Se obtiene menos del 0.1% de error con " + str(n) + " términos.")

#Se Llamamos a la función main si el script es ejecutado directamente
if __name__ == "__main__":
    main()
```
