from os import system, __name__
import time

def inputangka(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan No Daftar Menu : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan

def inputangka_mkn(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan Jumlah Porsi : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan

def inputangka_mnm(pesan):
    while True:
        try:
            pesan = int(input(">> Masukkan Jumlah Kuantitas : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan

def inputangka_bayar(pesan):
    while True:
        try:
            pesan = int(input(">> Uang Pembayaran  : "))
        except:
            print("\nWARNING!! : Masukkan Inputan Hanya Berupa Angka\n")
        else:
            return pesan

def inputmakanan(pesan):
    while(pesan != "a" and pesan != "b" and pesan != "c" and pesan != "d" and pesan != "e" and pesan != "f"):
        ulang = input(">> Masukkan Kode Makanan : ")

        if(ulang == "a" or ulang == "b" or ulang == "c" or ulang == "d" or ulang == "e" or ulang == "f"):
            return ulang
        else:
            print("\nWARNING : Masukkan Inputan Sesuai Pilihan Menu\n")
            pass

def inputminuman(pesan):
     while(pesan != "a" and pesan != "b" and pesan != "c" and pesan != "d" and pesan != "e"):
        ulang = input(">> Masukkan Kode Minuman     : ")

        if(ulang == "a" or ulang == "b" or ulang == "c" or ulang == "d" or ulang == "e"):
            return ulang
        else:
            print("\nWARNING : Masukkan Inputan Sesuai Pilihan Menu\n")
            pass

def inputpilihan(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input(">> Transaksi Ulang [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!\n")
            pass

def inputpilihan_mkn(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Pilih Menu Makanan Kembali [Y/T]     : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!")
            pass

def inputpilihan_mnm(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!")
            pass

def inputtambahan_mkn(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Ingin Menambahkan Menu Makanan [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!")
            pass

def inputtambahan_mnm(pesan):
      while(pesan != "Y" and pesan != "y" and pesan != "T" and pesan != "t"):
        ulang = input("\n>> Ingin Menambahkan Menu Minuman [Y/T] : ")

        if(ulang == "Y" or ulang == "y" or ulang == "T" or ulang == "t"):
            return ulang
        else:
            print("\nWARNING : Masukkan Input Perintah Berupa [Y/T]!!")
            pass

def uang(nilai):
    x = str(nilai)

    if(len(x) <= 3):
        return "Rp. " + x
    else:
        a = x[:-3]
        b = x[-3:]
        return uang(a) + "." + b

def resi_transaksi():

    resi = open("Resi-Transaksi.txt","w")

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
            resi.write("    ========= LIST MAKANAN (" + str(urutan) + ") ========\n")
            resi.write("    Nama Barang   : " + str(list_makanan[i]) + "\n")
            resi.write("    Harga         : " + uang(list_harga_mkn[i]) + " Per Porsi\n")
            resi.write("    Kuantitas     : " + str(list_qty_mkn[i]) + " Porsi\n")
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
            resi.write("    ========= LIST MINUMAN (" + str(urutan) + ") ========\n")
            resi.write("    Nama Barang   : " + str(list_minuman[i]) + "\n")
            resi.write("    Harga         : " + str(uang(list_harga_mnm[i])) + " Per Gelas\n")
            resi.write("    Kuantitas     : " + str(list_qty_mnm[i]) + " Gelas\n")
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

while True:

    _ = system('cls')

    print()
    print("+=========== DAFTAR MENU KANTIN FTI ===========+")
    print("|----------------------------------------------|")
    print("|                                              |")
    print("| PETUNJUK PEMESANAN     :                     |")
    print("|                                              |")
    print("| 1). Ketik 1 Untuk Memilih Menu Makanan       |")
    print("| 2). Ketik 2 Untuk Memilih Menu Minuman       |")
    print("|                                              |")
    print("|----------------------------------------------|")
    print("+==============================================+")
    print()

    makanan        = ["Nasi Goreng","Lontong Goreng","Bakso Goreng","Rujak Goreng","Rujak Bakso Pecel"]
    harga_mkn      = [15000,14900,12900,13000,15000,17000]
    kode_mkn       = ["a","b","c","d","e","f"]
    list_makanan   = []
    list_harga_mkn = []
    list_qty_mkn   = []
    list_total_mkn = []
    list_kode_mkn  = []
    qty_mkn        = 0
    mkn            = False

    minuman        = ["Teh Dingin/Panas","Kopi Dingin","Kopi Teh Panas","Coca-Cola Dingin","Coca-Cola Panas"]
    harga_mnm      = [2500,5000,6500,3500,5000]
    kode_mnm       = ["a","b","c","d","e"]
    list_minuman   = []
    list_harga_mnm = []
    list_qty_mnm   = []
    list_total_mnm = []
    list_kode_mnm  = []
    qty_mnm        = 0
    mnm            = False 


    ipt_menu = inputangka(">> Masukkan No Daftar Menu : ")

    while(ipt_menu <= 0 or ipt_menu >= 3):
        print("\nWARNING!! : Masukkan Inputan Sesuai Pilihan Menu\n")
        ipt_menu = inputangka(">> Masukkan No Daftar Menu : ")

        if(ipt_menu > 0 and ipt_menu < 3):
            break
        else:
            pass

    _ = system("cls")

    if(ipt_menu == 1):

        mkn = True
        urutan = 1
        i_mkn = 0
        sts = True
        while (sts == True):

            daftar_makanan()
            ipt_makanan  = inputmakanan(">> Masukkan Kode Makanan : ")

            x = ipt_makanan in list_kode_mkn
            while(x == True):
                print("\nWARNING!! : Makanan Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Makanan yang Lain\n")
                inpt_kode   = inputmakanan(">> Masukkan Kode Makanan : ")

                x = inpt_kode in list_kode_mkn
                if(x == False):
                    break
                else:
                    continue

            qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")
            
            while(qty_mkn <= 0):
                print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")

                if(qty_mkn > 0):
                    break
                else:
                    pass

            no_index = kode_mkn.index(ipt_makanan)
            list_makanan.append(makanan[no_index])
            list_harga_mkn.append(harga_mkn[no_index])
            list_kode_mkn.append(ipt_makanan)

            time.sleep(0.7)
            print("\n\n+=========== LIST MAKANAN",urutan,"===========+")
            print(">> Nama Makanan  :",makanan[no_index])
            print(">> Harga         :",uang(harga_mkn[no_index]),"Per Porsi")
            print(">> Kuantitas     :",qty_mkn,"Porsi")
            print("----------------------------------------")
            total_biaya_mkn = qty_mkn * harga_mkn[no_index]
            print(">> Total Harga  :",uang(total_biaya_mkn))
            print()
            list_total_mkn.append(total_biaya_mkn)
            list_qty_mkn.append(qty_mkn)
            i_mkn += 1
            i_mnm = 0
            urutan += 1

            pilihan_mkn = inputpilihan_mkn("\n>> Pilih Menu Makanan Kembali [Y/T]     : ")
            if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                sts = True
                time.sleep(0.7)
                _ = system('cls')
            else:
                pilihan_mnm = inputtambahan_mnm("\n>> Ingin Menambahkan Menu Minuman [Y/T] : ")
                if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                    _ = system('cls')

                    mnm = True
                    urutan = 1
                    i_mnm = 0
                    sts = True
                    while(sts == True):

                        daftar_minuman()
                        ipt_minuman  = inputminuman(">> Masukkan Kode Minuman     : ")

                        x = ipt_minuman in list_kode_mnm
                        while(x == True):
                            print("\nWARNING!! : Minuman Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Minuman yang Lain\n")
                            ipt_minuman   = inputminuman(">> Masukkan Kode Minuman     : ")

                            x = ipt_minuman in list_kode_mnm
                            if(x == False):
                                break
                            else:
                                continue

                        qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")

                        while(qty_mnm <= 0):
                            print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                            qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")

                            if(qty_mnm > 0):
                                break
                            else:
                                pass

                        no_index = kode_mnm.index(ipt_minuman)
                        list_minuman.append(minuman[no_index])
                        list_harga_mnm.append(harga_mnm[no_index])
                        list_kode_mnm.append(ipt_minuman)

                        time.sleep(0.7)
                        print("\n\n+=========== LIST MINUMAN",urutan,"===========+")
                        print(">> Nama Makanan  :",minuman[no_index])
                        print(">> Harga         :",uang(harga_mnm[no_index]),"Per Gelas")
                        print(">> Kuantitas     :",qty_mnm,"Gelas")
                        print("----------------------------------------")
                        total_biaya_mnm = qty_mnm * harga_mnm[no_index]
                        print(">> Total Harga  :",uang(total_biaya_mnm))
                        print()
                        list_total_mnm.append(total_biaya_mnm)
                        list_qty_mnm.append(qty_mnm)
                        i_mnm += 1
                        urutan += 1

                        pilihan_mnm = inputpilihan_mnm("\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

                        if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                            sts = True
                            time.sleep(0.7)
                            _ = system('cls')
                        else:
                            sts = False
                else:
                    break        

    else:

        mnm = True
        urutan = 1
        i_mnm = 0
        sts = True
        while(sts == True):

            daftar_minuman()
            ipt_minuman  = inputminuman(">> Masukkan Kode Minuman     : ")

            x = ipt_minuman in list_kode_mnm
            while(x == True):
                print("\nWARNING!! : Minuman Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Minuman yang Lain\n")
                ipt_minuman   = inputminuman(">> Masukkan Kode Minuman     : ")

                x = ipt_minuman in list_kode_mnm
                if(x == False):
                    break
                else:
                    continue

            qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")
            
            while(qty_mnm <= 0):
                print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                qty_mnm = inputangka_mnm(">> Masukkan Jumlah Kuantitas : ")

                if(qty_mnm > 0):
                    break
                else:
                    pass

            no_index = kode_mnm.index(ipt_minuman)
            list_minuman.append(minuman[no_index])
            list_harga_mnm.append(harga_mnm[no_index])
            list_kode_mnm.append(ipt_minuman)

            time.sleep(0.7)
            print("\n\n+=========== LIST MINUMAN",urutan,"===========+")
            print(">> Nama Makanan  :",minuman[no_index])
            print(">> Harga         :",uang(harga_mnm[no_index]),"Per Gelas")
            print(">> Kuantitas     :",qty_mnm,"Gelas")
            print("----------------------------------------")
            total_biaya_mnm = qty_mnm * harga_mnm[no_index]
            print(">> Total Harga  :",uang(total_biaya_mnm))
            print()
            list_total_mnm.append(total_biaya_mnm)
            list_qty_mnm.append(qty_mnm)
            i_mnm += 1
            i_mkn = 0
            urutan += 1

            pilihan_mnm = inputpilihan_mnm("\n>> Pilih Menu Minuman Kembali [Y/T]     : ")

            if(pilihan_mnm == "Y" or pilihan_mnm == "y"):
                sts = True
                time.sleep(0.7)
                _ = system('cls')
            else:
                pilihan_mkn = inputtambahan_mkn("\n>> Ingin Menambahkan Menu Makanan [Y/T] : ")
                if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                    _ = system('cls')

                    mkn = True                    
                    urutan = 1
                    i_mkn = 0
                    sts = True
                    while(sts == True):

                        daftar_makanan()
                        ipt_makanan  = inputmakanan(">> Masukkan Kode Makanan : ")

                        x = ipt_makanan in list_kode_mkn
                        while(x == True):
                            print("\nWARNING!! : Makanan Tersebut Telah Terdaftar Di List Anda, Silahkan Pilih Makanan yang Lain\n")
                            inpt_kode   = inputmakanan(">> Masukkan Kode Makanan : ")

                            x = inpt_kode in list_kode_mkn
                            if(x == False):
                                break
                            else:
                                continue

                        qty_mkn = inputangka_mkn(">> Masukkan Jumlah Porsi : ")

                        while(qty_mkn <= 0):
                            print("\nWARNING!! : Masukkan Inputan Harus >= 0\n")
                            qty_mkn= inputangka_mkn(">> Masukkan Jumlah Porsi : ")

                            if(qty_mkn > 0):
                                break
                            else:
                                pass

                        no_index = kode_mkn.index(ipt_makanan)
                        list_makanan.append(makanan[no_index])
                        list_harga_mkn.append(harga_mkn[no_index])
                        list_kode_mkn.append(ipt_makanan)

                        time.sleep(0.7)
                        print("\n\n+=========== LIST MAKANAN",urutan,"===========+")
                        print(">> Nama Makanan  :",makanan[no_index])
                        print(">> Harga         :",uang(harga_mkn[no_index]),"Per Porsi")
                        print(">> Kuantitas     :",qty_mkn,"Porsi")
                        print("----------------------------------------")
                        total_biaya_mkn = qty_mkn * harga_mkn[no_index]
                        print(">> Total Harga  :",uang(total_biaya_mkn))
                        print()
                        list_total_mkn.append(total_biaya_mkn)
                        list_qty_mkn.append(qty_mkn)
                        i_mkn += 1
                        urutan += 1

                        pilihan_mkn = inputpilihan_mkn("\n>> Pilih Menu Makanan Kembali [Y/T]     : ")

                        if(pilihan_mkn == "Y" or pilihan_mkn == "y"):
                            sts = True
                            time.sleep(0.7)
                            _ = system('cls')
                        else:
                            sts = False
                else:
                    break
    
    _ =  system('cls')

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
            print("    Nama Barang     :",list_makanan[i])
            print("    Harga           :",uang(list_harga_mkn[i]),"Per Porsi")
            print("    Kuantitas       :",list_qty_mkn[i],"Porsi")
            total = list_harga_mkn[i] * list_qty_mkn[i]
            print("    Total           :",uang(total))
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
            print("    LIST MINUMAN (" + str(urutan) + ")")
            print("    -----------------------------------")
            print("    Nama Barang     :",list_minuman[i])
            print("    Harga           :",uang(list_harga_mnm[i]),"Per Gelas")
            print("    Kuantitas       :",list_qty_mnm[i],"Gelas")
            total = list_harga_mnm[i] * list_qty_mnm[i]
            print("    Total           :",uang(total))
            print("    -----------------------------------")
            list_total_mnm[i]
            urutan += 1
            i += 1

    tot_mkn = sum(list_total_mkn)
    tot_mnm = sum(list_total_mnm)
    tot     = tot_mkn + tot_mnm 
    print("\n-> Total Harga      :",uang(tot))
    print("---------------------------------------")
    bayar = inputangka_bayar(">> Uang Pembayaran  : ")
    
    if(bayar < tot):
        while(bayar < tot):
            print("\nWARNING!! : Uang Pembayaran Masih Kurang\n")
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
    print("-> Jumlah Makanan :",sum(list_qty_mkn),"Makanan")
    print("-> Jumlah Minuman :",sum(list_qty_mnm),"Minuman")
    print("---------------------------------------\n")

    if(mkn == True):
        urutan = 1
        i = 0 
        print("-> Daftar Makanan")
        while(i < i_mkn):
            time.sleep(0.7)
            print()   
            print("    ========= LIST MAKANAN (" + str(urutan) + ") ========")
            print("    Nama Barang   :",list_makanan[i])
            print("    Harga         :",uang(list_harga_mkn[i]),"Per Porsi")
            print("    Kuantitas     :",list_qty_mkn[i],"Porsi")
            total = list_harga_mkn[i] * list_qty_mkn[i]
            print("    Total         :",uang(total))
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
            print("    Nama Barang   :",list_minuman[i])
            print("    Harga         :",uang(list_harga_mnm[i]),"Per Gelas")
            print("    Kuantitas     :",list_qty_mnm[i],"Gelas")
            total = list_harga_mnm[i] * list_qty_mnm[i]
            print("    Total         :",uang(total))
            print("    -----------------------------------")
            list_total_mnm[i]
            urutan += 1
            i += 1

    time.sleep(0.7)
    print("\n---------------------------------------")
    print("-> Total Harga    :",uang(tot))
    print("-> Pembayaran     :",uang(bayar))
    print("-> Kembalian      :",uang(kembalian))
    print("\n+============ TERIMA KASIH ===========+\n")

    # print resi transaksi pembayaran
    resi_transaksi() 

    ulang = inputpilihan(">> Transaksi Ulang [Y/T] : ")

    if(ulang == "Y" or ulang == "y"):
        True
    else:
        break

print("\n+======= PROGRAM TELAH BERAKHIR ======+")



         
