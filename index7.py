"""
7. Modifique o programa anterior de forma que o usuário
também digite o início e o fim da tabuada, em vez de
começar com 1 e 10.
"""
n = int(input("Tabuada de: "))
x = 1
while x <= 10:
 print(n, "x", x, "=", n*x, ",")
 x = x + 1