def transfer():
    pass

def withdraw():
    rek = input("Masukkan no rekening anda : ")
    cash = input("Masukkan jumlah uang : ")

def deposit():
    rek = input("Masukkan no rekening anda : ")
    cash = input("Masukkan jumlah uang : ")

def new_rek():
    name = input("Masukkan nama anda : ")
    cash = input("Masukkan rekening awal anda : ")

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
        new_rek()
        tanya()
    elif pilih == 2:
        print("Setoran tunai")
    elif pilih == 3:
        print("Tarik tunai")
    elif pilih == 4:
        print("Transfer")
    elif pilih == 5:
        print("Lihat daftar")
    elif (pilih == 6):
        ans = input("Yakin ingin keluar? (y/n) : ")
        if ans == 'y':
            print("Terima kasih")
        elif ans == 'n':
            tanya()
        else:
            print("Input anda salah")
            tanya()
    else:
        print("Masukkan yang anda masukkan salah")

tanya()