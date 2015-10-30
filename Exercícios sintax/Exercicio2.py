print ('Tempo de download')
tamanho = float (input('Digite o tamanho do arquivo a ser baixado, em MB: '))
velocidade = float(input('Digite a velocidade da Internetem kbps: '))
tempo = (tamanho*8*2**10)/velocidade
segundos = tempo % 60
minutos = tempo // 60
horas = minutos // 60
minutos = minutos % 60
print ('O tempo de download será: %s:%s:%s' %(str(round(horas)), str(round(minutos)), str(round(segundos))))