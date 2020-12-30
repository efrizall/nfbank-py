def transfer():
    pass

def withdraw():
    pass

def deposit():
    pass

def new_rek():
    pass

def tanya():
    print("[1] Buka Rekening")
    print("[2] Setoran Tunai")
    print("[3] Tarik Tunai")
    print("[4] Transfer")
    print("[5] Lihat Daftar Transfer")
    print("[6] Keluar")

    pilih = int(input("Masukkan pilihan anda : "))

    if pilih == 1:
        print("Buka rekening")
    elif pilih == 2:
        print("Setoran tunai")
    elif pilih == 3:
        print("Tarik tunai")
    elif pilih == 4:
        print("Transfer")
    elif pilih == 5:
        print("Lihat daftar")
    elif (pilih == 6):
        print("Yakin ingin keluar?")
    else:
        print("Masukkan yang anda masukkan salah")

tanya()
new_rek()