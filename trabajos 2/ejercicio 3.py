
altura = int(input("Altura: "))

print("triangulo")
for i in range(1, altura + 1):
        print("*" * i)

print("triangulo invertido")
for i in range(altura, 0, -1):
        print("*" * i)

print("triangulo centrado")
for i in range(1, altura + 1):
        print(" " * (altura - i) + "*" * (2 * i - 1))

print("tringulo contra invertido")
for i in range(altura, 0, -1):
        print(" " * (altura - i) + "*" * (2 * i - 1))