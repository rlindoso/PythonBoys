print ('exercício 4 \n')

valid = False

while not valid:
    try:
        qtdDados = int(input ('Digite a quantidade de pessoas \na serem ordenadas por idade: '))
        if qtdDados > 0:
            valid = True
        else:
            print ('quantidade deve ser positiva')
    except:
        print ( ' número incorreto ' )

array=[[0 for j in range(2)] for i in range(qtdDados)]

for i in range(qtdDados):
    nome = input ('Digite %uº nome: '%(i+1))
    valid = False
    while not valid:
        try:
            idade = int (input ('Digite a %uº idade: ' %(i+1)))
            if idade > 0:
                valid = True
            else:
                print ('idade deve ser positiva')    
        except:
            print ( ' número incorreto ' )
    array[i] = [nome, idade]

for i in range (qtdDados): 
    for j in range (qtdDados - i):
        if array[j+i][1] > array[i][1] :
            aux = array[i]
            array[i] = array[j+i]
            array[j+i] = aux

print('\n\n******************\n\n')

for i in range(qtdDados):
    print('Nome %s, idade %s.'%(array[i][0], str(array[i][1])))
