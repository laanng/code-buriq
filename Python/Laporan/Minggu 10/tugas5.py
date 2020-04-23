def rekursif(a,b):
    nilai=0
    if (a%2 != 0):
        a=a+1
    elif (b%2 != 0):
        b=b+1
    val=int(b/a)
    for i in range(val+1):
        nilai+=a+2
    print(f'\nJumlah bilangan Genap : {nilai}')
val1=input('\nMasukkan Angka batas awal : ')
assert val1.isdigit(), "Masukkan harus berupa Angka"
val2=input('Masukkan Angka batas akhir : ')
assert val2.isdigit(), "Masukkan harus berupa Angka"
rekursif(int(val1),int(val2))