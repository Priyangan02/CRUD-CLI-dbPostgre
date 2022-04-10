import psycopg2
#Connect Database
conn = psycopg2.connect(
         host="localhost",
         database="univumc",
         user="alan",
         password="sialan02")

#Menyimpan Data Baru
def insert_data(conn):
   nim = input("Masukan NIM Mahasiswa: ")
   nama = input("Masukan Nama Mahasiswa: ")
   idfakultas = int(input("Masukan ID Fakultas Mahasiswa(1...5): "))
   idprodi = int(input("Masukan ID Prodi(1...10): "))
   val = (nim,nama,idfakultas,idprodi)
   sql = "INSERT INTO mahasiswa (nim, nama, idfakultas, idprodi) VALUES (%s, %s, %s, %s)"
   cur = conn.cursor()
   cur.execute(sql, val)
   conn.commit()
   print("="*20)
   print("{} Data Berhasil Disimpan".format(cur.rowcount))

#Menampilkan Data
def show_data(conn):
   cur = conn.cursor()
   sql = "SELECT * FROM mahasiswa"
   cur.execute(sql)
   result = cur.fetchall()

   if cur.rowcount < 0:
      print("="*20)
      print("DATA TIDAK ADA ATAU BELUM TERISI")
   else:
      print("="*20)
      print("DATA BERHASIL DITEMUKAN")
      print("-{} (ID, NIM, NAMA, IDFAKULTAS, IDPRODI)".format(cur.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(conn):
   cur = conn.cursor()
   show_data(conn)
   nims = input("Pilih NIM Mahasiswa: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   nama = input("Masukan Nama Mahasiswa Yang Baru: ")
   idfakultas = int(input("Masukan Id Fakultas yang Baru(1...5): "))
   idprodi = int(input("Masukan Id Prodi Yang Baru(1...10): "))
   sql = "UPDATE mahasiswa SET nim=%s, nama=%s, idfakultas=%s, idprodi=%s WHERE nim=%s"
   val = (nim, nama, idfakultas, idprodi, nims)
   cur.execute(sql, val)
   conn.commit()
   print("="*20)
   print("{} Data Berhasil Diupdate".format(cur.rowcount))

#Menghapus Data
def delete_data(conn):
   cur = conn.cursor()
   show_data(conn)
   nims = str(input("Pilih NIM Mahasiswa Yang Akan Dihapus: "))
   slc = "SELECT * FROM mahasiswa WHERE nim= %s"
   val = (nims)
   cur.execute(slc, val)
   con = cur.rowcount
   if (con == 1):
      inp = input("Apakah Anda Ingin Menghapus Data Tersebut? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswa WHERE nim=%s"
         val = (nims)
         cur.execute(sql, val)
         conn.commit()
         print("="*20)
         print("\b{} DATA BERHASIL DIHAPUS".format(cur.rowcount))
      else:
         print("DATA TIDAK TERHAPUS")
   else:
      print("TIDAK ADA NIM YANG DIMAKSUD")

#Mencari Data
def search_data(conn):
   cur = conn.cursor()
   keyword = input("MASUKAN NIM ATAU NAMA DATA YANG DICARI: ")
   sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   cur.execute(sql, val)
   result = cur.fetchall()

   if cur.rowcount <= 0:
      print("="*20)
      print("TIDAK ADA DATA YANG DIMAKSUD")
   else:
      print("="*20)
      print("{} DATA BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Menampilkan Menu
def show_menu(conn):
   print("===================================")
   print("|    TUGAS 1 CRUD Berbasis CLI    |")
   print("===================================")
   print("1. Tambahkan Data")
   print("2. Tampilkan Data")
   print("3. Perbaharui Data")  
   print("4. Hapus Data")
   print("5. Cari Data")
   print("0. Keluar")
   print("------------------")
   menu = input("Pilih Menu: ")

   if menu == "1":
      insert_data(conn)
   elif menu == "2":
      show_data(conn)
   elif menu == "3":
      update_data(conn)
   elif menu == "4":
      delete_data(conn)
   elif menu == "5":
      search_data(conn)
   elif menu == "0":
      exit()
   else:
      print("Menu Salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(conn)