import math

x1 = int(input("Entre com a coordenada x do primeiro número"))
y1 = int(input("Entre com a coordenada y do primeiro número"))
x2 = int(input("Entre com a coordenada x do segundo número"))
y2 = int(input("Entre com a coordenada y do segundo número"))

d = math.sqrt((( x1 - x2) ** 2)+((y1 - y2)**2))

if d >= 10:
    print("longe")
else:
    print("perto")


