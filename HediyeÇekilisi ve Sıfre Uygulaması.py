import random
import string
isimler = ["Duygu", "Ozge", "Önder", "Mert", "Ali", "Deniz"]

def Hediye_cekilisi():
    alanlar = isimler.copy()
    verenler = isimler.copy()
    
    while len(alanlar) > 0:
        alici_index = random.randint(0, len(alanlar) - 1)
        verici_index = random.randint(0, len(verenler) - 1)
        
        while alanlar[alici_index] == verenler[verici_index]:
            alici_index = random.randint(0, len(alanlar) - 1)
            verici_index = random.randint(0, len(verenler) - 1)
        
        print(alanlar[alici_index], "şu kişiye hediye alacak:", verenler[verici_index])
        
        del alanlar[alici_index]
        del verenler[verici_index]

Hediye_cekilisi()



rakamlar = "0123456789"
semboller = string.punctuation
kucuk_Harfler = string.ascii_lowercase
buyuk_harfler= string.ascii_uppercase
tum_karakterler = [rakamlar,semboller,kucuk_Harfler,buyuk_harfler]

sıfre = ""
for i in range(2):
     sıfre += tum_karakterler[0][random.randint(0, 9)]
     for i in range(2):
        sıfre += tum_karakterler[1][random.randint(0, 9)]

for i in range(2):
    sıfre += tum_karakterler[2][random.randint(0, 9)]
    for i in range(2):
        sıfre += tum_karakterler[3][random.randint(0, 9)]

print(sıfre)
    
