'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. 
A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.
Entrada
Quatro números inteiros representando a hora de início e fim do jogo.
Saída
Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
'''

hora_inicial = int(input("informe a hora que iniciou o jogo: "))
minuto_inicial = int(input("informe os minutos que iniciou o jogo: "))

hora_final = int(input("informe a hora que terminou o jogo: "))
minuto_final = int(input("informe os minutos que terminou o jogo: "))

res = hora_final-hora_inicial
if res < 0:
    res_hora = res*(-1)
else:
    res_hora = res


# se o segundo for maior do que o primeiro
res_min = minuto_final-minuto_inicial
if res_min < 0:
    res_hora-=1
    res_min = 60-(res_min*(-1))

# caso o horário final seja maior
if hora_final < hora_inicial:
    res_hora+=22

if hora_inicial == hora_final and minuto_inicial == minuto_final:
    res_hora=24
    res_min=0


print(f"O jogo durou {res_hora} horas e {res_min} minutos")