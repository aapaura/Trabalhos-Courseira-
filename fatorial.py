# entra com o numero
num = int(input("Digite o valor de n:")) #5

# indice i e variaveis
i = 0
fatorial = 1
n = num

# loop
while i < num: # 0 <  5 -- 1< 5 -- 2<5 -- 3<5 -- 4<5 -- 5<5 FALSE
    fatorial *= n #1*5=5 -- 5*4=20 -- 20*3=60 -- 60*2=120 -- 120*1=120
    n -= 1 #4 -- 3 -- 2 -- 1 -- 0
    i += 1 #1 -- 2 -- 3 -- 4 -- 5

print(fatorial)
