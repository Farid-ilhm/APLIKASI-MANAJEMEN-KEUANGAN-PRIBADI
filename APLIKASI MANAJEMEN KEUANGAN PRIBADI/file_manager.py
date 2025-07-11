import csv
import os

FILE_NAME = 'data.csv'

def load_data():
    transactions = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    return transactions

def save_data(transactions):
    with open(FILE_NAME, 'w', newline='') as file:
        fieldnames = ['tanggal', 'jenis', 'kategori', 'jumlah']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for tr in transactions:
            writer.writerow(tr)
