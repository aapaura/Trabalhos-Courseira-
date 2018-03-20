# programa imprime numero primo

# numero primo: unm numero p pertencente aos inteiros, é chamado de primo se:
# i) p diferente de zero; ii) p diferente de (+/-)1 e; iii) os únicos divisores
# de p são 1, -1, p e -p

# entrando com um numero inteiro
num = int(input("Digite um número inteiro:"))

# indices e variaveis
i = 2
numeroPrimo = True

# OBS:
# todo numero não primo, é fatorável em numeros primo
# seja p primo e p | ab, então p | a ou p| b

# Loop de Verificação vai testar todos os  possíveis divisores i < 10 ou menores que o próprio número (no caso dele ser menor que 10)
# enquanto não achar um divisor, esse numero é primo
# se achar divisor, o numero não é primo
# testando por num módulo i --> resto da divisão de num por i

# loop
while i < 10 and i < num and numeroPrimo: 
    mod = num % i
    if mod == 0:
        numeroPrimo = False
    else:
        numeroPrimo = True
    i += 1

if numeroPrimo:
    print("primo")
else:
    print("não primo")
    
