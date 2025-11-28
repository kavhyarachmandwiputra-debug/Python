nilai = int(input("Inputkan nilai: "))

if nilai == 100:
    print("Sempurna")
    print("Selamat Kamu Lolos Ujian!")
elif nilai >= 85:
    print("Bagus")
    print("Selamat Kamu Lolos Ujian!")
elif nilai >= 65:
    print("ok")
    print("Kamu Lolos Bersyarat")
else:
    print("Maaf Kamu Tidak Lolos")