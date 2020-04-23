with open("kalimat.txt",'r') as f:
    val=[]
    for l in f:
        val.append(l)
    for l in range(len(val)):
        if l != (len(val)-1):
            val[l]=val[l][:-1]
    for l in range(len(val)):
       val[l]=val[l].split(' ')

with open("daftar_teks.txt","w") as g:
    for l in range(len(val)):
        g.write(f'\nBaris ke-{l+1}\n')
        for m in range(len(val[l])):
            g.write(f'{val[l][m]} : Urutan ke-{m+1}\n')