# Program Kasir GEROBAK FRIED CHICKEN - Versi Sederhana

print("="*50)
print("GEROBAK FRIED CHICKEN".center(50))
print("="*50)

# Tampilkan daftar harga
print("\nKode  Jenis Potong  Harga")
print("-" * 50)
print("D     Dada          Rp. 2500")
print("P     Paha          Rp. 2000")
print("S     Sayap         Rp. 1500")
print("-" * 50)

# Input banyak jenis
banyak_jenis = int(input("\nBanyak Jenis : "))

# Variabel untuk menyimpan data
jenis_list = []
banyak_list = []
harga_list = []
jumlah_list = []

# Loop untuk input data
for i in range(banyak_jenis):
    print(f"\nJenis Ke - {i + 1}")
    kode = input("Kode Potong [D/P/S] : ").upper()
    banyak = int(input("Banyak Potong : "))
    
    # Tentukan jenis dan harga berdasarkan kode
    if kode == "D":
        jenis = "Dada"
        harga = 2500
    elif kode == "P":
        jenis = "Paha"
        harga = 2000
    elif kode == "S":
        jenis = "Sayap"
        harga = 1500
    
    # Hitung jumlah harga
    jumlah = harga * banyak
    
    # Simpan ke list
    jenis_list.append(jenis)
    banyak_list.append(banyak)
    harga_list.append(harga)
    jumlah_list.append(jumlah)

# Tampilkan struk
print("\n" + "="*50)
print("GEROBAK FRIED CHICKEN".center(50))
print("="*50)
print(f"{'No':<4} {'Jenis':<12} {'Harga':<12} {'Banyak':<8} {'Jumlah'}")
print(f"{'':>4} {'Potong':<12} {'Satuan':<12} {'Beli':<8} {'Harga'}")
print("-" * 50)

# Loop untuk tampilkan detail pembelian
jumlah_bayar = 0
for i in range(banyak_jenis):
    print(f"{i+1:<4} {jenis_list[i]:<12} {harga_list[i]:<12} {banyak_list[i]:<8} Rp {jumlah_list[i]}")
    jumlah_bayar += jumlah_list[i]

# Hitung pajak dan total
print("-" * 50)
print(f"{'':<37} Jumlah Bayar  Rp {jumlah_bayar}")

pajak = jumlah_bayar * 10 / 100
print(f"{'':<37} Pajak 10%     Rp {int(pajak)}")

total_bayar = jumlah_bayar + pajak
print(f"{'':<37} Total Bayar   Rp {int(total_bayar)}")
print("="*50)
