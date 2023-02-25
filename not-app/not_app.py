def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    ogrenciAdı= (liste[0])
    Notlar = liste[1].split(',')
    not1 = int(Notlar[0])
    not2 = int(Notlar[1])
    not3 = int(Notlar[2])
    ortalama = (not1+not2+not3)/3
    if ortalama >=90 and ortalama<=100:
        harf = "AA"
    elif ortalama >= 85 and ortalama<=89:
        harf ="BA"
    elif ortalama >= 65:
        harf ="CC"
    else:
        harf ="FF"
    return ogrenciAdı + ": " + harf + "\n"
    

def read_ort():
    with open("sınav_notları.txt","r",encoding="utf-8") as notes:
        for satir in notes:
            print(not_hesapla(satir))


def enter_not():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = input("NOT 1: ")
    not2 = input("NOT 2: ")
    not3 = input("NOT 3: ")

    with open("sınav_notları.txt","a",encoding="utf-8") as notes:
        notes.write(ad+ " "+ soyad+ ":"+not1+","+not2+","+not3+"\n")

    
def not_kayıt():
    with open("sınav_notları.txt", "r", encoding="utf-8") as notes:
        liste=[]
        for i in notes:
          liste.append(not_hesapla(i))

        with open("sonuçlar.txt","w",encoding="utf-8") as notes1:
            for i in liste:
                notes1.write(i)
                break











while True:
    işlem = input("1-Notları oku\n2-Not gir\n3-Okunan notları kaydet\n4-Çıkış\n")
    if işlem =="1":
        read_ort()
    elif işlem =="2":
        enter_not()  
    elif işlem =="3":
        not_kayıt()
    else:
        break