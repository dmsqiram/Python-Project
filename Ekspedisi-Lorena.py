# import library
from os import system, __name__
import time

# fungsi validasi inputan angka hanya berupa integer
def inputangka(angka):
    while True:
        try:
            angka = int(input(">> Masukkan Jumlah Tujuan : "))
        except:
            print("\nWARNING : Masukkan Input Berupa Angka!!\n")
        else:
            return angka

# fungsi validasi ulang program agar inputan hanya [Y/T]
def inputulang(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Transaksi Ulang [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

# fungsi validasi inputan hanya berupa huruf (a,b)
def inputhuruf(huruf):
      while(huruf != "a" and huruf != "b"):
        ulang = input(">> Masukkan Kode Tujuan   : ")

        if(ulang == "a" or ulang == "b"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Sesuai Tabel List!!\n")
            pass

# fungsi format merubah integer menjadi mata uang
def uang(nilai):
    x = str(nilai)

    if(len(x) <= 3):
        return "Rp. " + x
    else:
        a = x[:-3]
        b = x[-3:]
        return uang(a) + "." + b

# program utama
while True:    

    print()
    print("+======= EKSPEDISI LORENA =======+")
    print("|--------------------------------|")
    print("|                                |")
    print("| A). SURABAYA 169KM Rp.2.500/KM |")
    print("| B). BANDUNG  452KM Rp.4.000/KM |")
    print("|                                |")
    print("|--------------------------------|")
    print("+================================+")
    print()

    # variabel array 
    kota       = ["Surabaya","Bandung"]
    harga      = [2500,4000]
    kode       = ["a","b"]
    jarak      = [169,452]
    list_kota  = []
    list_harga = []
    list_jarak = []
    list_total = []

    user = inputangka(">> Masukkan Jumlah Tujuan : ")

    # validasi inputan tidak boleh <= 0
    while(user <= 0):

         print("\nWARNING : Kurang Dari 0 Tidak Diperbolehkan!!\n")
         user = inputangka(">> Masukkan Jumlah Tujuan : ")

         if(user > 0):
             break
         else:
             continue

    # looping mencetak transaksi berdasarkan array
    i = 1
    while(i <= user):
        print()
        inpt_kode = inputhuruf(">> Masukkan Kode Tujuan   : ")
        sts = inpt_kode in kode
        while(sts == True):

            no_index = kode.index(inpt_kode)

            list_kota.append(kota[no_index])
            list_harga.append(harga[no_index])
            list_jarak.append(jarak[no_index]) 

            print("\n+=========== TUJUAN",i,"===========+")
            print(">> Tujuan       :",kota[no_index])
            print(">> Jarak        :",jarak[no_index],"Km")
            print(">> Harga/Km     :",uang(harga[no_index]))
            print("----------------------------------")
            total_biaya = jarak[no_index] * harga[no_index]
            print(">> Total Biaya  :",uang(total_biaya))
            list_total.append(total_biaya)
            print()   
            i += 1
            break
    
    # Loading proses pembuatan resi transaksi
    time.sleep(2.5)

    delay = 3
    for i in range((delay)):
        time.sleep(0.6)
        print("Loading...")
    
    print("Resi Transaksi Sedang Dibuat...")
    time.sleep(2.5)
    
    # print pembayaran
    print("\n+======= PRINT PEMBAYARAN =======+\n")
    print("(1) Jumlah Tujuan  :",user,"Tempat")
    print("----------------------------------")
    print("(2) Daftar Tujuan")
    
    urutan = 1
    i = 0
    while(i < user):
        print()
        print("    ========= TUJUAN (" + str(urutan) + ") =========")
        print("    Kota Tujuan    :",list_kota[i])
        print("    Jarak Kota     :",list_jarak[i],"Km")
        print("    Harga/Km       :",uang(list_harga[i]))
        total = list_harga[i] * list_jarak[i]
        print("    Total          :",uang(total))
        print("    ------------------------------")
        list_total[i]
        urutan += 1
        i += 1

    print("----------------------------------")
    print("(3) Total Biaya    :",uang(sum(list_total)))
    print("\n+========= TERIMA KASIH =========+\n")

    # input ulang program oleh user
    ulang = inputulang(">> Transaksi Ulang [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
        _ = system('cls')
    else:
        break

# akhir program
print("\n+==== PROGRAM TELAH BERAKHIR ====+")


