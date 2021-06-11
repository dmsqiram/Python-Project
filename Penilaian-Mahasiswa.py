# import library
from os import system, name

"""
+=============================================================+
| PROGRAM   : APLIKASI PENILAIAN MAHASISWA MENGGUNAKAN PYTHON |
| NAMA      : DIMASQI RAMADHANI                               |
| KELAS     : 2C                                              |
| NIM       : 20083000088                                     |
+=============================================================
"""

# fungsi validasi inputan user agar hanya berupa angka
def inputangka(nilai):
    while True:
        try:
            nilai = int(input(">> Masukkan Nilai : "))
        except:
            print("\nWARNING : Tidak Boleh Ada Karakter selain Integer/Angka!!\n")
        else:
            return nilai

# fungsi agar user hanya mengetikkan [Y/T]
def inputulang(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Ingin Mengulang [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

# fungsi/program utama, dimulai dari looping while agar user dapat mengulang program
while True:

    print("\n+====== PROGRAM PENILAIAN MAHASISWA =====+\n")

    # memperoleh input nilai dari user
    nilai = inputangka(">> Masukkan Nilai : ")

    # looping while untuk membatasi inputan user
    while(nilai < 0 or nilai > 100):

         print("\nWARNING : Masukkan Angka Hanya Dari 0-100!!\n")
         nilai = inputangka(">> Masukkan Nilai : ")

         if(nilai > 0 and nilai < 100):
             break
         else:
             continue
    
    # array dari nilai mahasiswa
    nilai_mhs = ['A','B','C','D']

    # pengkondisian if untuk menentukan nilai mahasiswa
    if(nilai >= 91):
        print("Status Nilai Anda :", nilai_mhs[0])
    elif(nilai >= 81 and nilai < 91):
        print("Status Nilai Anda :",nilai_mhs[1])
    elif(nilai >= 71 and nilai < 81):
        print("Status Nilai Anda :",nilai_mhs[2])
    else:
        print("Status Nilai Anda :",nilai_mhs[3])

    # inputan user agar dapat mengulang program    
    print()
    ulang = inputulang(">> Ingin Mengulang [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
        _ = system('cls')
    else:
        break

#akhir program
print("\n+======== PROGRAM TELAH BERAKHIR ========+")
