import time

#interface
print('-'*40)
print('Teste de Velocidade na Escrita'.center(40))
print('-'*40)
print()

print('Escreva a frase de desejar!')
time.sleep(0.5)
print(f'Aperte "Enter" para finalizar!')
print('3...')
time.sleep(1)
print('2...')
time.sleep(1)
print('1...')
time.sleep(1)
print()
#contagem de segundos para escrever
start_time = time.time()
vel_write = input(' - ')
end = time.time()
finish = end - start_time
#quantas letras por segundo foram escritas
qnt_letter = len(vel_write)
temp_letter = qnt_letter / finish

print(f'A sua media de velocidade é de {finish:.2f}seg e uma media de {temp_letter:.2f} letras por segundo')
