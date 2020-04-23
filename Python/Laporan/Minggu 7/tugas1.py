print('..:: Program Membalik & Jumlah vokal di Kalimat ::..\n')
input_kalimat=input('Masukkan Kalimat : ')
value=-len(input_kalimat)
input_kalimatList=list(input_kalimat)
input_kalimatSplit=input_kalimat.split(' ')
val=-1
print('\nKalimat terbalik :',end=' ')
for i in range(len(input_kalimatSplit)):
    print(input_kalimatSplit[len(input_kalimatSplit)-(i+1)],end=' ')
print('\nKalimat dibalik :',end=' ')
while (val>=value):
    print(input_kalimat[val], end='')
    val-=1
vokal=['a','i','u','e','o']
jumlahVokal=0
print('\nJumlah huruf vokal :',end=' ')
for i in range(len(input_kalimatList)):
    if input_kalimatList[i] in vokal: jumlahVokal+=1
print(jumlahVokal)