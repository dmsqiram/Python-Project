# import library
from os import system, __name__
import time

# fungsi validasi inputan jumlah belanjaan hanya berupa integer
def inputangka(angka):
    while True:
        try:
            angka = int(input(">> Jumlah Jenis Oli Yang Dibeli : "))
        except:
            print("\nWARNING : Masukkan Input Berupa Angka!!\n")
        else:
            return angka

# fungsi validasi inputan jumlah liter hanya berupa integer
def inputjumlah(angka):
    while True:
        try:
            angka = int(input(">> Masukkan Jumlah Oli/Liter    : "))
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

# fungsi validasi inputan hanya berupa huruf (a,b,c,d,e)
def inputhuruf(huruf):
      while(huruf != "a" and huruf != "b" and huruf != "c" and huruf != "d" and huruf != "e"):
        ulang = input(">> Masukkan Kode List Jenis Oli : ")

        if(ulang == "a" or ulang == "b" or ulang == "c" or ulang == "d" or ulang == "e"):
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

# fungsi void
def daftar_brg():

    print()
    print("+=========== DAFTAR BARANG ===========+")
    print("|-------------------------------------|")
    print("|                                     |")
    print("| A). Duration SW20      : Rp53.000/L |")
    print("| B). Castrol Magnatec   : Rp50.000/L |")
    print("| C). Federal Supreme XX : Rp54.000/L |")
    print("| D). Yamalube           : Rp45.000/L |")
    print("| E). Shell              : Rp46.000/L |")
    print("|                                     |")
    print("|-------------------------------------|")
    print("+=====================================+")
    print()

# program utama
while True:   

    _ = system('cls')
    daftar_brg()

    # variabel array 
    oli        = ["Duration SW20","Castrol Magnatec","Federal Supreme XX","Yamalube",   "Shell"]
    harga      = [53000,50000,54000,45000, 46000]
    kode       = ["a","b","c","d","e"]
    list_oli   = []
    list_harga = []
    list_qty   = []
    list_total = []
    list_kode  = []
    diskon     = 0.05
    ppn        = 0.01

    # memperoleh inputan user mengenai berapa jenis oli yang akan dibeli
    user = inputangka(">> Jumlah Jenis Oli Yang Dibeli : ")

    # validasi inputan tidak boleh <= 0
    while(user <= 0 or user > 5):

         print("\nWARNING : Hanya Tersedia 5 Jenis Oli, Masukkan Hanya 1-5!!\n")
         user = inputangka(">> Jumlah Jenis Oli Yang Dibeli : ")

         if(user <= 0):
             continue
         else:
             break
    print()

    # looping mencetak transaksi berdasarkan array
    i = 1
    while(i <= user):

        # menampilkan daftar barang, jika daftar barang sebelumnya tergeser dan tidak kelihatan
        if(i > 1):
            daftar_brg()

        print()

        # memperoleh inputan user mengenai jenis oli apa yang akan dibeli
        inpt_kode   = inputhuruf(">> Masukkan Kode List Jenis Oli : ")

        x = inpt_kode in list_kode
        while(x == True):
            print("\nWARNING : Jenis Oli Telah Terdaftar, Pilih Jenis Lainnya!!\n")
            inpt_kode   = inputhuruf(">> Masukkan Kode List Jenis Oli : ")

            x = inpt_kode in list_kode
            if(x == False):
                break
            else:
                continue

        sts = inpt_kode in kode
        while(sts == True):

            # memperoleh inputan user mengenai jumlah liter oli yang dibeli
            qty     = inputjumlah(">> Masukkan Jumlah Oli/Liter   : ")
            while(qty <= 0):

                print("\nWARNING : Kurang Dari 0 Tidak Diperbolehkan!!\n")
                qty = inputjumlah(">> Masukkan Jumlah Oli/Liter   : ")

                if(qty > 0):
                    break
                else:
                    continue

            no_index = kode.index(inpt_kode)        
            list_oli.append(oli[no_index])
            list_harga.append(harga[no_index])
            list_kode.append(inpt_kode)

            time.sleep(0.7)
            print("\n\n+=========== LIST BARANG",i,"===========+")
            print(">> Nama Barang  :",oli[no_index])
            print(">> Harga        :",uang(harga[no_index]),"Per Liter")
            print(">> Kuantitas    :",qty,"Liter")
            print("---------------------------------------")
            total_biaya = qty * harga[no_index]
            print(">> Total Harga  :",uang(total_biaya))
            print()
            list_total.append(total_biaya)
            list_qty.append(qty)

            i += 1
            input("\n>> Press Enter to Continue      : ")
            time.sleep(0.6)
            _ = system('cls')
            break
    
    # diskon pembelian
    print("DISKON")
    print("---------------------------------------")
    if(sum(list_total) >= 200000):
        print("\n-> Total Biaya     :",uang(sum(list_total)))
        print("-> Dapat Diskon 5% Untuk Pembelian >= Rp.200.000")
        nilai_diskon = sum(list_total) * diskon
        print("-> Diskon          :",uang(sum(list_total)),"x 5%")
        print("-> Potongan Diskon :",uang(int(nilai_diskon)))
    else:
        print("\n-> Total Biaya     :",uang(sum(list_total)))
        print("-> Tidak Dapat Diskon Untuk Pembelian < Rp.200.000")
        nilai_diskon = 0
        print("-> Diskon          :",uang(sum(list_total)),"x 0%")
        print("-> Potongan Diskon :",uang(int(nilai_diskon)))

    total_after_diskon = sum(list_total) - nilai_diskon
    
    # ppn penjualan
    print("\n\nPAJAK/PPN")
    print("---------------------------------------")
    print("\n-> Total Biaya     :",uang(int(total_after_diskon)))
    print("-> PPN 1% Untuk Setiap Pembelian")
    nilai_pajak = total_after_diskon * ppn
    print("-> Pajak/PPN       :",uang(int(total_after_diskon)),"x 1%")
    print("-> Tambahan Pajak  :",uang(int(nilai_pajak)))

    total_akhir  = total_after_diskon + nilai_pajak

    # Loading proses pembuatan resi transaksi
    print()
    print()
    time.sleep(2.5)

    delay = 8
    for i in range(delay):
        time.sleep(0.5)
        print("Loading...")

    time.sleep(0.5)   
    print() 
    print("Mohon Bersabar, Resi Transaksi Sedang Dibuat...")
    time.sleep(2.8)
    _ = system('cls')
    
    # print pembayaran
    print("\n+========== PRINT PEMBAYARAN =========+\n")
    print("-> Jumlah Jenis Oli :",user,"Jenis")
    print("-> Jumlah/Item      :",sum(list_qty),"Liter")
    print("---------------------------------------")
    print("-> Daftar Barang")

    urutan = 1
    i = 0
    while(i < user):
        time.sleep(0.7)
        print()   
        print("    ========= LIST BARANG (" + str(urutan) + ") =========")
        print("    Nama Barang     :",list_oli[i])
        print("    Harga           :",uang(list_harga[i]),"Per Liter")
        print("    Kuantitas       :",list_qty[i],"Liter")
        total = list_harga[i] * list_qty[i]
        print("    Total           :",uang(total))
        print("    -----------------------------------")
        list_total[i]
        urutan += 1
        i += 1

    time.sleep(0.7)
    print("---------------------------------------")
    print("-> Total Harga      :",uang(sum(list_total)))

    if(sum(list_total) >= 200000):
        print("-> Diskon           : 5%")
        print("-> Potongan Diskon  :",uang(int(nilai_diskon)))
    else:
        print("-> Diskon           : 0%")
        print("-> Potongan Diskon  :",uang(int(nilai_diskon)))

    print("-> Pajak\PPN        : 1%")
    print("-> Tambahan Pajak   :",uang(int(nilai_pajak)))
    print("---------------------------------------")
    print("-> Total Biaya      :",uang(int(total_akhir)))
    print("\n+============ TERIMA KASIH ===========+\n")

    # input ulang program oleh user
    ulang = inputulang(">> Transaksi Ulang [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
    else:
        break

# akhir program
print("\n+======= PROGRAM TELAH BERAKHIR ======+")


