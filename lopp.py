# Sistem Manajemen Baju Sederhana

# Database baju dengan merek dan harga
daftar_baju = {
    1: {"merek": "Nike", "harga": 350000, "ukuran": ["S", "M", "L", "XL"]},
    2: {"merek": "Adidas", "harga": 400000, "ukuran": ["S", "M", "L", "XL"]},
    3: {"merek": "Puma", "harga": 300000, "ukuran": ["S", "M", "L"]},
    4: {"merek": "Uniqlo", "harga": 250000, "ukuran": ["S", "M", "L", "XL", "XXL"]},
    5: {"merek": "H&M", "harga": 200000, "ukuran": ["S", "M", "L"]},
}

def tampilkan_menu():
    print("\n" + "="*50)
    print("SISTEM KATALOG BAJU".center(50))
    print("="*50)
    print("1. Lihat Semua Katalog Baju")
    print("2. Cari Baju Berdasarkan Merek")
    print("3. Cari Baju Berdasarkan Budget")
    print("4. Tambah Baju Baru")
    print("5. Keluar")
    print("="*50)

def lihat_katalog():
    print("\n" + "="*50)
    print("KATALOG BAJU".center(50))
    print("="*50)
    for id, data in daftar_baju.items():
        print(f"ID: {id}")
        print(f"  Merek   : {data['merek']}")
        print(f"  Harga   : Rp {data['harga']:,}")
        print(f"  Ukuran  : {', '.join(data['ukuran'])}")
        print("-" * 50)

def cari_berdasarkan_merek():
    merek = input("\nMasukkan nama merek yang dicari: ").strip()
    ditemukan = False
    
    print("\n" + "="*50)
    print(f"HASIL PENCARIAN: {merek}".center(50))
    print("="*50)
    
    for id, data in daftar_baju.items():
        if data['merek'].lower() == merek.lower():
            print(f"ID: {id}")
            print(f"  Merek   : {data['merek']}")
            print(f"  Harga   : Rp {data['harga']:,}")
            print(f"  Ukuran  : {', '.join(data['ukuran'])}")
            ditemukan = True
            break
    
    if not ditemukan:
        print(f"Baju dengan merek '{merek}' tidak ditemukan!")

def cari_berdasarkan_budget():
    try:
        budget = int(input("\nMasukkan budget maksimal (Rp): "))
        ditemukan = False
        
        print("\n" + "="*50)
        print(f"BAJU DALAM BUDGET Rp {budget:,}".center(50))
        print("="*50)
        
        for id, data in daftar_baju.items():
            if data['harga'] <= budget:
                print(f"ID: {id}")
                print(f"  Merek   : {data['merek']}")
                print(f"  Harga   : Rp {data['harga']:,}")
                print(f"  Ukuran  : {', '.join(data['ukuran'])}")
                print("-" * 50)
                ditemukan = True
        
        if not ditemukan:
            print(f"Tidak ada baju dalam budget Rp {budget:,}")
    except ValueError:
        print("Input tidak valid! Masukkan angka.")

def tambah_baju():
    print("\n" + "="*50)
    print("TAMBAH BAJU BARU".center(50))
    print("="*50)
    
    merek = input("Masukkan merek baju: ").strip()
    
    try:
        harga = int(input("Masukkan harga baju (Rp): "))
        ukuran_input = input("Masukkan ukuran (pisahkan dengan koma, contoh: S,M,L): ")
        ukuran = [u.strip().upper() for u in ukuran_input.split(",")]
        
        # Dapatkan ID baru
        id_baru = max(daftar_baju.keys()) + 1
        
        # Tambahkan ke database
        daftar_baju[id_baru] = {
            "merek": merek,
            "harga": harga,
            "ukuran": ukuran
        }
        
        print(f"\n✓ Baju '{merek}' berhasil ditambahkan dengan ID: {id_baru}")
    except ValueError:
        print("Input tidak valid! Harga harus berupa angka.")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-5): ").strip()
        
        if pilihan == "1":
            lihat_katalog()
        elif pilihan == "2":
            cari_berdasarkan_merek()
        elif pilihan == "3":
            cari_berdasarkan_budget()
        elif pilihan == "4":
            tambah_baju()
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan sistem katalog baju!")
            print("Sampai jumpa! 👋")
            break
        else:
            print("\n❌ Pilihan tidak valid! Silakan pilih 1-5.")
        
        input("\nTekan Enter untuk melanjutkan...")

# Jalankan program
if __name__ == "__main__":
    main()