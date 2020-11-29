import mysql.connector
import os,barang,barang_masuk,barang_keluar,satuan,jenis
 
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="db_tugas"
)

def show_menu(db):
    print("=== APLIKASI LOGISTIK PYTHON ===")
    print("1. DATA BARANG")
    print("2. DATA BARANG MASUK")
    print("3. DATA BARANG KELUAR")
    print("4. DATA JENIS")
    print("5. DATA SATUAN")
    print("\n\n0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")
 
    # clear screen
    os.system("clear")
 
    if menu == "1":
        barang.show_menu_barang(db)
    elif menu == "2":
        barang_masuk.show_menu_barang_masuk(db)
    elif menu == "3":
        barang_keluar.show_menu_barang_keluar(db)
    elif menu == "4":
        jenis.show_menu_jenis(db)
    elif menu == "5":
        satuan.show_menu_satuan(db)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")
 
if __name__ == "__main__":
    while (True):
        show_menu(db)