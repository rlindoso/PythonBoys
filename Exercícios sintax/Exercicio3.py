print ('exercício 3')

x = '-1'

while ( int(x) > 999 ) or ( int(x) < 0 ):
    x = input ('Digite um número entre 0 e 1000: ')
    try:
        y = int (x)
    except:
        print ('número incorreto')
        x = '-1'

if len(x) == 3 :
    print ('centena %s dezena %s e unidade %s'%(x[0], x [1], x [2]))
elif len(x) == 2 :
    print ('dezena %s e unidade %s'%(x[0], x [1]))
else:
    print ('unidade %s'%(x[0]))