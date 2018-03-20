# Este programa procura em um número, se existem dois algarismos adjacentes que sejam iguais
# ex: 12334 (repete o numero 3 duas vezes seguidas)


#  entrando com n número - lido como strings
num = input("Digite um número inteiro:")

#   Lendo a quantidade de digitos das strings
digitos = len(num)

#   Transformando as strings em numeros inteiros
num = int(num)
digitos = int(digitos)

# condição boolean 
digitoRepetido = False

#   Começando a verificação dos dígitos
# verificando digito a digito enquanto não se acha um digito repetido
while digitos > 0 and not digitoRepetido:
    primeiroDigito = num % 10 # separando último digito do numero
    num = num // 10  # dividindo o digito por 10 para pegar o penultimo digito (que será o novo ultimo)
    segundoDigito = num % 10 # separando o penultimo digito (agora, novo último)
    if primeiroDigito == segundoDigito: # comparando último com penultimo, se forem iguais, digitoRepetido recebe true (final do loop)
        digitoRepetido = True 
    else:  # se os digitos foram diferentes, digito recebe digito menos 1, volta para o loop com novo num (que foi dividido por 10)
        digitoRepertido = False 
    digitos = digitos - 1
    
#   Final do while; impressão dos resultados após término do loop
if digitoRepetido:
    print("Este número tem digitos adjacentes iguais")
else:
    print("Este número não tem dígitos adjacentes iguais")
    

 
