nilai = int(input("Inputkan nilai: "))
nilaiSebelum = int(input("Inpukan nilai sebelumya: "))

if nilai >= 90 and nilaiSebelum >= 65:
    print("Bagus")
    if nilai >= 90 and nilaiSebelum < 65:
        print("Bagus, kamu telah bekerja keras, kan?")
    elif nilai >= 65:
        print("Kamu lulus ujian")
    else:
        print("Dibawah nilai kelulusan")

if (niali >= 65 and not nilaiSebelum >= 65) or(not nilai >= 65 and nilaiSebelum >=65):
    print ("Setidaknya kamu lolos 1 ujian. Kerja Bagus!")