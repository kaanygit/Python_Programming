#class and objects

# Sınıf özellikleri tanımlama - 1
class Araba:
    #sınıf özellikleri
    marka="template marka"
    model="template model"
    yakit="template yakit tipi"
    
    def calistir(self):
        print(f"{self.marka} {self.model} çalıştırıldı")
        
    def durdur(self):
        print(f"{self.marka} {self.model} {self.yakit} yakit tipli arac durduruldu")
        
araba1=Araba()
araba2=Araba()

araba1.marka="Toyota"
araba1.model="Corolla"
araba1.yakit="Dizel"

araba2.marka="Bmw"
# araba2.model="m5"
araba2.yakit="Dizel"


araba1.calistir()
araba2.calistir()

araba1.durdur()
araba2.durdur()

print("**************")

# Sınıf özellikleri tanımlama - 1
class ArabaType2:
    
    #__init__ adlı özel bir metot, bir nesne oluşturulduğunda otomatik olarak çağrılır ve başlangıç 
    # değerlerini ayarlamak için kullanılır.
    def __init__(self,marka,model,yakit_tipi):
        self.marka=marka
        self.model=model
        self.yakit_tipi=yakit_tipi
        
    def calistir(self):
        print(f"{self.marka} {self.model} calistirildi")
        
    def durdur(self):
        print(f"{self.marka} {self.model} {self.yakit_tipi} yakit tipli arac duduruldu")
        

car1=ArabaType2("Mercedes","C-180","Dizel")
car2=ArabaType2("Bmw","M6","Benzin")


car1.calistir()
car1.durdur()

car2.calistir()
car2.durdur()