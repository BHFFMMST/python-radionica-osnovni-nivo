"""
Napisati program koji treba korisniku omogućiti unos broja bodova  od 1-100. 
Zatim program treba prema bodovnoj skali za svaki broj bodova ispisati koju ocjenu je učenik dobio.
Bodovne pragove je potrebno odrediti kao uslove u elif blokovima prema standardnoj tablici bodovanja ucenika.
"""

a = int(input("Unesite broj iz opsega 0-100 "))

if a >= 0 and a <= 100: 
    print("Bodovi =", a)

    if a < 55: 
        print("ocjena 5") 
    elif a >= 55 and a < 65:
        print("ocjena 6")
    elif a >= 65 and a < 75:
        print("ocjena 7")
    elif a >= 75 and a < 85:
        print("ocjena 8")
    elif a >= 85 and a < 95:
        print("ocjena 9")
    else:
        print("ocjena 10")
else:
    print("Uneseni broj nije iz opsega [0, 100]")
