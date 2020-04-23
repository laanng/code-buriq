def prima(value):
    nilai=value
    if (nilai%2 != 0 and nilai%3 != 0):
        print(f'{nilai} adalah Bilangan Prima')
    else:
        print(f'{nilai} adalah Bukan Bilangan Prima')
val=input('\nMasukkan Angka : ')
assert val.isdigit(), "Masukkan harus berupa Angka"
prima(int(val))