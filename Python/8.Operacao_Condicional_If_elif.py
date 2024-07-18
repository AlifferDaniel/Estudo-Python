# if / elif      / else
# se / se não se / se não
'''
Usado para executar um determinado codigo, após uma análise bool 
'''

entrada = input('Você quer entrar ou sair?: ')

if entrada == 'entrar':
    print('Você entrou no sistema')

elif entrada == 'sair':
    print('Você saiu do sistema')

else:
    print('Você não digitou nem entrar e nem sair')

# else não funciona sozinho 

'''
Abaixo vemos que após um dos termo ser satisfeito ele termina o trecho de 
código, não rodando os restante de 'elif' dentro do código
'''
condicao1 = False
condicao2 = True
condicao3 = True

if condicao1:
    print('condicao 1 é verdadeira')

elif condicao2: 
    print('condicao 2 é verdadeira')

elif condicao3:
    print('condicao 3 é verdadeira')

else:
    print('nenhuma condicao é verdadeira')