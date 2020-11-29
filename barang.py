import mysql.connector
import os
import uuid
import sys,app
from terminaltables import AsciiTable

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_tugas"
)

def insert_data_barang(db):
    print('0. Batalkan')
    cursor = db.cursor()

    barang_name = input('Masukkan nama barang\t')
    if barang_name == '0': show_menu_barang(db)
    
    container_jenis = []
    sql = "SELECT id,jenis_name FROM jeniss"
    cursor.execute(sql)
    result_jeniss = cursor.fetchall()
    for jenis in result_jeniss:
        container_jenis.append(jenis)
    print(container_jenis)
    jenis_id = input('Masukkan jenis barang\t')
    if jenis_id == '0': show_menu_barang(db)
    
    barang_stock = input('Masukkan Stock Barang\t')
    if barang_stock == '0': show_menu_barang(db)
    
    container_satuan = []
    sql = "SELECT id,satuan_name FROM satuans"
    cursor.execute(sql)
    result_satuans = cursor.fetchall()
    for satuan in result_satuans:
        container_satuan.append(satuan)
    print(container_satuan)
    satuan_id = input('Masukkan unit barang\t')
    if satuan_id == '0': show_menu_barang(db)
    
    val = (barang_name,jenis_id, barang_stock, satuan_id)
    cursor = db.cursor()
    sql = "INSERT INTO barangs (barang_name, jenis_id, barang_stock, satuan_id) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))


def show_data_barang(db):
    cursor = db.cursor()
    sql = "SELECT barangs.id, barangs.barang_name, jeniss.jenis_name, barangs.barang_stock, satuans.satuan_name FROM barangs LEFT JOIN satuans ON barangs.satuan_id = satuans.id LEFT JOIN jeniss ON barangs.jenis_id = jeniss.id GROUP BY barangs.id"
    cursor.execute(sql)
    results = cursor.fetchall()
    container_barang = [] 
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
            # header = [['id','barang_name','jenis_name','barang_stock','satuan_name'],[data[0],data[1]]]
            # container_barang.append(header)
        # for i in container_barang:
            
        # print(AsciiTable(header).table)
    # print(container_barang)
        print()


def update_data_barang(db):
    print('0. Batalkan')
    cursor = db.cursor()

    id = input('Masukkan ID barang\t')
    if id == '0': show_menu_barang(db)
    print('\n')
    barang_name = input('Masukkan nama barang\t')
    
    container_jenis = []
    sql = "SELECT id,jenis_name FROM jeniss"
    cursor.execute(sql)
    result_jeniss = cursor.fetchall()
    for jenis in result_jeniss:
        container_jenis.append(jenis)
    print(container_jenis)
    jenis_id = input('Masukkan jenis barang\t')
    if jenis_id == '0': show_menu_barang(db)
    barang_stock = input('Masukkan Stock Barang\t')
    if barang_stock == '0': show_menu_barang(db)
    container_satuan = []
    sql = "SELECT id,satuan_name FROM satuans"
    cursor.execute(sql)
    result_satuans = cursor.fetchall()
    for satuan in result_satuans:
        container_satuan.append(satuan)
    print(container_satuan)
    satuan_id = input('Masukkan unit barang\t')   
    if satuan_id == '0': show_menu_barang(db)
    val = (barang_name,jenis_id, barang_stock, satuan_id,id)
    cursor = db.cursor()
    sql = "UPDATE barangs SET barang_name=%s, jenis_id=%s, barang_stock=%s, satuan_id=%s WHERE id=%s"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data_barang(db):
    print('0. Batalkan')
    cursor = db.cursor()
    show_data_barang(db)
    id = input("pilih id barang ")
    if id == '0': show_menu_barang(db)
    sql = "DELETE FROM barangs WHERE id=%s"
    # val = (id)
    cursor.execute(sql, id)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def show_menu_barang(db):
    print("=== APLIKASI DATABASE PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print('\n')
    print("9. Kembali")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    # clear screen
    os.system("clear")

    if menu == "1":
        insert_data_barang(db)
    elif menu == "2":
        show_data_barang(db)
    elif menu == "3":
        update_data_barang(db)
    elif menu == "4":
        delete_data_barang(db)
    elif menu == "9":
        app.show_menu(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")

if __name__ == "__main__":
    while (True):
        show_menu_barang(db)