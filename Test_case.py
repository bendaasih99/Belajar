import mysql.connector as mysql
def menu():
    print("=========================")
    print("=========MENU============")
    print("| 1. Lihat Saldo        |")
    print("| 2. Tambah Saldo       |")
    print("| 3. Tarik Saldo        |")
    print("| 4. Exit               |")
    b=input('Pilih Menu : ')
    cursor=db.cursor()
    if b=='1':
        lihat()
    elif b=='2':
        tambah()
    elif b=='3':
        tarik()
    elif b=='4':
        exit()
    else :
        print('Menu Tidak Ada')

def lihat():
    cursor=db.cursor()
    sql = "SELECT saldo FROM tb_berangkas"
    cursor.execute(sql)
    results=cursor.fetchall()
    print(results)
    
    menu()

def tambah():
    cursor=db.cursor()
    s=input('Tambah Saldo Anda = ')
    a=s+sql
    sql= "UPDATE tb_berangkas SET saldo=%s"
    cursor.execute(sql)
    db.commit()
    print('Saldo anda adalah = ')

def tarik():
    cursor=db.cursor()
    s=input('Tambah Saldo Anda = ')
    a=s-sql
    sql= "UPDATE tb_berangkas SET saldo=%s"
    cursor.execute(sql)
    db.commit()
    print('Saldo anda adalah = ')

def keluar():
    exit()

db = mysql.connect(
    host="localhost",
    user="root",
    password="aryanshaquille",
    database="atm")
print('Koneksi Database Berhasil')

print('Silahkan masukan pilihan anda :')
print('1 utk nasabah, 2 utk non nasabah')
a=input('Input angka = ')
cursor=db.cursor()
if a=='1':
        i=input('Username= ')
        ii=input('Password= ')
        sql = "INSERT INTO tb_user(Username, Password) VALUES(%s, %s)"
        val = (i, ii)
        cursor.execute(sql, val)
        db.commit()
        print("{} Data Berhasil ditambahkan".format(cursor.rowcount))
        menu()
else:   
    print('Maaf silahkan Resgistrasi terlebih dahulu')

