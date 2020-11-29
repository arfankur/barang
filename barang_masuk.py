import mysql.connector
import os
import uuid
import sys,app

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_tugas"
)


def insert_data_barang_masuk(db):
    print('0. Batalkan')
    cursor = db.cursor()

    # barang_masuk_name = input('Masukkan nama barang_masuk\t')
    
    container_barang = []
    sql = "SELECT id,barang_name,barang_stock FROM barangs"
    cursor.execute(sql)
    result_barangs = cursor.fetchall()
    for jenis in result_barangs:
        container_barang.append(jenis)
    print(container_barang)

    barang_id = input('Masukkan id barang\t')
    if barang_id == '0': show_menu_barang_masuk(db)
    
    jumlah_barang_masuk = input('Jumlah barang masuk\t')
    if jumlah_barang_masuk == '0': show_menu_barang_masuk(db)

    val = (barang_id, jumlah_barang_masuk)
    cursor = db.cursor()
    sql = "INSERT INTO barang_masuks (barang_id,jumlah_barang_masuk) VALUES(%s,%s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data_barang_masuk(db):
    cursor = db.cursor()
    sql = "SELECT barang_masuks.id, barangs.barang_name, barang_masuks.jumlah_barang_masuk, barang_masuks.tanggal_barang_masuk FROM barang_masuks INNER JOIN barangs ON barang_masuks.barang_id =  barangs.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
        
    else:
        for data in results:
            print(data)
    print('\n')


def update_data_barang_masuk(db):
    print('0. Batalkan')
    cursor = db.cursor()
    show_data_barang_masuk(db)
    id = input('Masukkan ID \t')
    if id == '0': show_menu_barang_masuk(db)
    
    print('\n')
    # barang_masuk_name = input('Masukkan nama barang_masuk\t')
    
    container_barang = []
    sql = "SELECT id,barang_name,barang_stock FROM barangs"
    cursor.execute(sql)
    result_barangs = cursor.fetchall()
    for jenis in result_barangs:
        container_barang.append(jenis)
    print(container_barang)
    barang_id = input('Masukkan id barang\t')
    if barang_id == '0': show_menu_barang_masuk(db)
    
    jumlah_barang_masuk = input('Jumlah barang masuk\t')
    if jumlah_barang_masuk == '0': show_menu_barang_masuk(db)

    val = (barang_id, jumlah_barang_masuk,id)
    cursor = db.cursor()
    sql = "UPDATE barang_masuks SET barang_id=%s, jumlah_barang_masuk=%s WHERE id=%s"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data_barang_masuk(db):
    print('0. Batalkan')
    cursor = db.cursor()
    show_data_barang_masuk(db)
    id = input("pilih id barang_masuk ")
    if id == '0': show_menu_barang_masuk(db)
    
    sql = "DELETE FROM barang_masuks WHERE id=%s"
    # val = (id)
    cursor.execute(sql, id)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def show_menu_barang_masuk(db):
    print("=== NAVIGASI BARANG MASUK ===")
    print("1. Insert Data Barang Masuk")
    print("2. Tampilkan Data Barang Masuk")
    print("3. Update Data Barang Masuk")
    print("4. Hapus Data Barang Masuk")
    print('\n')
    print("9. Kembali")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu>\t ")

    os.system("clear")

    if menu == "1":
        insert_data_barang_masuk(db)
    elif menu == "2":
        show_data_barang_masuk(db)
    elif menu == "3":
        update_data_barang_masuk(db)
    elif menu == "4":
        delete_data_barang_masuk(db)
    elif menu == "9":
        app.show_menu(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu_barang_masuk(db)
