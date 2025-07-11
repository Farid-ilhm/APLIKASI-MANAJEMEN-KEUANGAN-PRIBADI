from file_manager import save_data

def tambah_transaksi(transactions):
    tanggal = input("Tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (pemasukan/pengeluaran): ").lower()
    kategori = input("Kategori: ")
    jumlah = input("Jumlah: ")

    transaksi = {
        'tanggal': tanggal,
        'jenis': jenis,
        'kategori': kategori,
        'jumlah': jumlah
    }
    transactions.append(transaksi)
    save_data(transactions)
    print("✅ - Transaksi berhasil ditambahkan.")

def tampilkan_transaksi_filter(transactions):
    if not transactions:
        print("Belum ada transaksi.")
        return

    print("\nFilter Transaksi:")
    print("1. Tampilkan Semua")
    print("2. Bulanan (misal: 2025-07)")
    print("3. Tahunan (misal: 2025)")
    pilihan = input("Pilih (1-3): ")

    if pilihan == '1':
        hasil = transactions

    elif pilihan == '2':
        bulan = input("Masukkan bulan dan tahun (YYYY-MM): ")
        hasil = [tr for tr in transactions if tr['tanggal'].startswith(bulan)]

    elif pilihan == '3':
        tahun = input("Masukkan tahun (YYYY): ")
        hasil = [tr for tr in transactions if tr['tanggal'].startswith(tahun)]

    else:
        print("Pilihan tidak valid.")
        return

    if not hasil:
        print("Tidak ada transaksi yang cocok.")
        return

    print("\nDaftar Transaksi:")
    for i, tr in enumerate(hasil, start=1):
        print(f"{i}. {tr['tanggal']} | {tr['jenis']} | {tr['kategori']} | Rp{tr['jumlah']}")


def ubah_transaksi(transactions):
    tampilkan_transaksi_filter(transactions)
    nomor = int(input("Nomor transaksi yang ingin diubah: "))
    index = nomor - 1

    if index < 0 or index >= len(transactions):
        print("Nomor tidak valid.")
        return

    # Tampilkan data lama
    data_lama = transactions[index]
    print("Data saat ini:")
    print(f"Tanggal : {data_lama['tanggal']}")
    print(f"Jenis   : {data_lama['jenis']}")
    print(f"Kategori: {data_lama['kategori']}")
    print(f"Jumlah  : {data_lama['jumlah']}")

    # Minta input baru
    print("\nMasukkan data baru:")
    tanggal = input("Tanggal baru: ")
    jenis = input("Jenis baru: ")
    kategori = input("Kategori baru: ")
    jumlah = input("Jumlah baru: ")

    # Simpan data baru (kalau kosong, tetap pakai data lama)
    transactions[index] = {
        'tanggal': tanggal if tanggal else data_lama['tanggal'],
        'jenis': jenis if jenis else data_lama['jenis'],
        'kategori': kategori if kategori else data_lama['kategori'],
        'jumlah': jumlah if jumlah else data_lama['jumlah']
    }

    save_data(transactions)
    print("✅ - Transaksi berhasil diubah.")

def hapus_transaksi(transactions):
    tampilkan_transaksi_filter(transactions)
    index = int(input("Masukkan nomor transaksi yang ingin dihapus: ")) - 1

    if 0 <= index < len(transactions):
        del transactions[index]
        save_data(transactions)
        print("🗑️ - Transaksi berhasil dihapus.")
    else:
        print("❌ - Nomor tidak valid.")
