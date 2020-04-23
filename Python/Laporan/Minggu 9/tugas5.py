def rekursif(a,b):
    nilai=0
    if (a%2!=0):
        a=a+1
    elif (b%2!=0):
        b=b+1
    val=int(b/a)
    for i in range(val+1):
        nilai+=a+2
    print(f'\nJumlah bilangan Genap : {nilai}')
rekursif(int(input('\nMasukkan Angka Batas Awal : ')),int(input('Masukkan Angka Batas Akhir : ')))