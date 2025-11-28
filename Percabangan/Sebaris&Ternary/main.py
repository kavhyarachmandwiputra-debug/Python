nilai = 100

if nilai >= 65:
    print("passed the exam")
else:
    print("below the passing exam")

#one line
if nilai >= 65: print("passed the exam")
if nilai < 65: print("Below the passing exam")

#Ternarry nilai balik
message = "passed the exam" if nilai >= 65 else "below passing the exam"
print(message)