import math as m

x = float(input("Digite o valor de X: "))

if (x > 4.0 or x < (-4.0)):
    fx = (5*x+3)/m.sqrt(x**2-16)
    print(f"\nf(x) = {fx}")
else:
    print("\nNao pode ser feita.")
