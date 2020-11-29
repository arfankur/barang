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


def insert_data_jenis(db):
    print('0. Batalkan\n')
    jenis_name = input('Masukkan nama jenis') 
    if jenis_name == '0':
        show_menu_jenis(db)

    val = (jenis_name)
    cursor = db.cursor()
    sql = "INSERT INTO jeniss (jenis_name) VALUES ('%s')"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil disimpan".format(cursor.rowcount))

def show_data_jenis(db):
    cursor = db.cursor()
    sql = "SELECT * FROM jeniss"
    cursor.execute(sql)
    results = cursor.fetchall()
    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)
    print('\n')


def update_data_jenis(db):
    print('0. Batalkan\n')
    cursor = db.cursor()
    show_data_jenis(db)
    id = input('Masukkan ID \t')
    if id == '0':
        show_menu_jenis(db) 
    print('\n')
    
    
    jenis_name = input('Masukkan nama jenis\t') 
    if jenis_name == '0':
        show_menu_jenis(db) 

    val = (jenis_name,id)
    cursor = db.cursor()
    sql = "UPDATE jeniss SET jenis_name=%s WHERE id=%s"
    cursor.execute(sql, val)
    db.commit()
    print("{} data berhasil diubah".format(cursor.rowcount))

def delete_data_jenis(db):
    print('0. Batalkan\n')
    cursor = db.cursor()
    show_data_jenis(db)
    id = input("pilih id jenis ") 
    if id == '0':
        show_menu_jenis(db)
    sql = "DELETE FROM jeniss WHERE id=%s"
    # val = (id)
    cursor.execute(sql, id)
    db.commit()
    print("{} data berhasil dihapus".format(cursor.rowcount))

def show_menu_jenis(db):
    print("=== NAVIGASI JENIS ===")
    print("1. Insert Data Jenis")
    print("2. Tampilkan Data Jenis")
    print("3. Update Data Jenis")
    print("4. Hapus Data Jenis")
    print('\n')
    print("9. Kembali")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu>\t ") 

    os.system("clear")

    if menu == "1":
        insert_data_jenis(db)
    elif menu == "2":
        show_data_jenis(db)
    elif menu == "3":
        update_data_jenis(db)
    elif menu == "4":
        delete_data_jenis(db)
    elif menu == "9":
        app.show_menu(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")


if __name__ == "__main__":
    while (True):
        show_menu_jenis(db)
