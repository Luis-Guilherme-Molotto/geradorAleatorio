import math

tam = int(60000000)
a = int(16807)
m = int(math.pow(2, 31) - 1)
i = int(1)

n = []
r = []

n.append(2022)  # primeiro elemento do array n[0] = 2022
r.append("")

while i < tam:
    print(i)

    valor = (a * n[i - 1]) % m
    n.append(valor)

    valor = valor / m
    r.append(valor)

    i = i + 1

print(n)
print(r)
