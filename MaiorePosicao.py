'''Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.
Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''
import random 
lista= []
maior = 0
cont=0
for i in range(10):
    num = random.randint(1,200)
    lista.append(num)
print(lista)    
for c in lista :
   
    if c > maior :
        maior = c
        index = lista.index(c)
        
print(maior) 
print(index)   
    





