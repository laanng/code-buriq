def pisah(value):
    dataList=['','','']
    for i in range(len(value)):
        if value[i] in '0123456789':
            dataList[1]=f'{dataList[1]}{value[i]}'
        elif value[i] in 'abcdefghijklmnopqrstuvwxyz':
            dataList[0]=f'{dataList[0]}{value[i]}'
        else:
            dataList[2]=f'{dataList[2]}{value[i]}'
    print(dataList)
pisah(input('\nMasukkan : '))
