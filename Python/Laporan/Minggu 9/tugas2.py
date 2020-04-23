def fungsimat(x):
    if (x>10 or x<-10):
        print('\nMaaf range input tidak memenuhi syarat')
    else:
        y=6*(x*x)+3*x+2
        print(f'\nx = {x}')
        print(f'y = 6({x})^2 + 3({x}) + 2 = {y}')
fungsimat(int(input('\nMasukkan Angka : ')))
