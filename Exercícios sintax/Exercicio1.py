print('exercício 1 - dados de entrada')

nome = input('Escreva seu nome: ')
while (len(nome) < 4):
	print ('Nome muito curto')
	nome = input ('Escreva seu nome : ')

idade = int(input ('Digite sua idade: '))
while ((idade < 0) or (idade > 150)):
	print ('Idade incorreta')
	print ('Digite uma idade entre 0 e 150')
	idade = int (input('Digite sua idade: '))

salario = float(input ('Digite seu salário: '))
while (salario < 0):
	print ('salário incorreto - digite um salário maior que 0')
	salario = float(input ('Digite seu salário: '))

sexo = input('Sexo Macho (m) ou Fêmea(f): ')
while ((sexo.upper() != 'M') and (sexo.upper() != 'F')):
	print ('Não existe intermediário, só (f) ou (m)')
	sexo = input('Sexo Macho (m) ou Fêmea(f): ')

if (sexo.upper() == 'M'):
	sexo = ' macho'
else:
	sexo = 'a fêmea'

ecivil = input ('Digite seu estado civil (s, c, v, d): ')
while (ecivil.upper() not in ('S', 'C', 'V', 'D')):
	print ('Digite apenas s, c, v ou d')
	ecivil = input ('Digite seu estado civil (s, c, v, d): ')

if (ecivil.upper() == 'S'):
	ecivil = 'solteiro'
elif (ecivil.upper() == 'C'):
	ecivil = 'casado'
elif (ecivil.upper() == 'V'):
	ecivil = 'viúvo'
else:
	ecivil = 'divorciado'

print('A pessoa de nome ' + nome + ', de idade ' + str(idade) + ' é um' + sexo)
print('com salário em torno de ' + str(salario) +' reais e tem estado civil ' + ecivil)