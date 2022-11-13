import tkinter as tk
from tkinter import ttk

win=tk.Tk()
win.geometry("1024x568")
win.title("Atom Similasyonu")
win.configure(bg="#9590A8")
win.minsize(800,600)

başlık=tk.Label(win,text=("Atom Çekirdeği Oluştur"),bg="#9590A8",fg="#18020C",font="Times 22 bold")
başlık.place(relx=0.5,anchor="n")

#proton ekleme fonksiyonu
def p_e():
    label.config(text="Proton Eklendi",font="times 15")
    
label=tk.Label(win,fg="black",bg="white")
label.place(relx=0.25,rely=0.2)


proton_ekle=tk.Button(win,text=("Proton Ekle"),bg="#BBCBCB",fg="#634B66",font="times 17 ",command=p_e,border=0)
proton_ekle.place(relx=0.05,rely=0.2)

#Proton çıkarma fonksiyonu
def p_c():
    label2.config(text="Proton Çıkartıldı",font="times 15")

label2=tk.Label(win,fg="black",bg="white")
label2.place(relx=0.25,rely=0.3)

proton_çıkar=tk.Button(win,text=("Proton Çıkar"),bg="#BBCBCB",fg="#634B66",font="times 17 ",command=p_c,border=0)
proton_çıkar.place(relx=0.05,rely=0.3)


#nötron ekleme fonksiyonu
def n_e():
    label_nötronekle.config(text="Nötron Eklendi",font="times 15")
    
label_nötronekle=tk.Label(win,fg="black",bg="white")
label_nötronekle.place(relx=0.25,rely=0.7)

nötron_ekle=tk.Button(win,text=("Nötron Ekle"),bg="#BBCBCB",fg="#634B66",font="times 17 ",command=n_e,border=0)
nötron_ekle.place(relx=0.05,rely=0.7)



#Nötron Çıkartma Fonksiyonu
def n_c():
    label_nötroncikar.config(text="Nötron Çıkartıldı",font="times 15")

label_nötroncikar=tk.Label(win,fg="black",bg="white")
label_nötroncikar.place(relx=0.25,rely=0.8)

nötron_çıkar=tk.Button(win,text=("Nötron Çıkar"),bg="#BBCBCB",fg="#634B66",font="times 17 ",command=n_c,border=0)
nötron_çıkar.place(relx=0.05,rely=0.8)
















win.mainloop()