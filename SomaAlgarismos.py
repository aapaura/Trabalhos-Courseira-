# programa para somar digitos de um número
# 1234 retorna 1+2+3+4 = 10

print("Este programa irá somar todos os digítos do número indicado")

num = input("Digite um número inteiro:")
digitos = len(num)
num = int(num)
digitos = int(digitos)

i = 0
soma = 0

while i < digitos:
    y = num % 10
    soma = soma + y
    num = num // 10
    i = i + 1

print(soma)








    
    
    


