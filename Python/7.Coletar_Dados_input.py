#Não funciona no Output
'''
Com necessidade de interacao com o usuario, serve para pedir e em seguida 
armazenar o dado fornecido  
'''
print('-' * 10, 'SEM COESAO','-' * 10)
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma dos doisnumeros é: {numero_1 + numero_2}')
'''
Esse dado é armazenadi como uma str, para operacoes aritimeticas com o 
dado é necessario a coersao do dado
'''
#1- forma de coercao, mas não tao util pois pode gerar quebra no inicio 
#do programa

print('-' * 10, 'COM 10COESAO','-' * 10)

numero_4 = int(input('Digite um número: '))
numero_5 = int(input('Digite outro número: '))

print(f'A soma dos doisnumeros é: {numero_4 + numero_5}')


 