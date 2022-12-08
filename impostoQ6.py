''' Faça um programa que use a função valorPagamento para determinar o valor a 
ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário 
o valor da prestação e o número de dias em atraso e passar estes valores para a função 
valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa 
que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução
o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja
informado um valor igual a zero para a prestação. Neste momento o programa deverá ser 
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações
pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso,
cobrar o valor da prestação. 
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.'''


def valorPagamento (valorPrestacao, diasAtraso):

    if diasAtraso == 0:
        valoraPagar = valorPrestacao
    elif diasAtraso< 0 :
        print(" dias de atraso invalido")    
    else:
        multa = valorPrestacao * 0.03
        juros = (valorPrestacao * 0.001)* diasAtraso
        valoraPagar = valorPrestacao + (multa+juros)    

    return valoraPagar


contador = 0
somador =0

ValorPrestacao = 1

while ValorPrestacao != 0:

    ValorPrestacao = float(input("Informe o valor da prestação a ser pago  : "))  

    if ValorPrestacao == 0 :
        break  
        print (" Obrigada (o) por usar nosso programa.")

    diasAtraso = int(input("Informe a quantidade de dias em atraso: "))  


    if diasAtraso < 0  or ValorPrestacao < 0 :
        print ("Valor de dias invalido ou Valor da prestação invalido.")
    else :
        valoraPagar = valorPagamento(ValorPrestacao,diasAtraso)   
        somador += ValorPrestacao
        contador +=1
        valorTotal = valorPagamento(ValorPrestacao,diasAtraso)
        print(" ")
        print(f" O valor total a ser pago é R$ {valorTotal}")    

print(50*"-")  
print("               Relatório            ")     
print(50*"-")  
print(f" A quantidade de valores informado foi:  {contador} ")
print(f" A  soma dos valores informado foi:  {somador } ")
print(" ------------------FIM--------------------------")


    
    