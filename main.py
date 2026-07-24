import math

# 1.
son1 = float(input("Son kiriting: "))
print("Natija:", math.ceil(son1))

# 2.
son2 = float(input("Son kiriting: "))
print("Natija:", math.floor(son2))

# 3.
x1, y1 = float(input("x1: ")), float(input("y1: "))
x2, y2 = float(input("x2: ")), float(input("y2: "))
print("Masofa:", math.dist((x1, y1), (x2, y2)))

# 4.
n = float(input("Musbat son kiriting: "))
print("Natija:", round(math.log10(n), 3))

# 5.
kub = lambda x: x ** 3
a = float(input("Son kiriting: "))
print("Kubi:", kub(a))

# 6.
yigindi = lambda x, y: x + y
b, c = float(input("1-son: ")), float(input("2-son: "))
print("Yig'indi:", yigindi(b, c))

# 7.
sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toq_sonlar = list(filter(lambda x: x % 2 != 0, sonlar))
print("Toq sonlar:", toq_sonlar)

# 8.
royhat = [1, 2, 3, 4, 5]
kvadratlar = list(map(lambda x: x ** 2, royhat))
print("Kvadratlar:", kvadratlar)