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


def insert_data_satuan(db):
    print('0. Batalkan\n')
    satuan_name = input('Masukkan nama satuan') 
    if satuan_name == '0':
        show_menu_satuan(db)

    val = (satuan_name)
    cursor = db.cursor()
    sql = "INSERT INTO satuans (satuan_name) VALUES ('%s')"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data_satuan(db):
    cursor = db.cursor()
    sql = "SELECT * FROM satuans"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
    print('\n')


def update_data_satuan(db):
    print('0. Batalkan\n')
    cursor = db.cursor()
    show_data_satuan(db)
    id = input('Masukkan ID \t')
    if id == '0':
        show_menu_satuan(db) 
    print('\n')
    
    
    satuan_name = input('Masukkan nama satuan\t') 
    if satuan_name == '0':
        show_menu_satuan(db) 

    val = (satuan_name,id)
    cursor = db.cursor()
    sql = "UPDATE satuans SET satuan_name=%s WHERE id=%s"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data_satuan(db):
    print('0. Batalkan\n')
    cursor = db.cursor()
    show_data_satuan(db)
    id = input("pilih id satuan ") 
    if id == '0':
        show_menu_satuan(db)
    sql = "DELETE FROM satuans WHERE id=%s"
    # val = (id)
    cursor.execute(sql, id)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def show_menu_satuan(db):
    print("=== NAVIGASI Satuan ===")
    print("1. Insert Data Satuan")
    print("2. Tampilkan Data Satuan")
    print("3. Update Data Satuan")
    print("4. Hapus Data Satuan")
    print('\n')
    print("9. Kembali")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu>\t ") 

    os.system("clear")

    if menu == "1":
        insert_data_satuan(db)
    elif menu == "2":
        show_data_satuan(db)
    elif menu == "3":
        update_data_satuan(db)
    elif menu == "4":
        delete_data_satuan(db)
    elif menu == "9":
        app.show_menu(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu_satuan(db)
