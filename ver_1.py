import math

v = float(input("Введите коэффициент Пуассона: "))

l = v / ((1 + v)*(1 - 2 * v))
nu = 1 / (2 * (1 + v))

print("л = " + "{0:.4f}".format(l))
print("n = " + "{0:.4f}".format(nu))

e = float(input("Введите упругость: "))
r = float(input("Введите радиус: "))
p = float(input("Введите плотность: "))
hr = float(input("Введите толщину оболочки: "))
t = float(input("Введите шаг по времени: "))
b = float(input("Что-то: ")) #посмотреть
hz = float(input("Что-то 2: ")) #посмотреть

anu = nu/t

a1 = (e + anu) * ((b * nu * t**2) / (r * hк * p))
print("A1 = ", a1)
a2 = (e + anu) * ((2 * nu * t**2) / ((r**2)*p)) - 2
print("A2 = ", a2)
a3 = (e + anu) * ((nu * t**2) / ((hz**2) * p))
print("A3 = ", a3)
b1 = (e + anu) * (3 * ((l + 2 * nu) / (hr**2)) - ((l - 4 * nu) / (r**2))) * ((t**2) / (p)) - 2 #посмотреть
print("B1 = ", b1)
b2 = (e + anu) * ((nu * t**2) / (r * hr * p))
print("B2 = ", b2)
b3 = (e + anu) * ((l * t**2) / (2 * hr * hz * p))
print("B3 = ", b3)
b4 = (e + anu) * ((nu * t**2) / ((hz**2) * p))
print("B4 = ", b4)
d1 = (e + anu) * (((l + 2 * nu) * t**2) / ((hz**2) * p))
print("D1 = ", d1)
d2 = (e + anu) * ((l * t**2) / (2 * r * hz * p)) #посмотреть
print("D2 = ", d2)
d3 = (e + anu) * ((nu * t**2) / (2 * r * hz * p))
print("D3 = ", d3)