fwrite = open("file_baru.txt","w")
fwrite.write("Hallo, Baris pertama file yang saya buat\n")
fwrite.write("Ini baris ke-2\n")
fwrite.close()

with open("file_baru2.txt","w") as f:
    f.write("Hi, ini file yang lain\n")
    f.write("Tapi menggunakan cara yang berbeda\n")
    f.write("Kira2 apa ya bedanya\n")

with open("file_baru.txt","r") as f:
    counter = 0
    for l in f:
        counter+=1
        print(f"{counter}: {l}", end='')
    print(f'Jumlah baris dari file {f.name} adalah {counter}')

with open("Latihan/Minggu 11/latihan1.py", "r") as f:
    counter = 1
    for l in f:
        print(f'{counter}: {l}',end='')
        counter+=1