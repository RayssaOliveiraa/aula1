'''Faça uma função chamada calculaSalario que recebe como parâmetro o valor do salário bruto
 calcula o salário líquido. O salário líquido é calculado a partir do salário bruto, primeiro
 descontando 11% referente ao INSS, e do resultado, descontando-se 15% de imposto de renda (IR).


Exemplo
Salário Bruto = R$ 5000,00
Desconto do INSS = R$ 550,00 (11% de R$ 5000,00)
Desconto do IR = R$ 667,50 (15% de R$ 4450,00)
Salário Líquido = 5000 - (550 + 667,50) = 3782,50'''


def calculaSalario(salarioBruto):
    inss = salarioBruto * 0.11
    ir = (salarioBruto- inss)*0.15
    salarioLiquido = ( salarioBruto - (inss+ir))
    return salarioLiquido

print(calculaSalario(5000.00))    
