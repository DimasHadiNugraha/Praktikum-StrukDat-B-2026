class Mole:
    def __init__(self,explane,goldlane,midlane):
        self.explane = explane
        self.godlane = goldlane
        self.midlane = midlane
    
    def tampilkan_hero(self):
        print(f"'explane'{ self.explane}'goldlane' {self.godlane}'midlane'{self.midlane}")
    
    def ubah_hero(self,hero):
        self.explane = hero
    
mole1 = Mole("gatot","miya","nana")
mole2 = Mole("nana","miya","nana")
mole3 = Mole("parsa","valen","saber")


mole1.tampilkan_hero()
mole2.tampilkan_hero()
mole2.ubah_hero('arlot')
mole2.tampilkan_hero()
