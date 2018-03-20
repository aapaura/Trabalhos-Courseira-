# entrada: numéro inteiro (n)
# saída: fatorial deste número (n!)

# entra com o numero
num = int(input("Digite o valor de n:"))

# indice i e variaveis
i = 0
fatorial = 1
n = num

# loop
while i < num: 
    fatorial *= n 
    n -= 1 
    i += 1 

print(fatorial)
