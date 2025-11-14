from typing import final

# tipe konstanta PItidak ditentukan secara eksplisit,
# melainkan didapat dari tipe  data nilai
PI: final = 3.14

# tipe konstanta TOTAL_MONTH ditentukan secara explisit yaitu 'int'
TOTAL_MONTH: final[int] = 12

print("pi = %f, Total Bulan = %d" % (PI, TOTAL_MONTH))