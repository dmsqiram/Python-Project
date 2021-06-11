# import library
from os import system, name

"""
+====================================================+
| PROGRAM   : CEK KELULUSAN NILAI MENGGUNAKAN PYTHON |
| NAMA      : DIMASQI RAMADHANI                      |
| KELAS     : 2C                                     |
| NIM       : 20083000088                            |
+====================================================+
"""

# fungsi validasi agar user hanya menginputkan berupa integer/angka 
def inputangka(nilai):
    while True:
        try:
            nilai = float(input(">> Masukkan Nilai : "))
        except:
            print("\nWARNING : Tidak Boleh Ada Karakter selain Integer/Angka!!\n")
        else:
            return nilai

# fungsi input agar user dapat mengulang program
def inputulang(pesan):
    while (pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Ingin Mengulang [Y/T] : ") 

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

# program utama dimulai dari looping agar user dapat menginput nilai secara berulang
while True:

    print("\n+===== PROGRAM CEK STATUS NILAI MURID =====+\n")

    # input dari user untuk memasukkan nilai
    nilai = inputangka(">> Masukkan Nilai : ")

    # looping validasi nilai, agar nilai yang diinputkan antara 0-100
    while (nilai < 0) or (nilai > 100):

        print("\nWARNING : Masukkan Angka Hanya Dari 0-100!!\n")
        nilai = inputangka(">> Masukkan Nilai : " )

        if (nilai > 0) and (nilai < 100):
            break
        else:
            pass
        
    # array dari status lulus
    lulus = ["Lulus", "Tidak Lulus"]

    #pengkondisian if untuk menentukan status nilai
    if nilai > 60:
        print("Status Nilai Anda :",lulus[0])
    else:
        print("Status Nilai Anda :",lulus[1])

    # input ulang agar user dapat mengulang program
    print()
    ulang = inputulang("\n>> Ingin Mengulang [Y/T] : ")

    if (ulang == "y" or ulang == "Y"):
        True
        _ = system('cls')
    else:
        break

# akhir program
print("\n+========= PROGRAM TELAH BERAKHIR =========+")

