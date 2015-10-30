print('exercicio 5')

num = int(input('\ndigite seu numero no sorteio: '))

from random import randint

sorte = randint(1,100)
if sorte < num:
    print('numero sorteado menor que seu numero')
elif sorte > num:
    print('numero sorteado maior que seu numero')
else:
    print('voce foi sorteado!')

print('\n \n************* \n \n')
print(sorte)
print(num)
