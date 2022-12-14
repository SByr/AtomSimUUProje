import pygame as py
from yarilanma import proton_sayısı, yarılanma_ömürleri, elementi_bul, izotopu_bul

py.init()


winsize=(1366,768)

win=py.display.set_mode(winsize)




#BAŞLIK
py.display.set_caption("Atom Oluşturma Similasyonu")



#PROTON TANESİ

proton_çap=20
proton_renk=(255,255,255)
hız=0.02
protonlar=0

#NÖTRON TANESİ
nötron_çap=20
nötron_renk=(0,0,0)
nötronlar=0


font=py.font.SysFont("Times",22,bold=True)
font3 = py.font.Font("seguisym.ttf", 26,bold=True)
font4=py.font.SysFont("Times",20,bold=True)
font5=py.font.SysFont("Times",100,bold=True)
#BAŞLIK
font2=py.font.SysFont("Times",30,bold=True)
başlık=font2.render("ATOM OLUŞTURMA SİMİLATÖRÜ",1,(255,255,255))
arkaplanrenk=(11,32,39)


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

#ELEKTRON BULUTU BUTON
eb_pos=(255,460)
eb_size=(30,35)
eb_color=(100,255,255)

eb_buton=py.Rect(eb_pos,eb_size)
eb_kapalı_text=font3.render("X",1,(0x18020C))
eb_açık_text=font3.render("✓",1,(0x18020C))
kapalı_açık=0
e_b_durumu_text=font4.render("ELEKTRON BULUTU:",1,(0,0,0))


#SEMBOL BUTON
sb_pos=(50,500)
sb_size=(200,30)
sb_color=(0,0,0)

sb_buton=py.Rect(sb_pos,sb_size)
sb_text=font.render("Sembol",1,(190,255,255))

#TANECİK KONUMLARI
proton_konum=[]
protoncıkarma_konum=[]

nötron_konum=[]
nötroncıkarma_konum=[]



sembolbilgi=0

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

            if pe_buton.collidepoint(mouse_pos):
                proton_konum.append((90,130))
                p_e()
                
            if pc_buton.collidepoint(mouse_pos):
                if protonlar>=1:
                    protoncıkarma_konum.append((683,394))
                    p_c()
                else:
                    pass

            if ne_buton.collidepoint(mouse_pos):
                nötron_konum.append((90,330))
                n_e()


            if nc_buton.collidepoint(mouse_pos):
                if nötronlar>=1:
                    nötroncıkarma_konum.append((683,434))
                    n_c()

            if eb_buton.collidepoint(mouse_pos):
                kapamaaçma()

            if sb_buton.collidepoint(mouse_pos):
                sembolonoff()



    
    
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



    win.fill(arkaplanrenk)


    #BUTONLARI ÇİZ
    py.draw.rect(win,pe_color,pe_buton)
    py.draw.rect(win,pc_color,pc_buton)
    py.draw.rect(win,sb_color,sb_buton)


    win.blit(pc_text,(90,210))
    win.blit(pe_text,(90,130))
    win.blit(sb_text,(90,502))

    py.draw.rect(win,ne_color,ne_buton)
    py.draw.rect(win,nc_color,nc_buton)
    win.blit(ne_text,(90,310))
    win.blit(nc_text,(90,390))
    win.blit(e_b_durumu_text,(50,468))

        
    py.draw.circle(win,eb_color,(270,480),15)

    if kapalı_açık==0:
        win.blit(eb_kapalı_text,(262,eb_pos[1]))
    elif kapalı_açık==1:
        win.blit(eb_açık_text,(262,eb_pos[1]))
    
    #TANECİKLERİ ÇİZ
    for pe_pos in proton_konum:
        py.draw.circle(win,proton_renk,pe_pos,proton_çap)
    
    for pc_pos in protoncıkarma_konum:
        py.draw.circle(win,proton_renk,pc_pos,proton_çap)

    for ne_pos in nötron_konum:
        py.draw.circle(win,nötron_renk,ne_pos,nötron_çap)
    
    for nc_pos in nötroncıkarma_konum:
        py.draw.circle(win,nötron_renk,nc_pos,nötron_çap)

    if protonlar==0:
        py.draw.circle(win,arkaplanrenk,(winsize[0]/2-20,winsize[1]/2-20) , 25)

    if nötronlar==0:
        py.draw.circle(win,arkaplanrenk,(winsize[0]/2-20,winsize[1]/2+27) , 25)


    
 
    #BAŞLIK
    win.blit(başlık,(450,30))

    #YARİLANMA BİLGİSİ

    yarilanma_text=font.render("Atom Adı ve Yarı Ömrü:"+ str(izotopu_bul(nötronlar,protonlar)),True,(255,255,255))
    win.blit(yarilanma_text,(50,700))


    #PROTON-NÖTRON SAYAÇ
    font = py.font.Font(None, 36)
    text = font.render(f"Proton Sayısı: {protonlar}", True, (255, 255, 255))
    win.blit(text, (1100, 110))

    text2=font.render(f"Nötron Sayısı: {nötronlar}",True,(255,255,255))
    win.blit(text2,(1100,170))

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



    if kapalı_açık==1:
        elektronbulutu= py.Surface((350,350),py.SRCALPHA)
        py.draw.circle(elektronbulutu,(0,0,100,128),(175,200),70)
        elektronbulutu=elektronbulutu.convert_alpha()
        elektronbulutu.set_colorkey((0,0,0))
        win.blit(elektronbulutu,(winsize[0]/2-175-20,winsize[1]/2-175-20))

    py.display.flip()

    py.time.delay(10)

py.quit()