'''Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.
Entrada
A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.
Saída
A saída contém um valor correspondente à média de idade dos indivíduos.

'''
lista=[]
soma=0
num= int(input('Informe uma idade : ' ))


while num > 0 :
    if num > 0 :    
        lista.append(num)
        soma+=num  
        num= int(input('Informe uma idade : ' ))
       
media =soma/len(lista)
print(f" A quantidade de idades informadas foram {len(lista)}, a soma das idades é {soma}, e media das idades é {media} ")
