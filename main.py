#input bilangan
'''
bilangan = int(input("Masukkan Bilangan : "))
#bilangan prima harus lebih besar dari 1
if bilangan > 1:
    for i in range(2,bilangan):
        if (bilangan % i) == 0:
            print(bilangan, "bukan bilangan prima")
            print(i, "kali", bilangan//i, "=", bilangan)
            break
    else:
        print(bilangan,"adalah bilangan prima")
else:
    print(bilangan, "bukan bilangan prima")
'''
#Fungsi Pangkat secara Rekursif
def pangkat(x,y):
    if y == 0:
        return 1
    else:
        return x * pangkat(x,y-1)
x = int(input("Masukan Nilai X : "))
y = int(input("Masukan Nilai Y : "))
print("%d dipangkatkan %d = %d"% (x,y,pangkat(x,y)))