# import library
from os import system, name

"""
+====================================================+
| PROGRAM   : CEK TINGKAT USIA MENGGUNAKAN PYTHON    |
| NAMA      : DIMASQI RAMADHANI                      |
| KELAS     : 2C                                     |
| NIM       : 20083000088                            |
+====================================================+
"""

# fungsi validasi agar user hanya menginputkan berupa integer/angka 
def inputangka(umur):
    while True:
        try:
            umur = int(input(">> Masukkan Umur : "))
        except :
            print("\nWARNING : Masukkan Hanya Berupa Angka!!\n")
        else:
            return umur
        
# fungsi input agar user dapat mengulang program
def inputulang(pesan):
    while (pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Ingin Mengulang [Y/T] : ") 

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

# Program utama Python, dimulai dengan looping while agar user dapat mengulang program
while True:

    print("\n+===== PROGRAM CEK STATUS UMUR USIA =====+\n")

    # mengambil input dari user
    umur = inputangka(">> Masukkan Umur : ")

    while (umur < 0) or (umur > 100):

        print("\nWARNING : Masukkan Hanya Angka Dari 0-100!!\n")
        umur = inputangka(">> Masukkan Umur : ")

        if (umur > 0) and (umur < 100):
            break
    
    # array kategori usia
    sts_umur = ["Lansia", "Dewasa", "Pemuda", "Remaja", "Anak-Anak"]

    # pengkondisian if untuk menentukan status umur
    if (umur >= 60):
        print("Status Usia Anda :",sts_umur[0])
    elif (umur >= 35) and (umur < 60):
        print("Status Usia Anda :",sts_umur[1])
    elif (umur >= 18) and (umur < 35):
        print("Status Usia Anda :",sts_umur[2])
    elif (umur >= 15) and (umur < 18):
        print("Status Usia Anda :",sts_umur[3])
    else:
        print("Status Usia Anda :",sts_umur[4])
    
    # inputan buat user yang akan melakukan program ulang
    print()
    ulang = inputulang(">> Ingin Mengulang [Y/T] : ")

    if (ulang == "y" or ulang == "Y"):
        True
        _ = system('cls')
    else:
        break

# akhir program
print("\n+======== PROGRAM TELAH BERAKHIR ========+\n")