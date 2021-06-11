# import library
from os import system, name

"""
+======================================================+
| PROGRAM   : MENGECEK STATUS NILAI MENGGUNAKAN PYTHON |
| NAMA      : DIMASQI RAMADHANI                        |
| KELAS     : 2C                                       |
| NIM       : 20083000088                              |
+======================================================+     
"""

# fungsi untuk validasi inputan user hanya berupa angka/integer 
def inputangka(nilai):
    while True:
        try:
            nilai = int(input(">> Masukkan Nilai : "))
        except:
            print("\nWARNING : Tidak Boleh Ada Karakter selain Integer/Angka!!\n")
        else:
            return nilai

# fungsi agar user hanya memasukkan perintah [Y/T]
def inputulang(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("Ingin Mengulang [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

# fungsi/program utama, dimulai dengan while agar user dapat mengulang program
while True:

      print("\n+===== PROGRAM CEK STATUS NILAI MURID =====+\n")
      
      # input nilai dari user
      nilai = inputangka(">> Masukkan Nilai : ")
      
      # looping while agar nilai yang dimasukkan dari 0-100
      while(nilai < 0 or nilai > 100):

          print("\nWARNING : Masukkan Angka Hanya Dari 0-100!!\n")
          nilai = inputangka(">> Masukkan Nilai : ")

          if(nilai > 0 and nilai < 100):
              break
          else:
              pass
      
      # array dari status nilai
      sts_nilai = ["Baik Sekali", "Baik", "Cukup", "Kurang", "Kurang Sekali"]

      # pengkondisian if untuk status nilai
      if(nilai >= 80):
          print("Status Nilai Anda :",sts_nilai[0])
      elif(nilai >= 65 and nilai < 80):
          print("Status Nilai Anda :",sts_nilai[1])
      elif(nilai >= 55 and nilai < 65 ):
          print("Status Nilai Anda :",sts_nilai[2])
      elif(nilai >= 40 and nilai < 55):
          print("Status Nilai Anda :",sts_nilai[3])
      else:
          print("Status Nilai Anda :",sts_nilai[4])

      # input dari user untuk mengulang program
      print()      
      ulang = inputulang(">> Ingin Mengulang : ")

      if(ulang == "Y" or ulang == "y"):
          True
          _ = system('cls')
      else:
          break

# program berakhir
print("\n+========= PROGRAM TELAH BERAKHIR =========+")
