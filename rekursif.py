
# Fungsi Pangkat secara Rekursif
# Fungsi yang memanggil dirinya sendiri

def pangkat(x,y):
    # Kondisi berhenti (base case) - jika pangkat 0, hasilnya selalu 1
    if y == 0:
        return 1
    # Jika pangkat belum 0, kalikan x dengan pangkat(x, y-1)
    else:
        return x * pangkat(x,y-1)

# Input bilangan pokok dari user
x = int(input("Masukan Nilai X : "))
# Input bilangan pangkat dari user
y = int(input("Masukan Nilai Y : "))
# Panggil fungsi pangkat dan tampilkan hasilnya
print("%d dipangkatkan %d = %d"% (x,y,pangkat(x,y)))
print('-'*20)
#pangkat tanpa rekursif
# Input bilangan pokok dari user
x = int(input("Masukan Nilai X : "))
# Input bilangan pangkat dari user
y = int(input("Masukan Nilai Y : "))

# Inisialisasi hasil dengan nilai 1 (nilai awal perkalian)
hasil = 1
# Loop sebanyak y kali untuk mengalikan x dengan x
for i in range(y):
    # Setiap iterasi, kalikan hasil dengan x
    hasil = hasil * x

# Tampilkan hasil akhir dengan format string
print("%d dipangkatkan %d = %d"% (x,y,hasil))
print('-'*20)

#faktorial secara rekursif
def faktorial(n):
    # Kondisi berhenti (base case) - faktorial dari 0 atau 1 adalah 1
    if n == 1:
        return (n)
    # Jika n lebih besar dari 1, kalikan n dengan faktorial(n-1)
    else:
        return (n * faktorial(n-1))
# Input bilangan dari user
num = int(input("Masukan Bilangan untuk Faktorial: "))
# Panggil fungsi faktorial dan tampilkan hasilnya
print("Faktorial dari %d adalah %d"%(num, faktorial(num)))
print('-'*20)

#faktorial tanpa rekursif
# Input bilangan dari user
num = int(input("Masukan Bilangan untuk Faktorial: "))
# Inisialisasi hasil faktorial dengan nilai 1   
hasil = 1
# Loop dari 1 hingga num untuk menghitung faktorial
for i in range(1, num + 1):
    # Kalikan hasil dengan i pada setiap iterasi
    hasil = hasil * i   
# Tampilkan hasil akhir faktorial dengan format string
print("Faktorial dari %d adalah %d"%(num, hasil))
print('-'*20)

# Fibonacci secara rekursif - menampilkan deret Fibonacci
def fibonacci_rekursif(n):
    # Kondisi berhenti (base case) - Fibonacci dari 0 adalah 0, dan dari 1 adalah 1
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Jika n lebih besar dari 1, jumlahkan dua nilai Fibonacci sebelumnya
    else:
        return fibonacci_rekursif(n-1) + fibonacci_rekursif(n-2)  

# Input jumlah bilangan Fibonacci dari user
n = int(input("Masukan Berapa Banyak Bilangan Fibonacci: "))
# Inisialisasi list untuk menyimpan deret Fibonacci
deret_fib_rekursif = []
# Loop untuk menghitung setiap bilangan Fibonacci
for i in range(n):
    # Tambahkan hasil fibonacci ke dalam list
    deret_fib_rekursif.append(fibonacci_rekursif(i))
# Tampilkan deret Fibonacci dengan format yang rapi
print("Deret Fibonacci (Rekursif):", deret_fib_rekursif)
print('-'*20)

# Fibonacci tanpa rekursif - menampilkan deret Fibonacci
# Input jumlah bilangan Fibonacci dari user
n = int(input("Masukan Berapa Banyak Bilangan Fibonacci: "))
# Inisialisasi list untuk menyimpan deret Fibonacci
deret_fib_loop = []
# Inisialisasi dua nilai awal Fibonacci
a, b = 0, 1
# Loop untuk menghitung Fibonacci sebanyak n kali
for i in range(n):
    # Tambahkan nilai a (Fibonacci saat ini) ke dalam list
    deret_fib_loop.append(a)
    # Hitung nilai Fibonacci berikutnya dengan menukar nilai a dan b
    a, b = b, a + b
# Tampilkan deret Fibonacci dengan format yang rapi
print("Deret Fibonacci (Loop):", deret_fib_loop)
print('-'*20)

#menara hanoi secara rekursif
def menara_hanoi(n, sumber, tujuan, bantu):
    # Jika hanya ada satu cakram, pindahkan langsung dari sumber ke tujuan
    if n == 1:
        print(f"Pindahkan cakram 1 dari {sumber} ke {tujuan}")
        return
    # Pindahkan n-1 cakram dari sumber ke bantu menggunakan tujuan sebagai penyangga
    menara_hanoi(n-1, sumber, bantu, tujuan)
    # Pindahkan cakram terbesar dari sumber ke tujuan
    print(f"Pindahkan cakram {n} dari {sumber} ke {tujuan}")
    # Pindahkan n-1 cakram dari bantu ke tujuan menggunakan sumber sebagai penyangga
    menara_hanoi(n-1, bantu, tujuan, sumber)
# Input jumlah cakram dari user
jumlah_cakram = int(input("Masukan Jumlah Cakram: "))
# Panggil fungsi menara_hanoi untuk memulai proses pemindahan cakram
menara_hanoi(jumlah_cakram, 'A', 'C', 'B')
print('-'*20)

#menara hanoi tanpa rekursif
# Input jumlah cakram dari user
jumlah_cakram = int(input("Masukan Jumlah Cakram: "))
# Hitung total langkah yang diperlukan (2^n - 1)
total_langkah = (2 ** jumlah_cakram) - 1
# Loop untuk setiap langkah dari 1 hingga total_langkah
for langkah in range(1, total_langkah + 1):
    # Tentukan sumber, tujuan, dan penyangga berdasarkan langkah saat ini
    sumber = (langkah & langkah - 1) % 3
    tujuan = ((langkah | langkah - 1) + 1) % 3
    # Peta indeks ke nama tiang
    tiang = ['A', 'B', 'C']
    # Tampilkan langkah pemindahan cakram
    print(f"Pindahkan cakram dari {tiang[sumber]} ke {tiang[tujuan]}")
print('-'*20)