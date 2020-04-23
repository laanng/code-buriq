def rekursif(str,val):
    if val>len(str):
        print('Index melebihi string')
    else:
        listData=[]
        for i in range(len(str)):
            if str[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                listData.append(str[i])
        print(listData[val])
rekursif(input('\nMasukkan Kalimat : '),int(input('Masukkan Index ke : ')))