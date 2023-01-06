import pygame as py

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

font=py.font.SysFont("Times",22,bold=True)

#BAŞLIK
font2=py.font.SysFont("Times",30,bold=True)
başlık=font2.render("ATOM OLUŞTURMA SİMİLATÖRÜ",1,(255,255,255))
arkaplanrenk=(11,32,39)


#PROTON EKLE-ÇIKAR BUTONU BUTONLARI
pe_pos=(50,120)
pe_size=(200,50)
pe_color=(64,121,140)
pc_pos=(300,120)
pc_size=(200,50)
pc_color=(64,121,140)


pe_buton=py.Rect(pe_pos,pe_size)
pe_text=font.render("Proton Ekle",1,(0x18020C))

pc_buton=py.Rect(pc_pos,pc_size)
pc_text=font.render("Proton Çıkar",1,(0x18020C))





protoncıkarma_positions=[]
proton_positions=[]

def p_e():
    global protonlar
    protonlar+=1

def p_c():
    global protonlar
    protonlar-=1

çalıştır=True
while çalıştır:



    for event in py.event.get():
        if event.type==py.QUIT:
            çalıştır=False
        if event.type== py.MOUSEBUTTONDOWN:
            mouse_pos=py.mouse.get_pos()

            if pe_buton.collidepoint(mouse_pos):
                proton_positions.append((90,130))
                p_e()

            if pc_buton.collidepoint(mouse_pos):

                if protonlar>=1:
                    protoncıkarma_positions.append((683,394))
                    p_c()
                else:
                    pass
    
    for i, pe_pos in enumerate(proton_positions):
        xyol=winsize[0]/2 - proton_çap - pe_pos[0]
        yyol=winsize[1]/2 - proton_çap - pe_pos[1]

        xhareket=xyol*hız*2
        yhareket=yyol*hız*2


        proton_positions[i]=(pe_pos[0]+ xhareket,pe_pos[1]+yhareket)
    
    for i, pc_pos in enumerate(protoncıkarma_positions):


        if protonlar>=0:
            xyol=winsize[1]*2 - proton_çap - pc_pos[0]
            yyol=winsize[0]/2 - proton_çap - pc_pos[1]

            xhareket=xyol*hız
            yhareket=yyol*hız


            protoncıkarma_positions[i]=(pc_pos[0]+ xhareket,pc_pos[1]+yhareket)



    win.fill(arkaplanrenk)

    py.draw.rect(win,pe_color,pe_buton)
    py.draw.rect(win,pc_color,pc_buton)

    for pe_pos in proton_positions:
        py.draw.circle(win,pe_color,pe_pos,proton_çap)
    
    for pc_pos in protoncıkarma_positions:
        py.draw.circle(win,pc_color,pc_pos,proton_çap)
    
    
    if protonlar==0:
        py.draw.circle(win,arkaplanrenk,(winsize[0]/2,winsize[1]/2) , 50)

    win.blit(pc_text,(338,130))
    win.blit(pe_text,(90,130))
    
    #BAŞLIK
    win.blit(başlık,(450,30))


    #PROTON SAYAÇ
    font = py.font.Font(None, 36)
    text = font.render(f'Proton Sayısı: {protonlar}', True, (255, 255, 255))
    win.blit(text, (1100, 110))
    py.display.flip()

    py.time.delay(10)

py.quit()