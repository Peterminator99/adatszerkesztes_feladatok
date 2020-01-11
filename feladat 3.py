with open("szamok3.txt") as f:
    numbers = f.read()


numbers = numbers.replace(" ", "")
numbers = numbers.split("\n")

lista = []
for num in numbers:
    if num != "":
        lista.append(int(num))

print(f"A szamok darabszama: {len(lista)}")


osszeg = 0

for i in lista:
    osszeg += int(i)

print(f"A szamok osszege: {osszeg}")

atlag = osszeg / len(lista)

print(f"A szamok atlaga: {atlag}")

print(f"A legkisebb szam: {min(lista)}")
print(f"A legnagyobb szam: {max(lista)}")

print("A szamok forditva:")

lista.reverse()

i = 0
for szam in lista:
    print(szam)
    i += 1

lista.sort()

print("A szamok novekvo sorrendben:")

i = 0
for szam in lista:
    print(szam)
    i += 1

lista.reverse()

print("A szamok csokkeno sorrendben:")

i = 0
for szam in lista:
    print(szam)
    i += 1

print("Az egyedi szamok:")

egyedi = set(lista)
szamlalo = 0

for szam in egyedi:
    print(szam)
    szamlalo += 1

print(f"Az egyedi szamok szama: {szamlalo}")

for szam in egyedi:
    print(f"A(z) {szam} szambol {lista.count(szam)} db van.")
