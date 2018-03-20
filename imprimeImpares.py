# Verifica se um número é ímpar (ou se é par)
# entrando com o valor de n
n = int(input("Digite o valor de n:"))

# indices e variaveis
num = n

# loop
while num > 0: # enquanto num for maior que zero
    n = num % 2  # n recebe num modulo 2 (resto da divisao de num por 2)
    if n != 0:  # se n for diferente de 0 (ou seja, se num for ímpar)
        print(num, "é um número ímpar") # imprime num
    else: 
        print(num, "é um número par")
    num -= 1  # num recebe num - 1 ---> loop
        
        
