# Input berapa banyak jenis gorengan yang dibeli
banyak_jenis = int(input('Berapa banyak jenis gorengan: '))

# Variabel untuk menyimpan total harga keseluruhan
total_semua = 0

# Loop untuk setiap jenis gorengan
for i in range(banyak_jenis):
    print(f'\nGorengan ke-{i+1}')
    # Input kode gorengan
    kode = input('Masukan kode (B/T/H): ')
    
    # Tentukan nama dan harga berdasarkan kode
    if kode == 'B':
        nama = 'Bakwan'
        harga = 1000
    elif kode == 'T':
        nama = 'Tahu isi'
        harga = 1500
    elif kode == 'H':
        nama = 'Hati ayam'
        harga = 2000
    
    # Input jumlah pembelian
    jumlah = int(input('Masukan jumlah: '))
    # Hitung total untuk item ini
    total = harga * jumlah
    
    # Tampilkan detail pembelian
    print(f'Nama: {nama}, Harga: Rp {harga}, Jumlah: {jumlah}, Total: Rp {total}')
    
    # Tambahkan ke total keseluruhan
    total_semua = total_semua + total

# Tampilkan ringkasan
print("\n" + "="*50)
print('GEROBAK GORENGAN')
print("="*50)
print(f'Total Pembelian: Rp {total_semua}')
print("TERIMA KASIH TELAH BELANJA DI GEROBAK GORENGAN")