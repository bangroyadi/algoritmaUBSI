kode=input('masukan kode gorengan (B,T,H)')
if kode=='B':
    nama='Bakwan'
    harga=1000
elif kode=='T':
    nama='Tahu isi'
    harga=1500
elif kode=='H':
    nama='Hati ayam'
    harga=2000
jumlah=int(input('masukan jumlah pembelian:'))
total=harga*jumlah
print('GEROBAK GORENGAN')
print('Nama Gorengan:',nama)
print('Harga Satuan: Rp',harga)
print('Jumlah Beli:',jumlah)
print('Total Harga: Rp',total)
print("-" * 50)
print("TERIMA KASIH TELAH BELANJA DI GEROBAK GORENGAN")