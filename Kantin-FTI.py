# import library
from os import system, __name__
import time


# fungsi validasi inputan user agar hanya berupa integer
def inputangka(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan No Daftar Menu : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan


# fungsi validasi inputan user agar hanya berupa integer
def inputangka_mkn(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan Jumlah Porsi : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan


# fungsi validasi inputan user agar hanya berupa integer
def inputangka_mnm(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan Jumlah Kuantitas : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan


# fungsi validasi inputan user agar hanya berupa integer
def inputangka_bayar(pesan):
    while True:
        try:
            pesan = int(input(">> Uang Pembayaran  : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan


# fungsi validasi inputan user agar pilihan makanan sesuai dengan yang ada list menu
def inputmakanan(pesan):
    while(pesan != "a" and pesan != "b" and pesan != "c" and pesan != "d" and pesan != "e" and pesan != "f"):
        ulang = input(">> Masukkan Kode Makanan : ")

        if(ulang == "a" or ulang == "b" or ulang == "c" or ulang == "d" or ulang == "e" or ulang == "f"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Inputan Sesuai Pilihan Menu\n")
            pass


# fungsi validasi inputan user agar pilihan minuman sesuai dengan yang ada list menu
def inputminuman(pesan):
    while(pesan != "a" and pesan != "b" and pesan != "c" and pesan != "d" and pesan != "e"):
        ulang = input(">> Masukkan Kode Minuman     : ")

        if(ulang == "a" or ulang == "b" or ulang == "c" or ulang == "d" or ulang == "e"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Inputan Sesuai Pilihan Menu\n")
            pass


# fungsi validasi inputan user sesuai dengan yang diperintahkan [Y/T]
def inputpilihan(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Transaksi Ulang [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]\n")
            pass


# fungsi validasi inputan user sesuai dengan yang diperintahkan [Y/T]
def inputpilihan_mkn(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Pilih Menu Makanan Kembali [Y/T]     : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]")
            pass


# fungsi validasi inputan user sesuai dengan yang diperintahkan [Y/T]
def inputpilihan_mnm(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]")
            pass


# fungsi validasi inputan user sesuai dengan yang diperintahkan [Y/T]
def inputtambahan_mkn(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Ingin Menambahkan Menu Makanan [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]")
            pass


# fungsi validasi inputan user sesuai dengan yang diperintahkan [Y/T]
def inputtambahan_mnm(pesan):
    while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Ingin Menambahkan Menu Minuman [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING!! : Masukkan Input Perintah Berupa [Y/T]")
            pass


# fungsi konversi integer menjadi format mata uang
def uang(nilai):
    x = str(nilai)

    if(len(x) <= 3):
        return "Rp. " + x
    else:
        a = x[:-3]
        b = x[-3:]
        return uang(a) + "." + b


# mencetak resi transaski berupa file.txt dari suatu transaksi
def resi_transaksi():

    resi = open("Resi-Transaksi.txt", "w")

    resi.write("+========== PRINT PEMBAYARAN =========+\n\n")
    resi.write("-> Jumlah Makanan : " + str(sum(list_qty_mkn)) + " Makanan\n")
    resi.write("-> Jumlah Minuman : " + str(sum(list_qty_mnm)) + " Minuman\n")
    resi.write("---------------------------------------\n\n")

    if(mkn == True):
        urutan = 1
        i = 0
        resi.write("-> Daftar Makanan\n")
        while(i < i_mkn):
            time.sleep(0.7)
            resi.write("\n")
            resi.write("    ========= LIST MAKANAN (" +
                       str(urutan) + ") ========\n")
            resi.write("    Nama Makanan  : " + str(list_makanan[i]) + "\n")
            resi.write("    Harga         : " +
                       uang(list_harga_mkn[i]) + " Per Porsi\n")
            resi.write("    Kuantitas     : " +
                       str(list_qty_mkn[i]) + " Porsi\n")
            total = list_harga_mkn[i] * list_qty_mkn[i]
            resi.write("    Total         : " + str(uang(total)) + "\n")
            resi.write("    -----------------------------------\n")
            list_total_mkn[i]
            urutan += 1
            i += 1

    if(mnm == True):
        urutan = 1
        i = 0
        resi.write("\n-> Daftar Minuman\n")
        while(i < i_mnm):
            time.sleep(0.7)
            resi.write("\n")
            resi.write("    ========= LIST MINUMAN (" +
                       str(urutan) + ") ========\n")
            resi.write("    Nama Minuman  : " + str(list_minuman[i]) + "\n")
            resi.write("    Harga         : " +
                       str(uang(list_harga_mnm[i])) + " Per Gelas\n")
            resi.write("    Kuantitas     : " +
                       str(list_qty_mnm[i]) + " Gelas\n")
            total = list_harga_mnm[i] * list_qty_mnm[i]
            resi.write("    Total         : " + str(uang(total)) + "\n")
            resi.write("    -----------------------------------\n")
            list_total_mnm[i]
            urutan += 1
            i += 1

    time.sleep(0.7)
    resi.write("\n---------------------------------------\n")
    resi.write("-> Total Harga    : " + uang(tot) + "\n")
    resi.write("-> Pembayaran     : " + uang(bayar) + "\n")
    resi.write("-> Kembalian      : " + uang(kembalian) + "\n")
    resi.write("\n+============ TERIMA KASIH ===========+\n")


# mencetak resi transaski berupa file.txt dari suatu transaksi
def daftar_makanan():

    print()
    print("+=========== DAFTAR MENU KANTIN FTI ===========+")
    print("|----------------------------------------------|")
    print("|================ MENU MAKANAN ================|")
    print("|                                              |")
    print("| A). Nasi Goreng        : Rp. 15.000          |")
    print("| B). Lontong Goreng     : Rp. 14.900          |")
    print("| C). Bakso Goreng       : Rp. 12.900          |")
    print("| D). Rujak Goreng       : Rp. 13.000          |")
    print("| E). Rujak Bakso        : Rp. 15.000          |")
    print("| F). Rujak Bakso Pecel  : Rp. 17.000          |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print("+==============================================+")
    print()


# fungsi menampilkan list minuman
def daftar_minuman():

    print()
    print("+=========== DAFTAR MENU KANTIN FTI ===========+")
    print("|----------------------------------------------|")
    print("|================ MENU MINUMAN ================|")
    print("|                                              |")
    print("| A). Teh Dingin/Panas   : Rp. 2.500           |")
    print("| B). Kopi Dingin        : Rp. 5.000           |")
    print("| C). Kopi Teh Panas     : Rp. 6.500           |")
    print("| D). Coca-Cola Dingin   : Rp. 3.500           |")
    print("| E). Coca-Cola Panas    : Rp. 5.000           |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print("+==============================================+")
    print()


# program utama dari transaksi kantin FTI
while True:

    _ = system('cls')

    print()
    print("+=========== DAFTAR MENU KANTIN FTI ===========+")
    print("|----------------------------------------------|")
    print("|                                              |")
    print("| PETUNJUK PEMESANAN       :                   |")
    print("|                                              |")
    print("| 1). Ketik 1 Untuk Memilih Menu Makanan       |")
    print("| 2). Ketik 2 Untuk Memilih Menu Minuman       |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print("+==============================================+")
    print()

    # variabel list makanan
    makanan = ["Nasi Goreng", "Lontong Goreng",
               "Bakso Goreng", "Rujak Goreng", "Rujak Bakso Pecel"]
    harga_mkn = [15000, 14900, 12900, 13000, 15000, 17000]
    kode_mkn = ["a", "b", "c", "d", "e", "f"]
    list_makanan = []
    list_harga_mkn = []
    list_qty_mkn = []
    list_total_mkn = []
    list_kode_mkn = []
    qty_mkn = 0
    mkn = False

    # variabel list minuman
    minuman = ["Teh Dingin/Panas", "Kopi Dingin",
               "Kopi Teh Panas", "Coca-Cola Dingin", "Coca-Cola Panas"]
    harga_mnm = [2500, 5000, 6500, 3500, 5000]
    kode_mnm = ["a", "b", "c", "d", "e"]
    list_minuman = []
    list_harga_mnm = []
    list_qty_mnm = []
    list_total_mnm = []
    list_kode_mnm = []
    qty_mnm = 0
    mnm = False

    # inputan user untuk memilih antara menu makanan atau minuman
    ipt_menu = inputangka(">> Masukkan No Daftar Menu : ")

    # perulangan yang digunakan untuk memvalidasi inputan agar hanya berupa pilihan 1 atau 2
    while(ipt_menu <= 0 or ipt_menu >= 3):
        print("\nWARNING!! : Masukkan Inputan Sesuai Pilihan Menu\n")
        ipt_menu = inputangka(">> Masukkan No Daftar Menu : ")

        if(ipt_menu > 0 and ipt_menu < 3):
            break
        else:
            pass

    _ = system("cls")

    # penkondisian utama dari pilihan user 1. untuk makanan
    if(ipt_menu == 1):

        # perulangan pertama untuk memilih menu makanan
        mkn = True
        urutan = 1
        i_mkn = 0
        sts = True
        while (sts == True):

            # inputan user agar memasukkan kode makanan
            daftar_makanan()
            ipt_makanan = inputmakanan(">> Masukkan Kode Makanan : ")

            # perulangan agar user tidak memasukkan kode makanan yang sama ke dalam tempt storage
            x = ipt_makanan in list_kode_mkn
            while(x == True):
                print(
                    "\nWARNING!! : Makanan Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Makanan yang Lain\n")
                ipt_makanan = inputmakanan(">> Masukkan Kode Makanan : ")

                x = ipt_makanan in list_kode_mkn
                if(x == False):
                    break
                else:
                    continue

            # inputan user untuk memasukkan kuantiti dari makanan yang dipesan
            qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")

            # validasi dari inputan user agar tidak memasukkan kuantiti <= 0
            while(qty_mkn <= 0):
                print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")

                if(qty_mkn > 0):
                    break
                else:
                    pass

            # variabel yang digunakan sebagai temp storage, untuk menyimpan semua pesanan yang dipilih
            no_index = kode_mkn.index(ipt_makanan)
            list_makanan.append(makanan[no_index])
            list_harga_mkn.append(harga_mkn[no_index])
            list_kode_mkn.append(ipt_makanan)

            time.sleep(0.7)
            print("\n\n+=========== LIST MAKANAN", urutan, "===========+")
            print(">> Nama Makanan  :", makanan[no_index])
            print(">> Harga         :", uang(harga_mkn[no_index]), "Per Porsi")
            print(">> Kuantitas     :", qty_mkn, "Porsi")
            print("----------------------------------------")
            total_biaya_mkn = qty_mkn * harga_mkn[no_index]
            print(">> Total Harga  :", uang(total_biaya_mkn))
            print()
            list_total_mkn.append(total_biaya_mkn)
            list_qty_mkn.append(qty_mkn)
            i_mkn += 1
            i_mnm = 0
            urutan += 1

            # inputan untuk memastikan jika user ingin memesan makanan lebih dari sekali
            # jika user menjawab Y atau y, maka sistem akan balik looping untuk menampilkan menu makanan
            # jika T atau t, maka sistem akan menawarkan pilihan kembali apakah ingin menambahkan minuman
            # jika Y atau y, maka sistem akan beralih ke menu daftar minuman
            # jika T atau t, maka sistem akan langsung keluar dari looping dan melanjutkan untuk melakukan pembayaran
            pilihan_mkn = inputpilihan_mkn(
                "\n>> Pilih Menu Makanan Kembali [Y/T]     : ")
            if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                sts = True
                time.sleep(0.7)
                _ = system('cls')
            else:
                pilihan_mnm = inputtambahan_mnm(
                    "\n>> Ingin Menambahkan Menu Minuman [Y/T] : ")
                if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                    _ = system('cls')

                    # perulangan kedua jika user ingin menambahkan menu minuman
                    mnm = True
                    urutan = 1
                    i_mnm = 0
                    sts = True
                    while(sts == True):

                        # inputan user agar memasukkan kode minuman
                        daftar_minuman()
                        ipt_minuman = inputminuman(
                            ">> Masukkan Kode Minuman     : ")

                        # perulangan agar user tidak memasukkan daftar menu yang sama ke dalam list
                        x = ipt_minuman in list_kode_mnm
                        while(x == True):
                            print(
                                "\nWARNING!! : Minuman Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Minuman yang Lain\n")
                            ipt_minuman = inputminuman(
                                ">> Masukkan Kode Minuman     : ")

                            x = ipt_minuman in list_kode_mnm
                            if(x == False):
                                break
                            else:
                                continue

                        # inputan user untuk memasukkan kuantiti dari menu yang dipilih
                        qty_mnm = inputangka_mnm(
                            ">> Masukkan Jumlah Kuantitas : ")

                        # perulangan agar user tidak memasukkan kuantiti <= 0
                        while(qty_mnm <= 0):
                            print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                            qty_mnm = inputangka_mnm(
                                ">> Masukkan Jumlah Kuantitas : ")

                            if(qty_mnm > 0):
                                break
                            else:
                                pass

                        # variabel yang berfungsi sebagai temp storage, dari pilihan menu yang dipilih user
                        no_index = kode_mnm.index(ipt_minuman)
                        list_minuman.append(minuman[no_index])
                        list_harga_mnm.append(harga_mnm[no_index])
                        list_kode_mnm.append(ipt_minuman)

                        time.sleep(0.7)
                        print("\n\n+=========== LIST MINUMAN",
                              urutan, "===========+")
                        print(">> Nama Makanan  :", minuman[no_index])
                        print(">> Harga         :", uang(
                            harga_mnm[no_index]), "Per Gelas")
                        print(">> Kuantitas     :", qty_mnm, "Gelas")
                        print("----------------------------------------")
                        total_biaya_mnm = qty_mnm * harga_mnm[no_index]
                        print(">> Total Harga  :", uang(total_biaya_mnm))
                        print()
                        list_total_mnm.append(total_biaya_mnm)
                        list_qty_mnm.append(qty_mnm)
                        i_mnm += 1
                        urutan += 1

                        # inputan berupa pilihan, apakah user ingin memilih menu minumab yang lain atau tidak
                        pilihan_mnm = inputpilihan_mnm(
                            "\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

                        if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                            sts = True
                            time.sleep(0.7)
                            _ = system('cls')
                        else:
                            sts = False
                else:
                    break

    # pengkondisian kedua jika user pada tahap awal langsung memilih menu minuman
    else:

        # perulangan pertama untuk memilih menu minuman
        mnm = True
        urutan = 1
        i_mnm = 0
        sts = True
        while(sts == True):

            # inputan user agar dapat memasukkan kode minuman
            daftar_minuman()
            ipt_minuman = inputminuman(">> Masukkan Kode Minuman     : ")

            # perulangan agar user tidak memasukkan kode yang sama ke dalam list pesanan mereka
            x = ipt_minuman in list_kode_mnm
            while(x == True):
                print(
                    "\nWARNING!! : Minuman Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Minuman yang Lain\n")
                ipt_minuman = inputminuman(">> Masukkan Kode Minuman     : ")

                x = ipt_minuman in list_kode_mnm
                if(x == False):
                    break
                else:
                    continue

            # inputan mengenai kuantiti yang ingin dipesan
            qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")

            # perulangan agar user tidak memasukkan kuantiti <= 0
            while(qty_mnm <= 0):
                print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")

                if(qty_mnm > 0):
                    break
                else:
                    pass

            # variabel yang berfungsi sebagai temp storage, untuk menyimpan semua pilihan menu yang dipesan
            no_index = kode_mnm.index(ipt_minuman)
            list_minuman.append(minuman[no_index])
            list_harga_mnm.append(harga_mnm[no_index])
            list_kode_mnm.append(ipt_minuman)

            time.sleep(0.7)
            print("\n\n+=========== LIST MINUMAN", urutan, "===========+")
            print(">> Nama Makanan  :", minuman[no_index])
            print(">> Harga         :", uang(harga_mnm[no_index]), "Per Gelas")
            print(">> Kuantitas     :", qty_mnm, "Gelas")
            print("----------------------------------------")
            total_biaya_mnm = qty_mnm * harga_mnm[no_index]
            print(">> Total Harga  :", uang(total_biaya_mnm))
            print()
            list_total_mnm.append(total_biaya_mnm)
            list_qty_mnm.append(qty_mnm)
            i_mnm += 1
            i_mkn = 0
            urutan += 1

            # inputan untuk memastikan jika user ingin memesan makanan lebih dari sekali
            # jika user menjawab Y atau y, maka sistem akan balik looping untuk menampilkan menu minuman
            # jika T atau t, maka sistem akan akan menawarkan pilihan kembali apakah ingin menambahkan makanan
            # jika Y atau y, maka sistem akan beralih ke menu daftar makanan
            # jika T atau t, maka sistem akan langsung keluar dari looping dan melanjutkan untuk melakukan pembayaran
            pilihan_mnm = inputpilihan_mnm(
                "\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

            if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                sts = True
                time.sleep(0.7)
                _ = system('cls')
            else:
                pilihan_mkn = inputtambahan_mkn(
                    "\n>> Ingin Menambahkan Menu Makanan [Y/T] : ")
                if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                    _ = system('cls')

                    # perulangan kedua agar user dapat menambahkan menu makanan kedalam list mereka
                    mkn = True
                    urutan = 1
                    i_mkn = 0
                    sts = True
                    while(sts == True):

                        # inputan user agar dapat menginputkan kode makanan yang ingin dipesan
                        daftar_makanan()
                        ipt_makanan = inputmakanan(
                            ">> Masukkan Kode Makanan : ")

                        # perulangan agar user tidak memasukkan kode yang sama kedalam list mereka
                        x = ipt_makanan in list_kode_mkn
                        while(x == True):
                            print(
                                "\nWARNING!! : Makanan Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Makanan yang Lain\n")
                            inpt_kode = inputmakanan(
                                ">> Masukkan Kode Makanan : ")

                            x = inpt_kode in list_kode_mkn
                            if(x == False):
                                break
                            else:
                                continue
                        # inputan agar user dapat memasukkan kuantiti dari pesanan yang dipilih
                        qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")

                        # inputan user agar tidak memasukkan kuantiti <= 0
                        while(qty_mkn <= 0):
                            print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                            qty_mkn = inputangka_mkn(
                                ">> Masukkan Jumlah Porsi : ")

                            if(qty_mkn > 0):
                                break
                            else:
                                pass

                        # variabel yang berfungsi sebagai temp storage, untuk menyimpan data menu yang dipesan user
                        no_index = kode_mkn.index(ipt_makanan)
                        list_makanan.append(makanan[no_index])
                        list_harga_mkn.append(harga_mkn[no_index])
                        list_kode_mkn.append(ipt_makanan)

                        time.sleep(0.7)
                        print("\n\n+=========== LIST MAKANAN",
                              urutan, "===========+")
                        print(">> Nama Makanan  :", makanan[no_index])
                        print(">> Harga         :", uang(
                            harga_mkn[no_index]), "Per Porsi")
                        print(">> Kuantitas     :", qty_mkn, "Porsi")
                        print("----------------------------------------")
                        total_biaya_mkn = qty_mkn * harga_mkn[no_index]
                        print(">> Total Harga  :", uang(total_biaya_mkn))
                        print()
                        list_total_mkn.append(total_biaya_mkn)
                        list_qty_mkn.append(qty_mkn)
                        i_mkn += 1
                        urutan += 1

                        # inputan user agar dapat memilih kembali menu makanan
                        pilihan_mkn = inputpilihan_mkn(
                            "\n>> Pilih Menu Makanan Kembali [Y/T]     : ")

                        if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                            sts = True
                            time.sleep(0.7)
                            _ = system('cls')
                        else:
                            sts = False
                else:
                    break

    _ = system('cls')

    # menampilkan list data pemesanan dari temp storage
    time.sleep(0.7)
    if(mkn == True):
        urutan = 1
        i = 0
        print("-> Daftar Makanan")
        while(i < i_mkn):
            time.sleep(0.7)
            print()
            print("    LIST MAKANAN (" + str(urutan) + ")")
            print("    -----------------------------------")
            print("    Nama Makanan    :", list_makanan[i])
            print("    Harga           :", uang(
                list_harga_mkn[i]), "Per Porsi")
            print("    Kuantitas       :", list_qty_mkn[i], "Porsi")
            total = list_harga_mkn[i] * list_qty_mkn[i]
            print("    Total           :", uang(total))
            print("    -----------------------------------")
            list_total_mkn[i]
            urutan += 1
            i += 1

    time.sleep(0.7)
    if(mnm == True):
        urutan = 1
        i = 0
        print("\n-> Daftar Minuman")
        while(i < i_mnm):
            time.sleep(0.7)
            print()
            print("    LIST MINUMAN (" + str(urutan) + ")")
            print("    -----------------------------------")
            print("    Nama Minuman    :", list_minuman[i])
            print("    Harga           :", uang(
                list_harga_mnm[i]), "Per Gelas")
            print("    Kuantitas       :", list_qty_mnm[i], "Gelas")
            total = list_harga_mnm[i] * list_qty_mnm[i]
            print("    Total           :", uang(total))
            print("    -----------------------------------")
            list_total_mnm[i]
            urutan += 1
            i += 1

    # proses transaksi
    tot_mkn = sum(list_total_mkn)
    tot_mnm = sum(list_total_mnm)
    tot = tot_mkn + tot_mnm
    print("\n-> Total Harga      :", uang(tot))
    print("---------------------------------------")
    bayar = inputangka_bayar(">> Uang Pembayaran  : ")

    if(bayar < tot):
        while(bayar < tot):
            print("\n\nWARNING!! : Uang Pembayaran Masih Kurang\n")
            bayar = inputangka_bayar(">> Uang Pembayaran  : ")

            if(bayar >= tot):
                kembalian = bayar - (tot_mkn + tot_mnm)
                break
            else:
                pass
    else:
        kembalian = bayar - (tot_mkn + tot_mnm)

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

    # print hasil transaksi ke layar
    print("+========== PRINT PEMBAYARAN =========+\n")
    print("-> Jumlah Makanan :", sum(list_qty_mkn), "Makanan")
    print("-> Jumlah Minuman :", sum(list_qty_mnm), "Minuman")
    print("---------------------------------------\n")

    if(mkn == True):
        urutan = 1
        i = 0
        print("-> Daftar Makanan")
        while(i < i_mkn):
            time.sleep(0.7)
            print()
            print("    ========= LIST MAKANAN (" + str(urutan) + ") ========")
            print("    Nama Makanan  :", list_makanan[i])
            print("    Harga         :", uang(list_harga_mkn[i]), "Per Porsi")
            print("    Kuantitas     :", list_qty_mkn[i], "Porsi")
            total = list_harga_mkn[i] * list_qty_mkn[i]
            print("    Total         :", uang(total))
            print("    -----------------------------------")
            list_total_mkn[i]
            urutan += 1
            i += 1

    if(mnm == True):
        urutan = 1
        i = 0
        print("\n-> Daftar Minuman")
        while(i < i_mnm):
            time.sleep(0.7)
            print()
            print("    ========= LIST MINUMAN (" + str(urutan) + ") ========")
            print("    Nama Minuman  :", list_minuman[i])
            print("    Harga         :", uang(list_harga_mnm[i]), "Per Gelas")
            print("    Kuantitas     :", list_qty_mnm[i], "Gelas")
            total = list_harga_mnm[i] * list_qty_mnm[i]
            print("    Total         :", uang(total))
            print("    -----------------------------------")
            list_total_mnm[i]
            urutan += 1
            i += 1

    time.sleep(0.7)
    print("\n---------------------------------------")
    print("-> Total Harga    :", uang(tot))
    print("-> Pembayaran     :", uang(bayar))
    print("-> Kembalian      :", uang(kembalian))
    print("\n+============ TERIMA KASIH ===========+\n")

    # print resi transaksi pembayaran
    resi_transaksi()

    # inputan jika user ingin mengulang program
    ulang = inputpilihan(">> Transaksi Ulang [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
    else:
        break

# akhir program
print("\n+======= PROGRAM TELAH BERAKHIR ======+")
