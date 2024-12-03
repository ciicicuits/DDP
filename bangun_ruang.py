import math
#deklarasi fungsi
def l_balok(p,l,t):
    hitung = 2*(p*l)+(p*t)+(l*t)
    print(f'Luas Balok Adalah {hitung}')

def l_kubus(sisi):
    hitung = 6*sisi*sisi
    print(f'Luas Kubus Adala {hitung}')

def l_tabung(r,t):
    hitung = 2*r+2*t
    print(f'Luas Tabung Adalah {hitung}')

def l_limas(luas,luassisi):
    hitung = luas + luassisi
    print(f'Luas Lima Adalah {hitung}')

def l_prisma_segitiga(luas,keliling,tinggi):
    hitung = 2*luas+keliling+tinggi
    print(f'Luas Prismasegitiga Adalah {hitung}')
    