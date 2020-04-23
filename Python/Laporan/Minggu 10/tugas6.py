def rekursif(str,val):
    if val > len(str):
        print('Index melebihi string')
    else:
        listData=[]
        for i in range(len(str)):
            if str[i] in 'abcdefghijklmnopqrstuvwxyz':
                listData.append(str[i])
        print(listData[val])
val1=input('\nMasukkan Kata : ')
assert val1.isalpha(), "Masukkan harus berupa kata"
val2=input('Masukkan Angka batas akhir : ')
assert val2.isdigit(), "Masukkan harus berupa Angka"
rekursif(val1, int(val2))