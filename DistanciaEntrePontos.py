

#>>>>>>  MEDINDO A DISTÂNCIA ENTRE DOIS PONTOS NO PLANO CARTESIANO  <<<<<<#

#importando pacote math - funções matematicas

import math

#entrando com as coordenadas x e y dos pontos
x1 = int(input("Entre com a coordenada x do primeiro número"))
y1 = int(input("Entre com a coordenada y do primeiro número"))
x2 = int(input("Entre com a coordenada x do segundo número"))
y2 = int(input("Entre com a coordenada y do segundo número"))

# calculo da distância entre dois pontos
d = math.sqrt((( x1 - x2) ** 2)+((y1 - y2)**2))

# condições: 
if d >= 10:  # se a distância for maior que dez, imprime que os pontos estão longe
    print("longe")
else:  # se for menor que 10, imprime que estão perto
    print("perto")


