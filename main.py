velocidade = int(input('Qual a velocidade atual?: '))

velocidade_max = 80
if velocidade <= velocidade_max:
    print('Não levou multa.')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
    print('Levou multa leve!')
elif velocidade > velocidade_max +11 and velocidade <= velocidade_max + 20:
    print('Levou multa grave!')
elif velocidade >= velocidade_max + 20:
    print('Levou multa gravissima!!!')
else:
    print('Ultilize valores validos...')