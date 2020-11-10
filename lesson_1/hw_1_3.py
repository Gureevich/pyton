a = input("Vvedite cislo ")
b = f"{a}{a}"
c = f"{a}{a}{a}"
print (a, b, c)
print (int(a) + int(b) + int(c))

a = input("Vvedite cislo ")
print (int(a) + int(f"{a}{a}") + int(f"{a}{a}{a}"))
