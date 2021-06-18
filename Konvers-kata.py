kata = input("\n>> Masukkan Kata : ")
array_kata = kata.split(" ")
list_kata = []
kosa_kota = ["di","ke","dari","dalam","yaitu","ada","dan"]
panjang_kata = len(array_kata)

i = 0
while(i < panjang_kata):

    if(array_kata[i] in kosa_kota):
        list_kata.append(array_kata[i])
        i += 1
        continue
    cek_kata = array_kata[i].istitle()
    if(cek_kata == False):
        konvers = array_kata[i].capitalize()
        list_kata.append(konvers)
        i += 1
    else:
        break

hasil = " ".join(list_kata)
print("\nHasil :",hasil)