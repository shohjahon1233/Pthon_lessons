from datetime import datetime

def foydalanuvchi(ism, familiya, tugilgan_yil, tugilgan_joy,
                  email=None, telefon=None):
    yosh = datetime.now().year - tugilgan_yil
    return {
        "ism": ism,
        "familiya": familiya,
        "tugilgan_yil": tugilgan_yil,
        "tugilgan_joy": tugilgan_joy,
        "email": email,
        "telefon": telefon,
        "yosh": yosh
    }

mijozlar = []

while True:
    ism = input("Ism: ")
    familiya = input("Familiya: ")
    yil = int(input("Tug'ilgan yil: "))
    joy = input("Tug'ilgan joy: ")
    email = input("Email (ixtiyoriy): ")
    telefon = input("Telefon (ixtiyoriy): ")

    mijoz = foydalanuvchi(
        ism,
        familiya,
        yil,
        joy,
        email if email else None,
        telefon if telefon else None
    )

    mijozlar.append(mijoz)

    yana = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")
    if yana.lower() != "ha":
        break

print("\nMijozlar ro'yxati:")
for m in mijozlar:
    print(m)


def eng_katta(a, b, c):
    return max(a, b, c)

print("Eng katta:", eng_katta(10, 25, 18))


import math

def aylana(radius):
    return {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * math.pi * radius,
        "yuza": math.pi * radius ** 2
    }

print(aylana(5))


def tub_sonlar(boshlanish, tugash):
    natija = []

    for son in range(max(2, boshlanish), tugash + 1):
        tub = True
        for i in range(2, int(son ** 0.5) + 1):
            if son % i == 0:
                tub = False
                break
        if tub:
            natija.append(son)

    return natija

print(tub_sonlar(1, 50))


def fibonacci(n):
    royxat = []
    a, b = 1, 1

    while len(royxat) < n:
        royxat.append(a)
        a, b = b, a + b

    return royxat

print(fibonacci(10))