def fungsimat(x):
    if (x > 10 or x < -10):
        print('\nMaaf range input tidak memenuhi syarat')
    else:
        y=6*(x*x)+3*x+2
        print(f'\nX = {x}')
        print(f'y= 6({x})^2 + 3({x}) + 2 = {y}')
val=input('\nMasukkan Angka : ')
assert val.isdigit(), "Masukkan harus berupa Angka"
fungsimat(int(val))