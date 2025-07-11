from file_manager import load_data
from transaksi import tambah_transaksi, tampilkan_transaksi_filter, ubah_transaksi, hapus_transaksi
from laporan import laporan

def menu():
    transactions = load_data()
    while True:
        print("\n=== Aplikasi Keuangan Pribadi ===")
        print("1. Tambah Transaksi")
        print("2. Tampilkan Transaksi")
        print("3. Ubah Transaksi")
        print("4. Hapus Transaksi")
        print("5. Laporan Keuangan")
        print("6. Keluar")
        pilihan = input("Pilih menu (1-6): ")

        if pilihan == '1':
            tambah_transaksi(transactions)
        elif pilihan == '2':
            tampilkan_transaksi_filter(transactions)
        elif pilihan == '3':
            ubah_transaksi(transactions)
        elif pilihan == '4':
            hapus_transaksi(transactions)
        elif pilihan == '5':
            laporan(transactions)
        elif pilihan == '6':
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("❌ - Pilihan tidak valid.")

if __name__ == "__main__":
    menu()
