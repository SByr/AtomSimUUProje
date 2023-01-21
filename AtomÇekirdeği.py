import pygame as py
from yarilanma import proton_sayısı, yarılanma_ömürleri, maxOrbitalDuzeni, orbitaller, elementi_bul, izotopu_bul, orbitalHesapla

py.init()

#PENCERE OLUŞTUR
winsize=(1366,768)

win=py.display.set_mode(winsize)

#BAŞLIK
py.display.set_caption("Atom Çekirdeği")

#PROTON TANESİ
proton_çap=20
proton_renk=(255,255,255)
hız=0.02
protonlar=0

#NÖTRON TANESİ
nötron_çap=20
nötron_renk=(0,0,0)
nötronlar=0

#FONTLAR
font=py.font.SysFont("Times",22,bold=True)
font3 = py.font.Font("seguisym.ttf", 26,bold=True)
font4=py.font.SysFont("Times",20,bold=True)
font5=py.font.SysFont("Times",100,bold=True)
font6 = py.font.Font("seguisym.ttf", 36,bold=True)

#BAŞLIK
font2=py.font.SysFont("Times",30,bold=True)
başlık=font2.render("ATOM ÇEKİRDEĞİ OLUŞTURMA SİMÜLASYONU",1,(255,255,255))
arkaplanrenk=(11,32,39)


#ÇIKIŞ BUTONU
cb_pos = (1300, 30)
cb_size = (50, 50)
cb_color = (64,121,140)

cikisButonu = py.Rect(cb_pos,cb_size)
cikisText = font.render("X",1,(0x18020C))

#PROTON EKLE-ÇIKAR BUTONLARI
pe_pos=(50,120)
pe_size=(200,50)
pe_color=(64,121,140)
pc_pos=(50,200)
pc_size=(200,50)
pc_color=(64,121,140)

pe_buton=py.Rect(pe_pos,pe_size)
pe_text=font.render("Proton Ekle",1,(0x18020C))

pc_buton=py.Rect(pc_pos,pc_size)
pc_text=font.render("Proton Çıkar",1,(0x18020C))

#NÖTRON EKLE-ÇIKAR BUTONLARI
ne_pos=(50,300)
ne_size=(200,50)
ne_color=(64,121,140)
nc_pos=(50,380)
nc_size=(200,50)
nc_color=(64,121,140)

ne_buton=py.Rect(ne_pos,ne_size)
ne_text=font.render("Nötron Ekle",1,(0x18020C))

nc_buton=py.Rect(nc_pos,nc_size)
nc_text=font.render("Nötron Çıkar",1,(0x18020C))

#BETA IŞIMASI BUTONLARI
bip_pos = (1005,350)
bip_cap = (200,40)
bip_color = (64,121,140)

bin_pos = (1005,410)
bin_cap = (200,40)
bin_color = (64,121,140)

alfa_pos=(1005,470)
alfa_size = (200,40)
alfa_color = (64,121,140)

proton_text=font.render("Proton",1,(255,255,255))
nötron_text=font.render("Nötron",1,(255,255,255))
elektron_text=font.render("Elektron",1,(255,255,255))
pozitron_text=font.render("Pozitron",1,(255,255,255))

bip_buton=py.Rect(bip_pos,bip_cap)
bip_text=font.render("β+ Bozunması",1,(0x18020C))

bin_buton=py.Rect(bin_pos,bin_cap)
bin_text=font.render("β- Bozunması",1,(0x18020C))

alfa_buton=py.Rect(alfa_pos,alfa_size)
alfa_text=font.render("α Bozunması",1,(0x18020C))

#ELEKTRON BULUTU BUTON
eb_pos=(255,460)
eb_size=(30,35)
eb_color=(100,255,255)

eb_buton=py.Rect(eb_pos,eb_size)
eb_kapalı_text=font3.render("X",1,(0x18020C))
eb_açık_text=font3.render("✓",1,(0x18020C))
kapalı_açık=1
e_b_durumu_text=font4.render("ELEKTRON BULUTU:",1,(0,0,0))

#SEMBOL BUTON
sb_pos=(50,500)
sb_size=(200,30)
sb_color=(0,0,0)

sb_buton=py.Rect(sb_pos,sb_size)
sb_text=font.render("Sembol",1,(190,255,255))
sembolbilgi=1

#SIFIRLA BUTONU
sıfırla_buton_pos=(1150,248)
sıfırla_buton_size=(150,30)
sıfırla_buton_color=(0,0,0)

sıfırla_buton=py.Rect(sıfırla_buton_pos,sıfırla_buton_size)

#TANECİK KONUMLARI
proton_konum=[]
protoncıkarma_konum=[]
nötron_konum=[]
nötroncıkarma_konum=[]
elektron_konum=[]
pozitron_konum=[]




#FONKSİYONLAR
def cik():
    çalıştır=False
    py.quit()

def p_e():
    global protonlar
    protonlar+=1

def p_c():
    global protonlar
    protonlar-=1

def n_e():
    global nötronlar
    nötronlar+=1

def n_c():
    global nötronlar
    nötronlar-=1

def b_p():
    global nötronlar
    global protonlar
    nötronlar+=1
    protonlar-=1

def b_n():
    global nötronlar
    global protonlar
    nötronlar-=1
    protonlar+=1


def alfa_bozunması():
    global nötronlar
    global protonlar
    nötronlar-=2
    protonlar-=2
    nötroncıkarma_konum.append((683,434))
    protoncıkarma_konum.append((683,394))

def kapamaaçma():
    global kapalı_açık
    if kapalı_açık==1:
        kapalı_açık-=1
    elif kapalı_açık==0:
        kapalı_açık+=1

def sembolonoff():
    global sembolbilgi
    if sembolbilgi==1:
        sembolbilgi-=1
    elif sembolbilgi==0:
        sembolbilgi+=1

çalıştır=True
while çalıştır:

    for event in py.event.get():

        if event.type==py.QUIT:
            çalıştır=False
        if event.type== py.MOUSEBUTTONDOWN:
            mouse_pos=py.mouse.get_pos()

            #BUTON-FARE ETKİLEŞİMLERİ
            
            if cikisButonu.collidepoint(mouse_pos):
                cik()
            
            if str(izotopu_bul(nötronlar,protonlar+1))!="None":
                if pe_buton.collidepoint(mouse_pos):
                    proton_konum.append((90,130))
                    p_e()


            if str(izotopu_bul(nötronlar,protonlar-1))!="None":    
                if pc_buton.collidepoint(mouse_pos):
                    if protonlar>=1:
                        protoncıkarma_konum.append((683,394))
                        p_c()

            if str(izotopu_bul(nötronlar+1,protonlar))!="None":
                if ne_buton.collidepoint(mouse_pos):
                    n_e()
                    nötron_konum.append((90,330))

            if str(izotopu_bul(nötronlar-1,protonlar))!="None":
                if nc_buton.collidepoint(mouse_pos):
                    if nötronlar>=1:
                        nötroncıkarma_konum.append((683,434))
                        n_c()
            
            if str(izotopu_bul(nötronlar+1,protonlar-1))!="None":
                if bip_buton.collidepoint(mouse_pos):
                    if nötronlar>=1:
                        elektron_konum.append((683,394))
                        b_p()
                        nötron_konum.append((90,330))

            if str(izotopu_bul(nötronlar-1,protonlar+1))!="None":
                if bin_buton.collidepoint(mouse_pos):
                    if nötronlar>=1:
                        pozitron_konum.append((683,434))
                        b_n()
                        proton_konum.append((90,130))

            if str(izotopu_bul(nötronlar-2,protonlar-2))!="None":
                if alfa_buton.collidepoint(mouse_pos):
                    alfa_bozunması()


            if eb_buton.collidepoint(mouse_pos):
                kapamaaçma()

            if sb_buton.collidepoint(mouse_pos):
                sembolonoff()

            if sıfırla_buton.collidepoint(mouse_pos):
                protonlar=0
                nötronlar=0
    

    #TANECİK HAREKETLERİ İÇİN FOR DÖNGÜLERİ
    for i, pe_pos in enumerate(proton_konum):
        xyol=winsize[0]/2 - proton_çap - pe_pos[0]
        yyol=winsize[1]/2 - proton_çap - pe_pos[1]

        xhareket=xyol*hız*2
        yhareket=yyol*hız*2


        proton_konum[i]=(pe_pos[0]+ xhareket,pe_pos[1]+yhareket)
    
    for i, pc_pos in enumerate(protoncıkarma_konum):


        if protonlar>=0:
            xyol=winsize[1]*2 - proton_çap - pc_pos[0]
            yyol=winsize[0]/2 - proton_çap - pc_pos[1]

            xhareket=xyol*hız
            yhareket=yyol*hız


            protoncıkarma_konum[i]=(pc_pos[0]+ xhareket,pc_pos[1]+yhareket)


    for i, ne_pos in enumerate(nötron_konum):
        xyol=winsize[0]/2 - nötron_çap - ne_pos[0]
        yyol=winsize[1]/2+50 - nötron_çap - ne_pos[1]

        xhareket=xyol*hız*2
        yhareket=yyol*hız*2


        nötron_konum[i]=(ne_pos[0]+ xhareket,ne_pos[1]+yhareket)
    
    for i, nc_pos in enumerate(nötroncıkarma_konum):


        if nötronlar>=0:
            xyol=winsize[1]*2 - nötron_çap - nc_pos[0]
            yyol=winsize[0]/2 - nötron_çap - nc_pos[1]

            xhareket=xyol*hız
            yhareket=yyol*hız


            nötroncıkarma_konum[i]=(nc_pos[0]+ xhareket,nc_pos[1]+yhareket)

    for i, bp_pos in enumerate(elektron_konum):

        xyol=winsize[1]*2 - bp_pos[0]
        yyol=winsize[0]/2 - bp_pos[1]

        xhareket=xyol*hız/1.5
        yhareket=0


        elektron_konum[i]=(bp_pos[0]+ xhareket,bp_pos[1]+yhareket)

    for i, bn_pos in enumerate(pozitron_konum):

        xyol=winsize[1]*2 - bn_pos[0]
        yyol=winsize[0]/2 - bn_pos[1]

        xhareket=xyol*hız/1.5
        yhareket=0


        pozitron_konum[i]=(bn_pos[0]+ xhareket,bn_pos[1]+yhareket)


    win.fill(arkaplanrenk)


    

    #IŞIMALAR

    py.draw.rect(win,(11,12,39),py.Rect(1000,300,300,325))
    bozunmalar_text=font.render("Mevcut Bozunmalar",True,(255,255,255))
    win.blit(bozunmalar_text,(1030,310))


    py.draw.rect(win,bip_color,bin_buton)
    win.blit(bip_text,(1010,420))

    py.draw.rect(win,bip_color,bip_buton)
    win.blit(bin_text,(1010,355))

    py.draw.rect(win,alfa_color,alfa_buton)
    win.blit(alfa_text,(alfa_pos[0]+5,alfa_pos[1]+5))

    py.draw.circle(win,(255,255,255),(1020,550),15)
    win.blit(proton_text,(1037,536))

    py.draw.circle(win,(0,0,0),(1150,550),15)
    win.blit(nötron_text,(1170,536))

    py.draw.circle(win,(0,255,0),(1150,590),10)
    win.blit(pozitron_text,(1170,576))

    py.draw.circle(win,(0,0,255),(1020,590),10)
    win.blit(elektron_text,(1037,576))


    #BUTONLARI ÇİZ
    py.draw.rect(win,cb_color,cikisButonu)
    win.blit(cikisText,(1317,39))
    
    py.draw.rect(win,pe_color,pe_buton)
    win.blit(pe_text,(90,130))

    py.draw.rect(win,pc_color,pc_buton)
    win.blit(pc_text,(90,210))  

    py.draw.rect(win,sb_color,sb_buton)
    win.blit(sb_text,(90,502))  

    py.draw.rect(win,ne_color,ne_buton)
    win.blit(ne_text,(90,310))

    py.draw.rect(win,nc_color,nc_buton)
    win.blit(nc_text,(90,390))
   
    py.draw.circle(win,eb_color,(270,480),15)
    win.blit(e_b_durumu_text,(50,468))

    py.draw.rect(win,sıfırla_buton_color,sıfırla_buton)

    #ELEKTRON BULUTU
    if kapalı_açık==0:
        win.blit(eb_kapalı_text,(262,eb_pos[1]))
    elif kapalı_açık==1:
        win.blit(eb_açık_text,(262,eb_pos[1]))
    
    # YARİLANMA BİLGİSİ
    
    global omurAtom , omur
    omurAtom , omur = None, None
    if protonlar >= 1 and izotopu_bul(nötronlar,protonlar) != None:
        
        omurAtom , omur = izotopu_bul(nötronlar,protonlar)
    
    if omur == None:
        pass
    elif omur < 0.0000001:
        yarilanma_text=font.render("(" + omurAtom +" ,Stabil)",True,(255,255,255))
        win.blit(yarilanma_text,(555,285))
        yarilanma_text2=font.render("Element Adı ve Yarı Ömrü;",True,(255,255,255))
        win.blit(yarilanma_text2,(515,250))
    else: 
        yarilanma_text=font.render(""+ str(izotopu_bul(nötronlar,protonlar)),True,(255,255,255))
        win.blit(yarilanma_text,(555,285))
        yarilanma_text2=font.render("Element Adı ve Yarı Ömrü;",True,(255,255,255))
        win.blit(yarilanma_text2,(515,250))
    
    #Orbital Göstergesi

    orbitalText1 = font.render("Orbital",True,(255,255,255))
    win.blit(orbitalText1,(750, 700))
    orbitalText2 = font.render(""+str(orbitalHesapla(protonlar)),True,(255,255,255))
    win.blit(orbitalText2,(900, 700))

    #ATOM OLUŞMUYORSA BUTONU KIRMIZIYA BOYAMA

    if str(izotopu_bul(nötronlar,protonlar+1))=="None":
        pe_oluşmaz=py.Surface((pe_size))
        pe_oluşmaz.set_alpha(128)
        pe_oluşmaz.fill((255,0,0))
        win.blit(pe_oluşmaz,(50,120))

    if str(izotopu_bul(nötronlar,protonlar-1))=="None":
        pc_oluşmaz=py.Surface((pc_size))
        pc_oluşmaz.set_alpha(128)
        pc_oluşmaz.fill((255,0,0))
        win.blit(pc_oluşmaz,(50,200))


    if str(izotopu_bul(nötronlar+1,protonlar))=="None":
        ne_oluşmaz=py.Surface((ne_size))
        ne_oluşmaz.set_alpha(128)
        ne_oluşmaz.fill((255,0,0))
        win.blit(ne_oluşmaz,(50,300))

    if str(izotopu_bul(nötronlar-1,protonlar))=="None":
        nc_oluşmaz=py.Surface((nc_size))
        nc_oluşmaz.set_alpha(128)
        nc_oluşmaz.fill((255,0,0))
        win.blit(nc_oluşmaz,(50,380))

    
    if str(izotopu_bul(nötronlar+1,protonlar-1))=="None":
        bp_oluşmaz=py.Surface((bip_cap))
        bp_oluşmaz.set_alpha(128)
        bp_oluşmaz.fill((255,0,0))
        win.blit(bp_oluşmaz,(bip_pos))

    if str(izotopu_bul(nötronlar-1,protonlar+1))=="None":
        bn_oluşmaz=py.Surface((bin_cap))
        bn_oluşmaz.set_alpha(128)
        bn_oluşmaz.fill((255,0,0))
        win.blit(bn_oluşmaz,(bin_pos))

    if str(izotopu_bul(nötronlar-2,protonlar-2))=="None":
        alfa_oluşmaz=py.Surface((alfa_size))
        alfa_oluşmaz.set_alpha(128)
        alfa_oluşmaz.fill((255,0,0))
        win.blit(alfa_oluşmaz,(alfa_pos))

    #TANECİKLERİ ÇİZ
    for pe_pos in proton_konum:
        py.draw.circle(win,proton_renk,pe_pos,proton_çap)
    
    for pc_pos in protoncıkarma_konum:
        py.draw.circle(win,proton_renk,pc_pos,proton_çap)


    for ne_pos in nötron_konum:
        py.draw.circle(win,nötron_renk,ne_pos,nötron_çap)
    
    for nc_pos in nötroncıkarma_konum:
        py.draw.circle(win,nötron_renk,nc_pos,nötron_çap)

    for bp_pos in elektron_konum:
        py.draw.circle(win,(0,0,255),bp_pos,10)


    for bn_pos in pozitron_konum:
        py.draw.circle(win,(0,255,0),bn_pos,10)

    #PROTON-NÖTRON SIFIRLANDIĞINDA EKRANIN ORTASINI TEMİZLEME
    if protonlar==0:
        py.draw.circle(win,arkaplanrenk,(winsize[0]/2-20,winsize[1]/2-20) , 25)

    if nötronlar==0:
        py.draw.circle(win,arkaplanrenk,(winsize[0]/2-20,winsize[1]/2+27) , 25)

    if protonlar+nötronlar==0:
        py.draw.rect(win,(arkaplanrenk),py.Rect(510,280,110,30))
        py.draw.rect(win,(255,255,255),py.Rect(winsize[0]//2-25,winsize[1]//2-80,10,5))

    #BAŞLIK
    win.blit(başlık,(370,30))

    #PROTON-NÖTRON SAYAÇ
    font = py.font.Font(None, 36)
    text = font.render(f"Proton Sayısı: {protonlar}", True, (255, 255, 255))
    win.blit(text, (1100, 110))
    text2=font.render(f"Nötron Sayısı: {nötronlar}",True,(255,255,255))
    win.blit(text2,(1100,170))

    #YENİLEME BUTONU
    yenile_text=font6.render("⟳",1,(255,255,255))
    win.blit(yenile_text,(1260,235))
    yenile_text2=font.render("Sıfırla:",1,(255,255,255))
    win.blit(yenile_text2,(1160,250))


    #ELEMENT SEMBOLÜ
    if sembolbilgi==1:
        py.draw.rect(win,(0,0,0),py.Rect(50,530,200,150))
        eksi=font.render(" -",True,(190,255,255))
        win.blit(eksi,(60,500))
        atomnumarası=font.render(f"{protonlar}",True,(190,255,255))
        win.blit(atomnumarası,(77,630))
        kütlenumarası=(protonlar)+(nötronlar)
        kütlenumarası_text=font.render(f"{kütlenumarası}",True,(190,255,255))
        win.blit(kütlenumarası_text,(77,550))

        if protonlar==0:
            yok=font5.render("-",True,(190,255,255))
            win.blit(yok,(125,530))
        if protonlar==1:
            hidrojen=font5.render("H",True,(190,255,255))
            win.blit(hidrojen,(100,540))
        if protonlar==2:
            helyum=font5.render("He",True,(190,255,255))
            win.blit(helyum,(100,540))
        if protonlar==3:
            lityum=font5.render("Li",True,(190,255,255))
            win.blit(lityum,(100,540))
        if protonlar==4:
            Element4=font5.render("Be",True,(190,255,255))
            win.blit(Element4,(100,540))
        if protonlar==5:
            Element5=font5.render("B",True,(190,255,255))
            win.blit(Element5,(100,540))
        if protonlar==6:
            Element6=font5.render("C",True,(190,255,255))
            win.blit(Element6,(100,540))
        if protonlar==7:
            Element7=font5.render("N",True,(190,255,255))
            win.blit(Element7,(100,540))
        if protonlar==8:
            Element8=font5.render("O",True,(190,255,255))
            win.blit(Element8,(100,540))
        if protonlar==9:
             Element9=font5.render("F",True,(190,255,255))
             win.blit(Element9,(100,540))
        if protonlar==10:
             Element10=font5.render("Ne",True,(190,255,255))
             win.blit(Element10,(100,540))
        if protonlar==11:
             Element11=font5.render("Na",True,(190,255,255))
             win.blit(Element11,(100,540))
        if protonlar==12:
             Element12=font5.render("Mg",True,(190,255,255))
             win.blit(Element12,(100,540))
        if protonlar==13:
             Element13=font5.render("Al",True,(190,255,255))
             win.blit(Element13,(100,540))
        if protonlar==14:
             Element14=font5.render("Si",True,(190,255,255))
             win.blit(Element14,(100,540))
        if protonlar==15:
             Element15=font5.render("P",True,(190,255,255))
             win.blit(Element15,(100,540))
        if protonlar==16:
             Element16=font5.render("S",True,(190,255,255))
             win.blit(Element16,(100,540))
        if protonlar==17:
             Element17=font5.render("Cl",True,(190,255,255))
             win.blit(Element17,(100,540))
        if protonlar==18:
             Element18=font5.render("Ar",True,(190,255,255))
             win.blit(Element18,(100,540))
        if protonlar==19:
             Element19=font5.render("K",True,(190,255,255))
             win.blit(Element19,(100,540))
        if protonlar==20:
             Element20=font5.render("Ca",True,(190,255,255))
             win.blit(Element20,(100,540))

    if sembolbilgi==0:
        artı=font.render("+",True,(190,255,255))
        win.blit(artı,(60,500))

    #ELEKTRON BULUTU
    if kapalı_açık==1:
        elektronbulutu= py.Surface((350,350),py.SRCALPHA)
        py.draw.circle(elektronbulutu,(0,0,100,128),(175,200),70)
        elektronbulutu=elektronbulutu.convert_alpha()
        elektronbulutu.set_colorkey((0,0,0))
        win.blit(elektronbulutu,(winsize[0]/2-175-20,winsize[1]/2-175-20))

    py.display.flip()

    py.time.delay(15)

py.quit()