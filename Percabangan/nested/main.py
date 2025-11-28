nilai = int(input("Inputkan nilai: "))

if nilai == 100:
    print("Sempurna")
elif nilai >= 85:
    print("Bagus")
elif nilai >= 65:
    print("Kamu lolos ujian")
    
    if nilai <= 70:
        print("Tapi kamu harus meningkatkannya")
    else:
        print("Dengan Nilai yang bagus")

else:
    print("Dibawah nilai kelulusan")