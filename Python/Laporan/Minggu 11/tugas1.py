with open("file_baru.txt",'r') as f:
    val=[]
    for l in f:
        val.append(l)
    for l in range(len(val)):
        if l != (len(val)-1):
            val[l]=val[l][:-1]
    
    with open("file_baru.txt","w") as g:
        for l in range(len(val)):
            g.write(f'{val[l]} ')