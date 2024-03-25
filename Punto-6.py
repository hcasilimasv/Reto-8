def pot(x, n):
  exp = 1
  for n in range(n):
    exp *= x
  return exp
x = float(input("Escriba un numero real"))
n = int(input("Escriba un numero natural"))
pot_x_n = pot(x, n)
print("El resultado de " + str(x) + "  elevado a " + str(n) + " es  " + str(pot_x_n) + "")