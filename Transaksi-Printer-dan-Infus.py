# import library
from os import system, __name__

"""
+=======================================================+
| PROGRAM   : TRANSAKSI PRINTER DAN INFUS DENGAN PYTHON |
| NAMA      : DIMASQI RAMADHANI                         |
| KELAS     : 2C                                        |
| NIM       : 20083000088                               |
+=======================================================+
"""

# fungsi validasi integer inputan infus
def infus(jumlah):
    while True:
        try:
            jumlah = int(input(">> Inputkan Jumlah Infus        : "))
        except:
            print("\nWARNING : Inputkan Jumlah Barang Hanya Berupa Angka!!\n")
        else:
            return jumlah

# fungsi validasi integer inputan printerinfus
def printerinfus(jumlah):
    while True:
        try:
            jumlah = int(input(">> Inputkan Jumlah PrinterInfus : "))
        except:
            print("\nWARNING : Inputkan Jumlah Barang Hanya Berupa Angka!!\n")
        else:
            return jumlah

# fungsi validasi integer inputan printer
def printer(jumlah):
    while True:
        try:
            jumlah = int(input(">> Inputkan Jumlah Printer      : "))
        except:
            print("\nWARNING : Inputkan Jumlah Barang Hanya Berupa Angka!!\n")
        else:
            return jumlah

# validasi inputan ulang dari user
def inputulang(ulang):
    while(ulang != "Y" and ulang != "y" and ulang != "T" and ulang != "t"):
        ulang = input(">> Transaksi Baru : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Hanya Perintah [Y/T]!!\n")
            pass

# validasi inputan status dari infus
def inputinfus(sts):
    while(sts != "Y" and sts != "y" and sts != "T" and sts != "t"):
        sts = input(">> Pembelian Dengan Infus [Y/T] : ")

        if(sts == "Y" or sts == "y" or sts == "T" or sts == "t"):
            return sts
        else:
            print("\nWARNING : Masukkan Hanya Perintah [Y/T]!!\n")
            pass

# program utama, looping while agar user dapat mengulang program
while True:

    print("\n+============ TRANSAKSI PENJUALAN ===========+\n")

    # inisiasi variabel
    min_diskon = 1500000
    persen_diskon = 0.15
    hrg_dasar_printer = 660000
    hrg_infus = 250000
    hrg_satuan_printerinfus = hrg_dasar_printer + hrg_infus

    # memperoleh inputan user mengenai status infus
    sts_infus = inputinfus(">> Pembelian Dengan Infus [Y/T] : ")
    print()

    # pengkondisian if untuk pembayaran menggunakan infus atau tidak
    if(sts_infus == "Y" or sts_infus == "y"):

        qty_printerinfus = printerinfus(">> Inputkan Jumlah PrinterInfus : ") 

        # looping agar inputan tidak kurang dari 0
        while(qty_printerinfus < 0):

            print("\nWARNING : Jumlah PrinterInfus Tidak Boleh Kurang Dari 0!!\n")
            qty_printerinfus = printerinfus(">> Inputkan Jumlah PrinterInfus : ")

            if(qty_printerinfus > 0):
                break
            else:
                pass

        qty_printer = printer(">> Inputkan Jumlah Printer      : ")

        # looping agar inputan tidak kurang dari 0
        while(qty_printer < 0):

            print("\nWARNING : Jumlah Printer Tidak Boleh Kurang Dari 0!!\n")
            qty_printer = printerinfus(">> Inputkan Jumlah Printer : ")

            if(qty_printer > 0):
                break
            else:
                pass

        qty_infus = infus(">> Inputkan Jumlah Infus        : ")

        # looping agar inputan tidak kurang dari 0
        while(qty_infus < 0):

            print("\nWARNING : Jumlah Infus Tidak Boleh Kurang Dari 0!!\n")
            qty_infus = printerinfus(">> Inputkan Jumlah Infus : ")

            if(qty_infus > 0):
                break
            else:
                pass
        
        total_qty = (qty_infus + qty_printer + qty_printerinfus)

        # pengkondisian if untuk menentukan pembelian dari user 
        if(qty_printerinfus > 0 and qty_printer > 0 and qty_infus > 0):

            total_awal = (qty_printerinfus * hrg_satuan_printerinfus) + (qty_printer * hrg_dasar_printer) + (qty_infus * hrg_infus)
            print()
            print("1) PrinterInfus    :",qty_printerinfus,"Set")
            print("   Harga           :","Rp.",int(hrg_satuan_printerinfus))
            print("   Total           :","Rp.",int(hrg_satuan_printerinfus*qty_printerinfus),"\n")
            print("2) Printer         :",qty_printer,"Set")
            print("   Harga           :","Rp.",int(hrg_dasar_printer))
            print("   Total           :","Rp.",int(hrg_dasar_printer*qty_printer),"\n")
            print("3) Infus           :",qty_infus,"Set")
            print("   Harga           :","Rp.",int(hrg_infus),)
            print("   Total           :","Rp.",int(hrg_infus*qty_infus),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        elif(qty_printerinfus > 0 and qty_printer > 0):

            total_awal = (qty_printerinfus * hrg_satuan_printerinfus) + (qty_printer * hrg_dasar_printer)
            print()
            print("1) PrinterInfus    :",qty_printerinfus,"Set")
            print("   Harga           :","Rp.",int(hrg_satuan_printerinfus))
            print("   Total           :","Rp.",int(hrg_satuan_printerinfus*qty_printerinfus),"\n")
            print("2) Printer         :",qty_printer,"Set")
            print("   Harga           :","Rp.",int(hrg_dasar_printer))
            print("   Total           :","Rp.",int(hrg_dasar_printer*qty_printer),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        elif(qty_printerinfus > 0 and qty_infus > 0):

            total_awal = (qty_printerinfus * hrg_satuan_printerinfus) + (qty_infus * hrg_infus)
            print()
            print("1) PrinterInfus    :",qty_printerinfus,"Set")
            print("   Harga           :","Rp.",int(hrg_satuan_printerinfus))
            print("   Total           :","Rp.",int(hrg_satuan_printerinfus*qty_printerinfus),"\n")
            print("2) Infus           :",qty_infus,"Set")
            print("   Harga           :","Rp.",int(hrg_infus))
            print("   Total           :","Rp.",int(hrg_infus*qty_infus),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        elif(qty_printer > 0 and qty_infus > 0):

            total_awal = (qty_printer * hrg_dasar_printer) + (qty_infus * hrg_infus)
            print()
            print("1) Printer         :",qty_printer,"Set")
            print("   Harga           :","Rp.",int(hrg_dasar_printer))
            print("   Total           :","Rp.",int(hrg_dasar_printer*qty_printer),"\n")
            print("2) Infus           :",qty_infus,"Set")
            print("   Harga           :","Rp.",int(hrg_infus))
            print("   Total           :","Rp.",int(hrg_infus*qty_infus),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        elif(qty_printerinfus > 0):

            total_awal = qty_printerinfus * hrg_satuan_printerinfus
            print()
            print("1) PrinterInfus    :",qty_printerinfus,"Set")
            print("   Harga           :","Rp.",int(hrg_satuan_printerinfus))
            print("   Total           :","Rp.",int(hrg_satuan_printerinfus*qty_printerinfus),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        elif(qty_infus > 0):

            total_awal = qty_infus * hrg_infus
            print()
            print("1) Infus           :",qty_infus,"Set")
            print("   Harga           :","Rp.",int(hrg_infus))
            print("   Total           :","Rp.",int(hrg_infus*qty_infus),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)

        else:

            total_awal   = qty_printer * hrg_dasar_printer
            print()
            print("1) Printer         :",qty_printer,"Set")
            print("   Harga           :","Rp.",int(hrg_dasar_printer))
            print("   Total           :","Rp.",int(hrg_dasar_printer*qty_printer),"\n")
            print("Total Barang       :",total_qty,"Set")
            print("Total Harga        :","Rp.",total_awal)
    else:

        qty_printer  = printer(">> Inputkan Jumlah Printer      : ")
        total_qty    = qty_printer
        total_awal   = qty_printer * hrg_dasar_printer
        print()
        print("1) Printer         :",qty_printer,"Set")
        print("   Harga           :","Rp.",int(hrg_dasar_printer))
        print("   Total           :","Rp.",int(hrg_dasar_printer*qty_printer),"\n")
        print("Total Barang       :",total_qty,"Set")
        print("Total Harga        :","Rp.",total_awal)

    # diskon pembelian
    if(total_awal > min_diskon):
        print("\nDiskon 15% Untuk Pembelian > Rp. 1500000")
        nilai_diskon = total_awal * persen_diskon
        print("Potongan Diskon    :","Rp.",total_awal,"x 15% : Rp.",int(nilai_diskon))
    else:
        print("\nTidak ada Diskon Untuk Pembelian < Rp. 1500000")
        nilai_diskon = 0
        print("Potongan Diskon    :","Rp.",total_awal,"x 0%  : Rp.",int(nilai_diskon))

    total_akhir = total_awal - nilai_diskon

    # print pembayaran transaksi
    print()
    print("+============= PRINT PEMBAYARAN =============+\n")
    
    if(sts_infus == "Y" or sts_infus == "y"):

        if(qty_printerinfus > 0 and qty_printer > 0 and qty_infus > 0):

            print("1) Daftar Barang\n")
            print("   - PrinterInfus  :",qty_printerinfus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_satuan_printerinfus))
            print("     Total         :","Rp.",int(qty_printerinfus * hrg_satuan_printerinfus),"\n")
            print("   - Printer       :",qty_printer,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_dasar_printer))
            print("     Total         :","Rp.",int(qty_printer * hrg_dasar_printer),"\n")
            print("   - Infus         :",qty_infus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_infus))
            print("     Total         :","Rp.",int(qty_infus * hrg_infus),"\n")

        elif(qty_printerinfus > 0 and qty_printer > 0):

            print("1) Daftar Barang\n")
            print("   - PrinterInfus  :",qty_printerinfus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_satuan_printerinfus))
            print("     Total         :","Rp.",int(qty_printerinfus * hrg_satuan_printerinfus),"\n")
            print("   - Printer       :",qty_printer,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_dasar_printer))
            print("     Total         :","Rp.",int(qty_printer * hrg_dasar_printer),"\n")

        elif(qty_printerinfus > 0 and qty_infus > 0):

            print("1) Daftar Barang\n")
            print("   - PrinterInfus  :",qty_printerinfus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_satuan_printerinfus))
            print("     Total         :","Rp.",int(qty_printerinfus * hrg_satuan_printerinfus),"\n")
            print("   - Infus         :",qty_infus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_infus))
            print("     Total         :","Rp.",int(qty_infus * hrg_infus),"\n")

        elif(qty_printer > 0 and qty_infus > 0):
            print("1) Daftar Barang\n")
            print("   - Printer       :",qty_printer,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_dasar_printer))
            print("     Total         :","Rp.",int(qty_printer * hrg_dasar_printer),"\n")
            print("   - Infus         :",qty_infus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_infus))
            print("     Total         :","Rp.",int(qty_infus * hrg_infus),"\n")

        elif(qty_printerinfus > 0):
            print("1) Daftar Barang\n")
            print("   - PrinterInfus  :",qty_printerinfus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_satuan_printerinfus))
            print("     Total         :","Rp.",int(qty_printerinfus * hrg_satuan_printerinfus),"\n")
        
        elif(qty_infus > 0):
            print("1) Daftar Barang\n")
            print("   - Infus         :",qty_infus,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_infus))
            print("     Total         :","Rp.",int(qty_infus * hrg_infus),"\n")

        else:
            print("1) Daftar Barang\n")
            print("   - Printer       :",qty_printer,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_dasar_printer))
            print("     Total         :","Rp.",int(qty_printer * hrg_dasar_printer),"\n")
    else:
        if(qty_printer > 0):
            print("1) Daftar Barang\n")
            print("   - Printer       :",qty_printer,"Set")
            print("     Harga Satuan  :","Rp.",int(hrg_dasar_printer))
            print("     Total         :","Rp.",int(qty_printer * hrg_dasar_printer),"\n")

    print("2) Total Awal      :","Rp.",total_awal)
    print("3) Total Barang    :",total_qty,"Set")

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
    print("                   : Rp.",int(total_akhir))
    print("\n+=============== TERIMA KASIH ===============+")

    # memperoleh inputan user untuk mengulang program
    print()
    ulang = inputulang("\n>> Ulangi Transaksi : ")

    if(ulang == "Y" or ulang == "y"):
        True
        _ = system('cls')
    else:
        break
   
# akhir program
print("\n+========== PROGRAM TELAH BERAKHIR ==========+")
