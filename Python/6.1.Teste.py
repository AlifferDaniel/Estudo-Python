nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

print('--' * 10)

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))

print('--' * 10)

nome = "Luiz"
idade = 23
formato = f'{nome} tem {idade:.2f} anos'
print(formato)

print('--' * 10)

'''Concatenacao entre srt e int não
ocorre 
'''
#print('teste'+ 2)

print(int('teste') + 2)