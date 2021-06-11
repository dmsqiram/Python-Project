# import library
from os import system, __name__

"""
+=====================================================+
| PROGRAM   : MENGHITUNG TRANSAKSI MENGGUNAKAN PYTHON |
| NAMA      : DIMASQI RAMADHANI                       |
| KELAS     : 2C                                      |
| NIM       : 20083000088                             |
+=====================================================+
"""

# fungsi validasi inputan berupa integer 
def inputbarang(jumlah):
    while True:
        try:
            jumlah = int(input(">> Masukkan Jumlah Barang  : "))
        except:
            print("\nWARNING : Masukkan Hanya Berupa Angka!!\n")
        else:
            return jumlah

# input untuk mengulang program    
def inputulang(ulang):
    while(ulang != "Y" and ulang != "y" and ulang != "T" and ulang != "t"):
        ulang = input(">> Ulangi Transaksi : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Perintah [Y/T]!!\n")
            pass

# program utama, while looping agar dapat mengulang program
while True:

    print("\n+============ TRANSAKSI PENJUALAN ===========+\n")

    # inisiasi variabel
    min_diskon = 1500000
    persen_diskon = 0.15
    harga_satuan = 660000

    # memperoleh inputan user
    qty = inputbarang(">> Masukkan Jumlah Barang  : ")

    # pengkondisian if agar user tidak memasukkan kuantiti barang < 0
    if(qty > 0):
        print("\nA) Jumlah Barang   :",qty,"Set")
        total_awal = harga_satuan * qty
        print("B) Total Awal      :","Rp.",harga_satuan,"x",qty)
        print("                   : Rp.",total_awal)
    else:
        while(qty < 0):

            print("\nWARNING : Jumlah Barang Tidak Boleh Kurang Dari 0\n")
            qty = inputbarang(">> Masukkan Jumlah Barang  : ")

            if(qty > 0):
                print("\nA) Jumlah Barang   :",qty,"Set")
                total_awal = harga_satuan * qty
                print("B) Total Awal      :","Rp.",harga_satuan,"x",qty)
                print("                   : Rp.",total_awal)
                break
            else:
                pass
    
    # menghitung diskon barang
    if(total_awal > min_diskon):
        print("\nDiskon 15% Untuk Pembelian > Rp. 1500000")
        nilai_diskon = total_awal * persen_diskon
        print("C) Potongan Diskon : Rp.",total_awal,"x 15%")
        print("                   : Rp.",int(nilai_diskon))
    else:
        print("\nTidak ada Diskon Untuk Pembelian < Rp. 1500000")
        nilai_diskon = 0
        print("C) Potongan Diskon : Rp.",total_awal,"x 0%")
        print("                   : Rp.",int(nilai_diskon))
    
    total_bayar = total_awal - nilai_diskon

    # print total pembayaran
    print()
    print("+============= PRINT PEMBAYARAN =============+\n")
    print("1) Nama Barang     : Printer Epson T20") 
    print("2) Total Barang    :",qty,"Set")
    print("3) Harga Barang    :","Rp.",harga_satuan)
    
    if(total_awal > min_diskon):
        print("4) Diskon          : 15%")
        print("5) Potongan Diskon :","Rp.",int(total_awal),"x 15%")
        print("                   : Rp.",int(nilai_diskon))
    else:
        print("4) Diskon          : 0%")
        print("5) Potongan Diskon :","Rp.",int(total_awal),"x 0%")
        print("                   : Rp.",int(nilai_diskon))

    print()
    print("6) Total Bayar     :","Rp.",int(total_awal),"- Rp.",int(nilai_diskon))
    print("                   : Rp.",int(total_bayar))
    print("\n+=============== TERIMA KASIH ===============+")

    # memperoleh inputan ulang user
    print()
    ulang = inputulang("\n>> Ulangi Transaksi : ")

    if(ulang == "Y" or ulang == "y"):
        True
        _ = system('cls')
    else:
        break

# akhir program 
print("\n+========== PROGRAM TELAH BERAKHIR ==========+")

    


