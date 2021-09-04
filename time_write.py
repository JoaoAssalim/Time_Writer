import time
import random

#palavras para escrever
frases = ['python a melhor linguagem','desistir nao eh um caminho','tudo tem uma solucao',
'nao de desculpas e sim solucoes']

#interface
print('-'*40)
print('Teste de Velocidade na Escrita'.center(40))
print('-'*40)
print()
#escolhendo frase
frase_escolhida = random.choice(frases)
print(f'Escreva a seguinte frase:\n{frase_escolhida.center(40)}')
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print()
#contagem de segundos para escrever
start_time = time.time()
vel_write = input(' - ').lower()
end = time.time()
finish = end - start_time
#quantas letras por segundo foram escritas
qnt_letter = len(frase_escolhida)
temp_letter = qnt_letter / finish

print(f'A sua media de velocidade é de {finish:.2f}seg e uma media de {temp_letter:.2f} letras por segundo')