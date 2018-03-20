# este programa calcula as raízes de uma equação de segundo grau por baskara.

# importando pacote math
import math

# entrando com valores de a, b e c
a = float(input("Digite o valor de a:"))
b = float(input("Digite o valor de b:"))
c = float(input("Digite o valor de c:"))

# calculando Delta
delta = b ** 2 - 4 * a * c

# Se delta maior ou igual a zero 
if delta >= 0:
     x1 = (-b + math.sqrt(delta)) / (2 * a) #calculo raiz 1
     x2 = (-b - math.sqrt(delta)) / (2 * a) #calculo raiz 2
     if delta == 0: # se delta igual a zero
         print("a raiz desta equação é", x1) #só existe uma raiz (ou duas iguais), no caso, imprime a raiz 1
     else:
          if x1<x2:   #colocando em ordem crescente a saída do resultado: valores das raizes em ordem crescente
               print("as raízes da equação são", x1, "e", x2)
          else:
               print("as raízes da equação são", x2, "e", x1)
else: # se Delta for menor que zero, imprime que não existem raízes reais
    print("esta equação não possui raízes reais")



    
    
