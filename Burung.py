from Animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi 
    def cetak_burung(self):
        super().cetak()
        print("jenis \t\t: ", self.jenis, 
              "\nbunyi  \t\t: ", self.bunyi)
              
pipit = Burung("Pipit", "Jagung", "Darat", "Bertelur", "Gold Amadin", "Cip Cip Cip")
pipit.cetak_burung()

merpati = Burung("Merpati", "Biji-Bijian", "Darat", "Bertelur", "Karolina", "Kur Kur Kur")
merpati.cetak_burung()