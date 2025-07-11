def laporan(transactions):
    total_masuk = 0
    total_keluar = 0
    kategori_pengeluaran = {}

    for tr in transactions:
        jumlah = int(tr['jumlah'])
        if tr['jenis'] == 'pemasukan':
            total_masuk += jumlah
        elif tr['jenis'] == 'pengeluaran':
            total_keluar += jumlah
            kategori_pengeluaran[tr['kategori']] = kategori_pengeluaran.get(tr['kategori'], 0) + jumlah

    saldo = total_masuk - total_keluar

    print("\n📊 - Laporan Keuangan:")
    print(f"Total Pemasukan   : Rp{total_masuk}")
    print(f"Total Pengeluaran : Rp{total_keluar}")
    print(f"Sisa Saldo        : Rp{saldo}")
    print("Pengeluaran per Kategori:")
    for k, v in kategori_pengeluaran.items():
        print(f" - {k}: Rp{v}")
