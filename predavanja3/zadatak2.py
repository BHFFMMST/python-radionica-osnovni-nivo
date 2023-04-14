"""
Unijeti dva broja i sabrati ih. Ispisati da li je ili nije suma ta dva  broja veća od 20.
"""

a = int(input("Unesite a = "))
b = int(input("Unesite b = "))
suma = a + b
print("a + b =", suma)

if suma > 20:
    print("Suma je veca od 20.")
elif suma == 20:
    print("Suma je jednaka 20.")
else:
    print("Suma je manja od 20.")
    