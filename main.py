cont=0
for i in range(1,6):
    nun1 = int(input(f"Informe um numero {i} inteiro: "))
    if nun1 % 2 == 0:
        cont+=1
print(f"Você digitou {cont}, numeros pares")       
