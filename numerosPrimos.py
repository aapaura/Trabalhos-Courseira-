# programa imprime numero primo

# numero primo: unm numero p pertencente aos inteiros, é chamado de primo se:
# i) p diferente de zero; ii) p diferente de (+/-)1 e; iii) os únicos divisores
# de p são 1, -1, p e -p

# entrando com um numero inteiro

num = int(input("Digite um número inteiro:"))

# indices e variaveis

i = 2
numeroPrimo = True

# loop de verificação
# todo numero não primo (p), é fatorável em numeros primos (f)
# seja p primo e p | ab, então p | a ou p| b
# e isso acontece tal que ou a ou b sejam algum primo entre 2 e 7, visto que
# utilizamos alfabeto numerico de base 10

# testando divisores i < 10 ou menores que o próprio número
# enquanto não achar um divisor, esse numero é primo
# se achar divisor, o numero não é primo
# testando pelo num mod i --> resto da divisão de num por i

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
    
