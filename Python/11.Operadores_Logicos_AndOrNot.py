#Operadores logicos :
#and (e), or (ou), not (não)
"""
And - Todas as condicoes precisam ser verdadeiras.

Se qualquer valor for considerad falso, a expressao é 
interrrompida e retorna o valor (Falso)

São considerados falsy : 0 , 0.0 , '' , False

None representa o não valor

"""
entrar = input('[E]ntrar [S]air: ')
senha_digitada = input ('Senha: ')

senha_permitida = '1234'

if entrar == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')
    