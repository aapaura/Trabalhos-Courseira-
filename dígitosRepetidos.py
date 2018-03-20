# achar dois numeros adjacentes iguais
# 12334
#   entrando com os dados numericos lidos como strings
num = input("Digite um número inteiro:")
#   Lendo a quantidade de digitos das strings
digitos = len(num)

#   Transformando as strings em numeros inteiros
num = int(num)
digitos = int(digitos)

digitoRepetido = False

#   Começando a verificação dos dígitos
while digitos > 0 and not digitoRepetido:
    primeiroDigito = num % 10
    num = num // 10
    segundoDigito = num % 10
    if primeiroDigito == segundoDigito:
        digitoRepetido = True
    else:
        digitoRepertido = False
    digitos = digitos - 1
    
#   Final do while; impressão dos resultados    
if digitoRepetido:
    print("Este número tem digitos adjacentes iguais")
else:
    print("Este número não tem dígitos adjacentes iguais")
    

 
