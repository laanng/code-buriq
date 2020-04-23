def faktorial(nilai):
    hasil=1
    for i in range(nilai):
        print(f'{nilai-i}', end='')
        hasil+=hasil*(nilai-i)
        if i == nilai-1:
            print(f' = {hasil}')
        else:
            print(end=' x ')
val=input('\nMasukkan Angka : ')
assert val.isdigit(), "Masukkan harus berupa Angka"
faktorial(int(val))