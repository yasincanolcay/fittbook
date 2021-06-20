
import tkinter
from tkinter import *
import time
from time import sleep
import datetime
import random
from threading import Thread






#ideal kalori hesaplama math
#66+(13.75*kilo)+(5*boy)+(6.8*yas)=66+1375+940-183.6 = sonuc
#dwnd = PhotoImage(file='fitbook.png')
#Button(master, image=dwnd, command=None,relief=FLAT,bg="white",activebackground="darkslategrey").pack(pady=10)


#------uye kayıt fonksiyonu-------#

def uye_kaydi():
    mesaj=""
    l_aciklama["font"] = "Verdana 12 bold"
    
    
        
    try:


        isim = e_isim.get()
        soyisim = e_soyisim.get()
        yas = e_yas.get()
        kilo_kilo = int(e_kilo.get())
        Eboy = float(e_boy.get())
        uyelik_id = random.randint(1,10000000)
        uyelik_id2 = random.randint(1,2000000)
        id = uyelik_id + uyelik_id2

        boy = e_boy.get()
        kilo = e_kilo.get()
        l_bilgi["text"] = "İSİM:  {}   SOYİSİM:  {}   YAŞ: {}  \t BOY: {} / KİLO: {}".format(isim,soyisim,yas,boy,kilo)
        kalori = (1*kilo_kilo)*24
        if var.get():
            if e_isim.get() and e_soyisim.get() and e_kilo.get() and e_boy.get() and e_yas.get():
                
                
                if var.get()==1:

                    master["bg"] = "black"
                    #kilo kontrol      
                    endeks  = kilo_kilo/(Eboy*Eboy)
                    durum = ""
                    zayif = ""
                    ideal = ""
                    kilolu = ""
                    obez = ""
                    ciddi_obez = ""
                    aciklama=""
                    tavsiyeler = ""
                    kayit = datetime.datetime.now()
                    sonkayit["text"] = "Son Kayıt\n{}".format(kayit)

                    if endeks <18:
                        durum+="İdeal kilonuzun altındasınız\nDurum: zayıf\nDiyet programına göz atın"
                        zayif+="isim: {} - durum: zayif uye\n".format(isim)
                        zayif_uye = open("zayif.txt","a")
                        zayif_yaz = zayif_uye.write(zayif)
                        zayif_uye.close()
                        kilo_al = kalori + 650
                        aciklama += """
Merhaba {} görünüşe göre ideal kilonuzun altındasınız\nama endişelenmeyin fitbook herzaman yanınızda\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo almak için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 100-200 \nkalori arttırabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_al)
                        l_aciklama["text"] = aciklama
                        def kiloal():
                            dosya = open("kilo_al","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                kiloal_yaz = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,kiloal_yaz,"style")

                        kl = Thread(target=kiloal)
                        kl.start()

                    elif endeks >= 18 and endeks <25 :
                        durum+="Kilonuz Normal\nDurum: mükemmel\nDiyet yapmanıza gerek yok"
              
                        ideal+="isim: {} - durum: Mükemmel\n".format(isim)
                        ideal_uye = open("ideal.txt","a")
                        ideal_yaz = ideal_uye.write(ideal)
                        ideal_uye.close()
                      
                        aciklama += """
Merhaba {} kilonuz tamamen normal\nsizin için herhangi bir diyet tablosu oluşturmadık\n
ideal kilonuzu korumanız için bir kaç tavsiyemiz var.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\n
Saglıklı beslenmeye ve hareket etmeye özen göstererek\nideal kilonuzu koruyabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori)
                        l_aciklama["text"] = aciklama
                        tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                        tavsiye_alani.insert(END,durum,"style")
                    elif endeks >= 25 and endeks <30:
                        durum+="İdeal kilonuzun üstündesiniz\nDurum: kilolu\nDiyet programına göz atmanızı tavsiye ederiz"
                        
                        kilolu+="isim: {} - durum: kilolu\n".format(isim)
                        kilolu_uye = open("kilolu.txt","a")
                        kilolu_yaz = kilolu_uye.write(kilolu)
                        kilolu_uye.close()
                        kilo_ver = kalori - 400

                        aciklama += """
Merhaba {} görünüşe göre fazla kilolarınız var\nama endişelenmeyin fitbook olarak size tavsiyelerimiz var\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 200-300 kalori azaltabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver)
                        l_aciklama["text"] = aciklama
                        def tavsiye():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz,"style")

                        tv = Thread(target=tavsiye)
                        tv.start()


                      


                    


                    elif endeks >= 30 and endeks <35:
                        durum+="İdeal kilonuzun çok üstünde\nDurum: obez\nDiyet programına göz atarak\nkilolardan kurtulun"
            
                        obez+="isim: {} - durum: obez\n".format(isim)
                        obez_uye = open("obez.txt","a")
                        obez_yaz = obez_uye.write(obez)
                        obez_uye.close()
                        kilo_ver2 = kalori - 650

                        aciklama += """
Merhaba {} görünüşe göre obez sınıfındasınız\nama endişelenmeyin fitbook herzaman yanınızda\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 300-500 kalori azaltabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver2)
                        l_aciklama["text"] = aciklama
                        def tavsiye2():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz2 = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz2,"style")

                        tv2 = Thread(target=tavsiye2)
                        tv2.start()
                
                    else:
                        durum+="İdeal kilonuzun çok çok üstü\nDurum: ciddi obezite\nAcilen Diyet Programına Göz Atın!"
                      
                        ciddi_obez+="isim: {} - durum: ciddi obez\n".format(isim)
                        ciddi_uye = open("ciddi_obez.txt","a")
                        ciddi_yaz = ciddi_uye.write(ciddi_obez)
                        ciddi_uye.close()
                
                        kilo_ver3 = kalori - 700

                        aciklama += """
Merhaba {} görünüşe göre ciddi obez sınıfındasınız\nama endişelenmeyin fitbook da çözümler bitmez\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 400-600 kalori azaltablirsiniz\nsize güveniyoruz ve inanıyoruz 
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver3)
                        l_aciklama["text"] = aciklama
                        def tavsiye3():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz3 = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz3,"style")

                        tv3 = Thread(target=tavsiye3)
                        tv3.start()

                    
                    tablo = """
*****************************************************************
üye ismi: {}
üye soyisim: {}
yaş : {}
kilo : {}
boy: {}
cinsiyet: erkek

durum: {}

uyelik kimligi: {}

©fitbook - olcaysoftware



*****************************************************************
            
                    """.format(isim,soyisim,yas,kilo_kilo,Eboy,durum,id)

                    uye_dosyasi = open("fittbook_uye.txt","a")
                    uye_dosyasi.write(tablo)
                    uye_dosyasi.close()

                    uye_isimleri = open("uyelikler.txt","a")
                    yaz = "uye : {} {}  - cinsiyet: erkek\n".format(isim,soyisim)
                    yazdir = uye_isimleri.write(yaz)
                    uye_isimleri.close()
                    
                    erkek = open("erkek.txt","a")
                    erkek.write(yaz)
                    erkek.close()
                    #-----
                    with open("uyelikler.txt", "r") as f:
                          uye_sayisi = f.read().count("\n")
                          uye_str = "Toplam Üyeler\n{}".format(str(uye_sayisi))
                          toplam_str = "Toplam Kaydetme\n{}".format(str(uye_sayisi))

                          toplam_uye["text"] = uye_str
                          toplam_uye2["text"] = uye_str
                          toplam_kayit["text"] = toplam_str
                          


                    #-------------------#
                    with open("ciddi_obez.txt", "r") as c:
                      uye_sayisi_c = c.read().count("\n")
                      uye_str_c = "Ciddi Obez üyeler\n{}".format(str(uye_sayisi_c))
                      ciddi_obez_sayisi["text"] = uye_str_c

                    with open("obez.txt", "r") as o:
                      uye_sayisi_o = o.read().count("\n")
                      uye_str_o = "Obez üyeler\n{}".format(str(uye_sayisi_o))
                      obez_uye_sayisi["text"] = uye_str_o


                    with open("kilolu.txt", "r") as k:
                      uye_sayisi_k = k.read().count("\n")
                      uye_str_k = "Kilolu üyeler\n{}".format(str(uye_sayisi_k))
                      kilolu_uye_sayisi["text"] = uye_str_k


                    with open("zayif.txt", "r") as z:
                      uye_sayisi_z = z.read().count("\n")
                      uye_str_z = "Zayıf üyeler\n{}".format(str(uye_sayisi_z))
                      zayif_uye_sayisi["text"] = uye_str_z


                    with open("ideal.txt", "r") as ideal:
                      uye_sayisi_ideal = ideal.read().count("\n")
                      uye_str_ideal = "İdeal Kilolu üyeler\n{}".format(str(uye_sayisi_ideal))
                      ideal_uye_sayisi["text"] = uye_str_ideal
                    

                    with open("erkek.txt", "r") as erkek:
                      erkekuye = erkek.read().count("\n")
                      erkek_str = "Erkek üyeler\n{}".format(str(erkekuye))
                      lerkek["text"] = erkek_str
               
                    
                    def d2():
                        person = PhotoImage(file="person_50px.png")
                        cinsiyet_ek["image"] = person

                        
                        for i in range(1):
                            kayit_sonucu2["text"] = "lütfen bekleyin"
                            load1 = PhotoImage(file="load1.png")
                            kayit_sonucu["image"] = load1
                            sleep(1)
                            load2 = PhotoImage(file="load2.png")
                            kayit_sonucu["image"] = load2
                            sleep(1)
                            load3 = PhotoImage(file="load3.png")
                            kayit_sonucu["image"] = load3
                            sleep(1)
                            load4 = PhotoImage(file="load4.png")
                            kayit_sonucu["image"] = load4
                            sleep(1)
                            kayit_succes = PhotoImage(file="kayit_succes.png")
                            kayit_sonucu["image"] = kayit_succes
                            kayit_sonucu2["text"] = "uye kaydedildi"
                            sleep(10)
                            kayit_sonucu2["text"] = ""
                           
         
      
          



                    t2 = Thread(target=d2)
                    t2.start()
                    
                      #loading efekti
                    def d3():
                        
    
                        for i in range(1):
                            l_load1 = PhotoImage(file="label_load1.png")
                            l_load["image"] = l_load1
                            sleep(1)
                            l_load2 = PhotoImage(file="label_load2.png")
                            l_load["image"] = l_load2
                            sleep(1)
                            l_load3 = PhotoImage(file="label_load3.png")
                            l_load["image"] = l_load3
                            sleep(1)
                            l_load4 = PhotoImage(file="label_load4.png")
                            l_load["image"] = l_load4
                            sleep(1)
                            l_load5 = PhotoImage(file="label_load5.png")
                            l_load["image"] = l_load5
                            sleep(15)
                       
                           
         
      
          



                    t3 = Thread(target=d3)
                    t3.start()

                
                if var.get()==2:

                    #kilo kontrol
                    master["bg"] = "violet"
                    
                    
              
                    endeks  = kilo_kilo/(Eboy*Eboy)
                    durum = ""
                    obez = ""
                    ciddi_obez = ""
                    kilolu = ""
                    zayif = ""
                    ideal = ""
                    aciklama=""
                    kayit = datetime.datetime.now()
                    sonkayit["text"] = "Son Kayıt\n{}".format(kayit)

                    if endeks <18:
                        durum+="İdeal kilonuzun altındasınız\nDurum: zayıf\nDiyet programına göz atın"
                        zayif+="isim: {} - durum: zayif uye\n".format(isim)
                        zayif_uye = open("zayif.txt","a")
                        zayif_yaz = zayif_uye.write(zayif)
                        zayif_uye.close()
                        kilo_al = kalori + 650
                        

                        aciklama += """
Merhaba {} görünüşe göre ideal kilonuzun altındasınız\nama endişelenmeyin fitbook herzaman yanınızda\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo almak için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 100-200 kalori arttırabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_al)
                        l_aciklama["text"] = aciklama
                        def kiloal():
                            dosya = open("kilo_al","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                kiloal_yaz = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,kiloal_yaz,"style")

                        kl = Thread(target=kiloal)
                        kl.start()
                    elif endeks >= 18 and endeks <25 :
                        durum+="Kilonuz Normal\nDurum: mükemmel\nDiyet yapmanıza gerek yok"
              
                        ideal+="isim: {} - durum: Mükemmel\n".format(isim)
                        ideal_uye = open("ideal.txt","a")
                        ideal_yaz = ideal_uye.write(ideal)
                        ideal_uye.close()
                        
                        aciklama += """
Merhaba {} kilonuz tamamen normal\nsizin için herhangi bir diyet tablosu oluşturmadık\n
ideal kilonuzu korumanız için bir kaç tavsiyemiz var.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\n
Saglıklı beslenmeye ve hareket etmeye özen göstererek\nideal kilonuzu koruyabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori)
                        l_aciklama["text"] = aciklama
                        tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                        tavsiye_alani.insert(END,durum,"style")
                    elif endeks >= 25 and endeks <30:
                        durum+="İdeal kilonuzun üstündesiniz\nDurum: kilolu\nDiyet programına göz atmanızı tavsiye ederiz"
                        
                        kilolu+="isim: {} - durum: kilolu\n".format(isim)
                        kilolu_uye = open("kilolu.txt","a")
                        kilolu_yaz = kilolu_uye.write(kilolu)
                        kilolu_uye.close()
                        kilo_ver = kalori - 400
                        
                        aciklama += """
Merhaba {} görünüşe göre fazla kilolarınız var\nama endişelenmeyin fitbook olarak size tavsiyelerimiz var\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 200-300 kalori azaltabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver)
                        l_aciklama["text"] = aciklama
                        def tavsiye():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz,"style")

                        tv = Thread(target=tavsiye)
                        tv.start()

                    elif endeks >= 30 and endeks <35:
                        durum+="İdeal kilonuzun çok üstünde\nDurum: obez\nDiyet programına göz atarak\nkilolardan kurtulun"
            
                        obez+="isim: {} - durum: obez\n".format(isim)
                        obez_uye = open("obez.txt","a")
                        obez_yaz = obez_uye.write(obez)
                        obez_uye.close()
                        kilo_ver2 = kalori - 650
                        
                        aciklama += """
Merhaba {} görünüşe göre obez sınıfındasınız\nama endişelenmeyin fitbook herzaman yanınızda\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 300-500 kalori azaltabilirsiniz
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver2)
                        l_aciklama["text"] = aciklama
                        def tavsiye2():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz2 = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz2,"style")

                        tv2 = Thread(target=tavsiye2)
                        tv2.start()
                
                    else:
                        durum+="İdeal kilonuzun çok çok üstü\nDurum: ciddi obezite\nAcilen Diyet Programına Göz Atın!"
                      
                        ciddi_obez+="isim: {} - durum: ciddi obez\n".format(isim)
                        ciddi_uye = open("ciddi_obez.txt","a")
                        ciddi_yaz = ciddi_uye.write(ideal)
                        ciddi_uye.close()
                        kilo_ver3 = kalori - 700
                       
                        aciklama += """
Merhaba {} görünüşe göre ciddi obez sınıfındasınız\nama endişelenmeyin fitbook da çözümler bitmez\n
şimdi gelin bir diyet programı oluşturalım.\nkilonuz {} ve boyunuz {} yaşınız ise {}\n
1g protein: 4kcal / 1g karbonhidrat: 4kcal / 1g yag: 9kcal\nGünlük almanız gereken kalori: {} kaloridir\nKilo vermek için {} kalori almalısınız\n
İdeal kiloya gelene kadar her hafta 400-600 kalori azaltablirsiniz\nsize güveniyoruz ve inanıyoruz 
                        
                        """.format(isim,kilo,boy,yas,kalori,kilo_ver3)
                        l_aciklama["text"] = aciklama
                        def tavsiye3():
                            dosya = open("kilo_ver","r")
                            icerik = dosya.read()
                            dosya.close()
           
                        
                            for i in icerik.splitlines():
                                tavsiye_yaz3 = "{}\n".format(i)
                                tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',10,'bold'))
                                tavsiye_alani.insert(END,tavsiye_yaz3,"style")

                        tv3 = Thread(target=tavsiye3)
                        tv3.start()

                   
                    tablo = """
*****************************************************************
üye ismi: {}
üye soyisim: {}
yaş : {}
kilo : {}
boy: {}
cinsiyet: kadın

durum: {}

uyelik kimligi: {}

©fitbook - olcaysoftware



*****************************************************************
            
                    """.format(isim,soyisim,yas,kilo_kilo,Eboy,durum,id)

                    uye_dosyasi = open("fittbook_uye.txt","a")
                    uye_dosyasi.write(tablo)
                    uye_dosyasi.close()

                    uye_isimleri = open("uyelikler.txt","a")
                    yaz = "uye : {} {}  - cinsiyet: kadın\n".format(isim,soyisim)
                    yazdir = uye_isimleri.write(yaz)
                    uye_isimleri.close()

                    kadin = open("kadin.txt","a")
                    kadin.write(yaz)
                    kadin.close()
                    #-----Toplam üyeler senkronizasyon
                    with open("uyelikler.txt", "r") as f:
                          uye_sayisi = f.read().count("\n")
                          uye_str = "Toplam Üyeler\n{}".format(str(uye_sayisi))
                          toplam_str = "Toplam Kaydetme\n{}".format(str(uye_sayisi))

                          toplam_uye["text"] = uye_str
                          toplam_uye2["text"] = uye_str
                          toplam_kayit["text"] = toplam_str

                    
                    #-------------------#üye sayıları senkronizasyon
                    with open("ciddi_obez.txt", "r") as c:
                      uye_sayisi_c = c.read().count("\n")
                      uye_str_c = "Ciddi Obez üyeler\n{}".format(str(uye_sayisi_c))
                      ciddi_obez_sayisi["text"] = uye_str_c

                    with open("obez.txt", "r") as o:
                      uye_sayisi_o = o.read().count("\n")
                      uye_str_o = "Obez üyeler\n{}".format(str(uye_sayisi_o))
                      obez_uye_sayisi["text"] = uye_str_o


                    with open("kilolu.txt", "r") as k:
                      uye_sayisi_k = k.read().count("\n")
                      uye_str_k = "Kilolu üyeler\n{}".format(str(uye_sayisi_k))
                      kilolu_uye_sayisi["text"] = uye_str_k


                    with open("zayif.txt", "r") as z:
                      uye_sayisi_z = z.read().count("\n")
                      uye_str_z = "Zayıf üyeler\n{}".format(str(uye_sayisi_z))
                      zayif_uye_sayisi["text"] = uye_str_z


                    with open("ideal.txt", "r") as ideal:
                      uye_sayisi_ideal = ideal.read().count("\n")
                      uye_str_ideal = "İdeal Kilolu üyeler\n{}".format(str(uye_sayisi_ideal))
                      ideal_uye_sayisi["text"] = uye_str_ideal


                    with open("kadin.txt", "r") as kadin:
                      kadinuye = kadin.read().count("\n")
                      kadin_str = "Kadın üyeler\n{}".format(str(kadinuye))
                      lkadin["text"] = kadin_str
                    
                      #loading efekti
                    def d2():
                        lady = PhotoImage(file="lady_50px.png")
                        cinsiyet_ek["image"] = lady
    
                        for i in range(1):
                            kayit_sonucu2["text"] = "lütfen bekleyin"
                            load1 = PhotoImage(file="load1.png")
                            kayit_sonucu["image"] = load1
                            sleep(1)
                            load2 = PhotoImage(file="load2.png")
                            kayit_sonucu["image"] = load2
                            sleep(1)
                            load3 = PhotoImage(file="load3.png")
                            kayit_sonucu["image"] = load3
                            sleep(1)
                            load4 = PhotoImage(file="load4.png")
                            kayit_sonucu["image"] = load4
                            sleep(1)
                            kayit_succes = PhotoImage(file="kayit_succes.png")
                            kayit_sonucu["image"] = kayit_succes
                            kayit_sonucu2["text"] = "uye kaydedildi"
                            sleep(10)
                            kayit_sonucu2["text"] = ""
                           
         
                    t2 = Thread(target=d2)
                    t2.start()
                      #loading efekti
                    def d3():
                      
    
                        for i in range(1):
                            l_load1 = PhotoImage(file="label_load1.png")
                            l_load["image"] = l_load1
                            sleep(1)
                            l_load2 = PhotoImage(file="label_load2.png")
                            l_load["image"] = l_load2
                            sleep(1)
                            l_load3 = PhotoImage(file="label_load3.png")
                            l_load["image"] = l_load3
                            sleep(1)
                            l_load4 = PhotoImage(file="label_load4.png")
                            l_load["image"] = l_load4
                            sleep(1)
                            l_load5 = PhotoImage(file="label_load5.png")
                            l_load["image"] = l_load5
                            sleep(30)
                       
      

                    t3 = Thread(target=d3)
                    t3.start()
            else:

                kayit_sonucu2["text"] = "lütfen bilgileri doldurun!"


        else:
            mesaj += "Gerekli Alanları Doldurun Ve İşaretleyin"
            messagebox.showinfo("Eksikler Var",mesaj)
    
    except:

        mesaj += "Boş Alanlar Var!"
        kayit_sonucu2["text"] = mesaj
        bos_alan = PhotoImage(file="error_20px.png")
        kayit_sonucu["image"] = bos_alan

#---------------------------------#

master = Tk()
master.title("FİTBOOK - hoşgeldiniz")
master.geometry("1100x600+100+100")
photoicon = PhotoImage(file = "food_100px.png")
master.iconphoto(False, photoicon)
master.minsize(700,400)
master.state("zoomed")
master["bg"] = "black"


#----------frame1----------#
#--------------------------#
frame1 = Frame(master,bg="black",bd=5,relief=SOLID)
frame1.place(relx=0,rely=0,relwidth=0.2,relheight=0.1)
yanframe = Frame(master,bg="black")
yanframe.place(relx=0.2,rely=0,relwidth=0.8,relheight=0.1)

limage = PhotoImage(file="fitbook.png")
Label(frame1,text="  FİTBOOK ",bg="black",fg="white",font="Arial 12 bold").pack(padx=5,pady=5,side=LEFT)
Label(frame1,image=limage,bg="black",font="Arial 12 bold").pack(padx=5,pady=5,side=LEFT)
cinsiyet_ek = Label(frame1,bg="black")
cinsiyet_ek.pack(padx=5,pady=5,side=LEFT)

toplam_uye = Label(yanframe,bg="black",fg="white",font="Verdana 10 bold")
toplam_uye.pack(padx=10,pady=10,side=LEFT)
#obez sayısı
obez_uye_sayisi = Label(yanframe,bg="black",fg="white",font="Verdana 10 bold")
obez_uye_sayisi.pack(padx=25,pady=10,side=LEFT)
#ciddi_obez_sayisi
ciddi_obez_sayisi = Label(yanframe,bg="black",fg="white",font="Verdana 10 bold")
ciddi_obez_sayisi.pack(padx=10,pady=10,side=LEFT)
#kilolu uyeler
kilolu_uye_sayisi = Label(yanframe,bg="black",fg="white",font="Verdana 10 bold")
kilolu_uye_sayisi.pack(padx=10,pady=10,side=LEFT)
#zayif uyeler
zayif_uye_sayisi = Label(yanframe,bg="black",fg="white",font="Verdana 10 bold")
zayif_uye_sayisi.pack(padx=10,pady=10,side=LEFT)
#ideal kilolu uyeler
ideal_uye_sayisi = Label(yanframe,bg="black",fg="green",font="Verdana 10 bold")
ideal_uye_sayisi.pack(padx=10,pady=10,side=LEFT)


#----------frame2----------#
#--------------------------#

frame2 = Frame(master,bg="lightgrey")
frame2.place(relx=0,rely=0.1,relwidth=0.2,relheight=0.1)
Label(frame2,text="Üye Kaydı Oluşturun",bg="lightgrey",fg="darkslategrey",font="Arial 15 bold").pack(padx=5,pady=5,anchor=S)


yan_frame2 = Frame(master,bg="lightgrey",bd=2,relief=GROOVE)
yan_frame2.place(relx=0.21,rely=0.1,relwidth=0.4,relheight=0.1)
#bilgilendirme label
licon = PhotoImage(file="about_20px.png")
l_icon = Label(yan_frame2,image=licon,bg="lightgrey")
l_icon.pack(padx=5,pady=0,anchor=NW,side=LEFT)

l_baslik = Label(yan_frame2,bg="lightgrey",fg="#333",text="Bilgiler burada görünür..",font="Arial 10 bold")
l_baslik.pack(padx=5,pady=5,anchor=NW)

l_bilgi = Label(yan_frame2,bg="lightgrey",font="Arial 10 bold")
l_bilgi.pack(padx=5,pady=5,anchor=NW)


yan_frame3 = Frame(master,bg="lightgrey")
yan_frame3.place(relx=0.21,rely=0.2,relwidth=0.4,relheight=0.4)

l_aciklama = Label(yan_frame3,bg="lightgrey",text="\nFİTBOOK APP",font="Arial 48 bold",fg="black")
l_aciklama.pack(padx=5,pady=5)

#--
yan_frame4 = Frame(master,bg="lightgrey")
yan_frame4.place(relx=0.21,rely=0.6,relwidth=0.4,relheight=0.1)


ticon = PhotoImage(file="about_20px.png")
l_icon = Label(yan_frame4,image=ticon,bg="lightgrey")
l_icon.pack(padx=5,pady=0,side=LEFT)
l_tavsiye = Label(yan_frame4,bg="lightgrey",fg="#333",text="Tavsiyeler burada görünür..",font="Arial 12 bold")
l_tavsiye.pack(padx=5,pady=5,side=LEFT)
l_load = Label(yan_frame4,bg="lightgrey")
l_load.pack(padx=5,pady=5,side=LEFT)


yan_frame5 = Frame(master,bg="lightgrey")
yan_frame5.place(relx=0.21,rely=0.7,relwidth=0.4,relheight=0.30)


tavsiye_alani = Text(yan_frame5,height=15,width=67,bg="lightgrey")
tavsiye_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Verdana',20,'bold'))
tavsiye_alani.pack()
example = "FİTBOOK TAVSİYE EDİYOR.."
tavsiye_alani.insert(END,example,"style")
#üyeleri sil---
def uye_sil():
    
    zayif_uye = open("zayif.txt","w")
    temizle1 = zayif_uye.write("")
    zayif_uye.close()
    #-------
    ideal_uye = open("ideal.txt","w")
    temizle2 = ideal_uye.write("")
    ideal_uye.close()
    #-------
    kilolu_uye = open("kilolu.txt","w")
    temizle3 = kilolu_uye.write("")
    kilolu_uye.close()
    #-------
    obez_uye = open("obez.txt","w")
    temizle4 = obez_uye.write("")
    obez_uye.close()
    #-------
    ciddi_uye = open("ciddi_obez.txt","w")
    temizle5 = ciddi_uye.write("")
    ciddi_uye.close()
    #-------
    uye_dosyasi = open("fittbook_uye.txt","w")
    temizle6 = uye_dosyasi.write("")
    uye_dosyasi.close()
    #-------
    uyelikler = open("uyelikler.txt","w")
    temizle7 = uyelikler.write("")
    uyelikler.close()
    #-------
    kadinlar = open("kadin.txt","w")
    temizle8 = kadinlar.write("")
    kadinlar.close()
    #-------
    erkekler = open("erkek.txt","w")
    temizle9 = erkekler.write("")
    erkekler.close()

        #-----Toplam üyeler senkronizasyon
    with open("uyelikler.txt", "r") as f:
            uye_sayisi = f.read().count("\n")
            uye_str = "Toplam Üyeler\n{}".format(str(uye_sayisi))
            toplam_uye["text"] = uye_str
            toplam_uye2["text"] = uye_str

                    
    #-------------------#üye sayıları senkronizasyon
    with open("ciddi_obez.txt", "r") as c:
        uye_sayisi_c = c.read().count("\n")
        uye_str_c = "Ciddi Obez üyeler\n{}".format(str(uye_sayisi_c))
        ciddi_obez_sayisi["text"] = uye_str_c

    with open("obez.txt", "r") as o:
        uye_sayisi_o = o.read().count("\n")
        uye_str_o = "Obez üyeler\n{}".format(str(uye_sayisi_o))
        obez_uye_sayisi["text"] = uye_str_o


    with open("kilolu.txt", "r") as k:
        uye_sayisi_k = k.read().count("\n")
        uye_str_k = "Kilolu üyeler\n{}".format(str(uye_sayisi_k))
        kilolu_uye_sayisi["text"] = uye_str_k


    with open("zayif.txt", "r") as z:
        uye_sayisi_z = z.read().count("\n")
        uye_str_z = "Zayıf üyeler\n{}".format(str(uye_sayisi_z))
        zayif_uye_sayisi["text"] = uye_str_z


    with open("ideal.txt", "r") as ideal:
        uye_sayisi_ideal = ideal.read().count("\n")
        uye_str_ideal = "İdeal Kilolu üyeler\n{}".format(str(uye_sayisi_ideal))
        ideal_uye_sayisi["text"] = uye_str_ideal


    with open("erkek.txt", "r") as erkek:
        erkekuye = erkek.read().count("\n")
        erkek_str = "Erkek üyeler\n{}".format(str(erkekuye))
        lerkek["text"] = erkek_str


    with open("kadin.txt", "r") as kadin:
        kadinuye = kadin.read().count("\n")
        kadin_str = "Kadın üyeler\n{}".format(str(kadinuye))
        lkadin["text"] = kadin_str
#-------------------------------
yan_frame6 = Frame(master,bg="lightgrey",bd=2,relief=GROOVE)
yan_frame6.place(relx=0.61,rely=0.1,relwidth=0.39,relheight=0.1)
Label(yan_frame6,text="Tüm Üyeleri Sil",bg="lightgrey",fg="#333",font="Arial 13 bold").pack(padx=15,pady=5,side=LEFT)
delete = PhotoImage(file="delete.png")
sil = Button(yan_frame6,image=delete,command=uye_sil,relief=FLAT,bg="lightgrey")
sil.pack(padx=5,pady=5,side=LEFT)
toplam_uye2 = Label(yan_frame6,bg="lightgrey",fg="black",font="Arial 10 bold")
toplam_uye2.pack(padx=5,pady=5,side=LEFT)
silme_islemi = Label(yan_frame6,text="Bu işlem geri döndürülemez!",bg="lightgrey",fg="#333",font="Arial 8 bold")
silme_islemi.pack(padx=5,pady=5,side=LEFT)

#uye bilgi paneli yan_frame7 bilgiler
yan_frame7 = Frame(master,bg="lightgrey",bd=2,relief=GROOVE)
yan_frame7.place(relx=0.61,rely=0.2,relwidth=0.39,relheight=0.1)
Label(yan_frame7,text="Üye Bilgi Paneli",bg="lightgrey",fg="#333",font="Arial 13 bold").pack(padx=15,pady=5,side=LEFT)
lkadin = Label(yan_frame7,bg="lightgrey",fg="black",font="Arial 10 bold")
lkadin.pack(padx=5,pady=5,side=LEFT)
lerkek = Label(yan_frame7,bg="lightgrey",fg="black",font="Arial 10 bold")
lerkek.pack(padx=15,pady=5,side=LEFT)
Label(yan_frame7,text="Düzenlenebilir panel",bg="lightgrey",fg="#333",font="Arial 9 bold").pack(padx=15,pady=5,side=LEFT)
#panel


def panel():

    yazdir = panel_alani.get("1.0","end")
    changer = open("fittbook_uye.txt","w")
    changer.write(yazdir)
    changer.close()
    
    kaydet_panel.pack(padx=50,pady=10,side=LEFT)
    kaydedildi.pack(side=LEFT)

   
    def loading():
     
        for i in range(1):
            
            load1 = PhotoImage(file="load1.png")
            kaydedildi["image"] = load1
            sleep(1)
            load2 = PhotoImage(file="load2.png")
            kaydedildi["image"] = load2
            sleep(1)
            load3 = PhotoImage(file="load3.png")
            kaydedildi["image"] = load3
            sleep(1)
            load4 = PhotoImage(file="load4.png")
            kaydedildi["image"] = load4
            sleep(1)
            kayit_succes = PhotoImage(file="kayit_succes.png")
            kaydedildi["image"] = kayit_succes
            sleep(10)
            
  
                           
         
    load = Thread(target=loading)
    load.start()

#düzenleme ve kayıt islemleri
yan_frame8 = Frame(master,bg="lightgrey",bd=2,relief=FLAT)
yan_frame8.place(relx=0.61,rely=0.3,relwidth=0.39,relheight=0.45)

fittbook_uye = open("fittbook_uye.txt","r")
oku = fittbook_uye.read()
fittbook_uye.close()
fitt_book = "Bilgiler Burada Görünür...\n"+oku
panel_alani = Text(yan_frame8,height=15,width=67,bg="lightgrey")
panel_alani.tag_configure('style',foreground='black',background="lightgrey",font=('Arial',10,'bold'))
panel_alani.pack()
panel_alani.insert(END,fitt_book,"style")

kaydet = PhotoImage(file="kaydet.png")
kaydet_panel = Button(yan_frame8,image=kaydet,command=panel,bg="lightgrey",relief=FLAT)
kaydet_panel.pack(pady=10)

kaydedildi = Label(yan_frame8,bg="lightgrey")
kaydedildi.pack()

#son frame--

yan_frame9 = Frame(master,bg="lightgrey",bd=2,relief=FLAT)
yan_frame9.place(relx=0.61,rely=0.75,relwidth=0.39,relheight=0.15)
toplam_kayit = Label(yan_frame9,bg="lightgrey",fg="black",font="Arial 10 bold")
toplam_kayit.pack(padx=5,pady=5,side=LEFT)

songiris = Label(yan_frame9,bg="lightgrey",fg="black",font="Arial 10 bold")
songiris.pack(padx=5,pady=5,side=LEFT)
giris = datetime.datetime.now()
songiris["text"] = "Son Giriş\n{}".format(giris)

sonkayit = Label(yan_frame9,bg="lightgrey",fg="black",font="Arial 10 bold")
sonkayit.pack(padx=5,pady=5,side=LEFT)

#footer kapanış---yapımcı hakkında bilgi
yan_frame10 = Frame(master,bg="lightgrey",bd=2,relief=FLAT)
yan_frame10.place(relx=0.61,rely=0.9,relwidth=0.39,relheight=0.1)
yapimci = "OlcaySoftware - ©fittbook 2021\nyasincan olcay"
Label(yan_frame10,text=yapimci,bg="lightgrey",fg="#333",font="Arial 10 bold").pack()
#instagram ikon
instagram = PhotoImage(file="instagram.png")
Label(yan_frame10,image=instagram,bg="lightgrey").pack(side=LEFT)
#facebook ikon
facebook = PhotoImage(file="facebook.png")
Label(yan_frame10,image=facebook,bg="lightgrey").pack(side=LEFT)
#twitter ikon
twitter = PhotoImage(file="twitter.png")
Label(yan_frame10,image=twitter,bg="lightgrey").pack(side=LEFT)
#github ikon
github = PhotoImage(file="github.png")
Label(yan_frame10,image=github,bg="lightgrey").pack(side=LEFT)
#onay ikon
onay = PhotoImage(file="onay.png")
Label(yan_frame10,image=onay,bg="lightgrey").pack(side=LEFT)
#python ikon
python = PhotoImage(file="python.png")
Label(yan_frame10,image=python,bg="lightgrey").pack(side=RIGHT)
#linux ikon
linux = PhotoImage(file="linux.png")
Label(yan_frame10,image=linux,bg="lightgrey").pack(side=RIGHT)
#windows ikon
windows = PhotoImage(file="windows.png")
Label(yan_frame10,image=windows,bg="lightgrey").pack(side=RIGHT)

#----------frame3----------#
#--------------------------#

frame3 = Frame(master,bg="lightgrey")
frame3.place(relx=0,rely=0.2,relwidth=0.2,relheight=0.1)
Label(frame3,text="İSİM:",bg="lightgrey",fg="black",font="Arial 12 bold").pack(padx=27,pady=2,side=LEFT)
e_isim = Entry(frame3,bd=2,relief=SOLID)
e_isim.pack(padx=0,pady=2,side=LEFT)

#----------frame4----------#
#--------------------------#

frame4 = Frame(master,bg="lightgrey")
frame4.place(relx=0,rely=0.3,relwidth=0.2,relheight=0.1)
#--
Label(frame4,text="SOYİSİM:",bg="lightgrey",fg="black",font="Arial 12 bold").pack(padx=10,pady=2,side=LEFT)
e_soyisim = Entry(frame4,bd=2,relief=SOLID)
e_soyisim.pack(padx=0,pady=2,side=LEFT)

#----------frame5----------#
#--------------------------#

frame5 = Frame(master,bg="lightgrey")
frame5.place(relx=0,rely=0.4,relwidth=0.2,relheight=0.1)
#--
Label(frame5,text="YAŞ:",bg="lightgrey",fg="black",font="Arial 12 bold").pack(padx=27,pady=2,side=LEFT)
e_yas = Entry(frame5,bd=2,relief=SOLID)
e_yas.pack(padx=0,pady=2,side=LEFT)

#----------frame6----------#
#--------------------------#

frame6 = Frame(master,bg="lightgrey")
frame6.place(relx=0,rely=0.5,relwidth=0.2,relheight=0.1)
#--
Label(frame6,text="KİLO/BOY:",bg="lightgrey",fg="black",font="Arial 12 bold").pack(padx=10,pady=2,side=LEFT)
e_kilo = Entry(frame6,bd=2,relief=SOLID,width=13)
e_kilo.pack(padx=0,pady=2,side=LEFT)
e_boy = Entry(frame6,bd=2,relief=SOLID)
e_boy.pack(padx=3,pady=2,side=LEFT)



#----------frame7----------#
#--------------------------#


frame7 = Frame(master,bg="lightgrey")
frame7.place(relx=0,rely=0.6,relwidth=0.2,relheight=0.1)
Label(frame7,text="CİNSİYET:",bg="lightgrey",fg="black",font="Arial 12 bold").pack(padx=5,pady=0,side=LEFT)
var = IntVar()
R1 = Radiobutton(frame7,text='erkek',variable=var,value=1,bg='lightgrey',fg='black',font='Arial 12 bold')
R1.pack(side=LEFT,pady=5,padx=5)
#----------------
R2 = Radiobutton(frame7,text='kadın',variable=var,value=2,bg='lightgrey',fg='black',font='Arial 12 bold')
R2.pack(side=LEFT,pady=5,padx=5)
#--------buton frame-------#
#--------------------------#
frame_btn = Frame(master,bg="lightgrey")
frame_btn.place(relx=0,rely=0.7,relwidth=0.2,relheight=0.15)
kayit_sonucu = Label(frame_btn,text="kayıt bekleniyor..",fg="grey",bg="lightgrey",font="Arial 8 bold")
kayit_sonucu.pack()
kayit_sonucu2 = Label(frame_btn,text=".",fg="grey",bg="lightgrey",font="Arial 8 bold")
kayit_sonucu2.pack()

#uyelerin sayısı-----
with open("uyelikler.txt", "r") as f:
  uye_sayisi = f.read().count("\n")
  uye_str = "Toplam Üyeler\n{}".format(str(uye_sayisi))
  toplam_uye["text"] = uye_str
  toplam_uye2["text"] = uye_str

#-------------------#
with open("ciddi_obez.txt", "r") as c:
  uye_sayisi_c = c.read().count("\n")
  uye_str_c = "Ciddi Obez üyeler\n{}".format(str(uye_sayisi_c))
  ciddi_obez_sayisi["text"] = uye_str_c

with open("obez.txt", "r") as o:
  uye_sayisi_o = o.read().count("\n")
  uye_str_o = "Obez üyeler\n{}".format(str(uye_sayisi_o))
  obez_uye_sayisi["text"] = uye_str_o


with open("kilolu.txt", "r") as k:
  uye_sayisi_k = k.read().count("\n")
  uye_str_k = "Kilolu üyeler\n{}".format(str(uye_sayisi_k))
  kilolu_uye_sayisi["text"] = uye_str_k


with open("zayif.txt", "r") as z:
  uye_sayisi_z = z.read().count("\n")
  uye_str_z = "Zayıf üyeler\n{}".format(str(uye_sayisi_z))
  zayif_uye_sayisi["text"] = uye_str_z


with open("ideal.txt", "r") as ideal:
  uye_sayisi_ideal = ideal.read().count("\n")
  uye_str_ideal = "İdeal Kilolu üyeler\n{}".format(str(uye_sayisi_ideal))
  ideal_uye_sayisi["text"] = uye_str_ideal




with open("erkek.txt", "r") as erkek:
    erkekuye = erkek.read().count("\n")
    erkek_str = "Erkek üyeler\n{}".format(str(erkekuye))
    lerkek["text"] = erkek_str


with open("kadin.txt", "r") as kadin:
    kadinuye = kadin.read().count("\n")
    kadin_str = "Kadın üyeler\n{}".format(str(kadinuye))
    lkadin["text"] = kadin_str

def d1():
    x=0
    while True:
        kayit_sonucu["text"] = "kayıt bekleniyor."
        l_baslik["text"] = "Bilgiler burada görünür.."
        sleep(1)
        kayit_sonucu["text"] = "kayıt bekleniyor.."
        l_baslik["text"] = "Bilgiler burada görünür..."

        sleep(1)
        kayit_sonucu["text"] = "kayıt bekleniyor..."
        l_baslik["text"] = "Bilgiler burada görünür...."

        sleep(1)
        kayit_sonucu["text"] = "kayıt bekleniyor...."
        l_baslik["text"] = "Bilgiler burada görünür....."

        sleep(1)
        x+=1
        if x == 1:
            kayit_sonucu["text"] = "kayıt için tıkla"
            l_baslik["text"] = "Bilgiler burada görünür.."

            break
        else:
            continue

    

t1 = Thread(target=d1)
t1.start()
        
 
#-
dwnd = PhotoImage(file='fitbook.png')
Button(frame_btn, image=dwnd, command=uye_kaydi,relief=FLAT,bg="lightgrey",activebackground="lightgrey").pack(pady=10)

#----------frame8----------#
#--------------------------#
def exit():

    master.destroy()
    
frame8 = Frame(master,bg="lightgrey")
frame8.place(relx=0,rely=0.85,relwidth=0.2,relheight=0.15)
Label(frame8,text="Çıkış..",bg="lightgrey",fg="#333",font="Arial 10 bold").pack()
yemek_kalori = PhotoImage(file='exit.png')
Button(frame8, image=yemek_kalori, command=exit,relief=FLAT,bg="lightgrey",activebackground="lightgrey").pack(pady=10)

master.mainloop()

