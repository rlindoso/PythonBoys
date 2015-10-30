print('**** IMPRENSADINHO ****\n')

valid = False

from random import randint
menor = 0;
maior = 100;
sorte = randint(menor+1,maior-1)

while not valid:
    try:
        qtdPessoas = int(input ('Digite o quantidade de pessoas \nque participarão do jogo: '))
        if qtdPessoas > 0:
            valid = True
        else:
            print ('quantidade deve ser positiva')
    except:
        print ( ' número incorreto ' )

array=[[0 for j in range(2)] for i in range(qtdPessoas)]

for i in range(qtdPessoas):
    nome = input ('Digite nome do %uº jogador: '%(i+1))
    array[i] = [nome, 1]

num = 0;
idPessoa = 0;
while (num < sorte) or (num > sorte):   
    valid = False

    print('está na vez de ' + array[idPessoa][0])
    
    while not valid:
        try:
            num = int (input ('Digite a um número entre %u e %u: ' %(menor, maior)))
            if (num <= maior) and (num >= menor) and (num != menor) and (num != maior):
                valid = True
                if num < sorte:
                    print('Número menor que o sorteado')
                    menor = num
                elif num > sorte:
                    print('Número maior que o sorteado')
                    maior = num
                else:
                    print('Acertou!\nO vencedor é %s com %u tentativas.' %(array[idPessoa][0], array[idPessoa][1]))
                    maior = num

                array[idPessoa][1] = array[idPessoa][1] + 1    
                if idPessoa == qtdPessoas - 1:
                    idPessoa = -1;
                    
                idPessoa = idPessoa + 1
            else:
                print ('Número deve estar entre %u e %u.' %(menor, maior))    
        except:
            print ( ' número incorreto ' )


