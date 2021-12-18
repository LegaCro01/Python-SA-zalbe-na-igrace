from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkFont


i = 0
j = 0
nickname2 = str
minutaza = 0
window=Tk()
count2=0
window.title('[SA] Zalbe Na Igrace [By Lega]')
window.geometry("450x310+10+10")
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Unos')
tab_control.add(tab2, text='Popis')
tab_control.pack(expand=1, fill='both')
combo = Combobox(tab1)
Label(tab2, text='Popis igraca za kazniti', font=("Arial Bold", 9)).place(x=110, y=5)
Label(tab2, text='#', font=("Arial Bold", 8)).place(x=10, y=30) #red broj
Label(tab2, text='Nickname:', font=("Arial Bold", 8)).place(x=20, y=30) #nick
Label(tab2, text='Vrsta:', font=("Arial Bold", 8)).place(x=140, y=30) #vrsta
Label(tab2, text='Razlog:', font=("Arial Bold", 8)).place(x=220, y=30) #razlog
Label(tab2, text='Vrijeme:', font=("Arial Bold", 8)).place(x=320, y=30) #vrijeme
Label(tab2, text='WARN:', font=("Arial Bold", 8)).place(x=380, y=30) #warn

count = 0 #counter redova
            


def neutral():
    global minutaza
    minutaza=1
def pp():
    global minutaza
    minutaza=2
def rp():
    global minutaza
    minutaza=5

def clicked():
    
    global j
    global i
    global minutaza
    j=j+1
    i=i+18
    
    #Zatvori/Disarm
    if(str(combo.get())=="Zatvori"):
        Label(tab2, text=str(j)+'.', font=("Arial", 8)).place(x=10, y=30+i) #red broj
        Label(tab2, text=str(nickname.get()), font=("Arial", 8)).place(x=20, y=30+i) #nick
        Label(tab2, text=str(combo.get()), font=("Arial", 8)).place(x=140, y=30+i) #vrsta
        if (minutaza == 1):
            Label(tab2, text=str(razlog.get()), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        elif (minutaza == 2):
            Label(tab2, text=str(razlog.get()+" Pijaca/Plaza"), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        elif (minutaza == 5):
            Label(tab2, text=str(razlog.get()+" RP Zona"), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        if (int(vrijeme.get())*int(minutaza) >= 120):
            Label(tab2, text=int(vrijeme.get())*int(minutaza), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme
            Label(tab2, text='DA', font=("Arial", 8)).place(x=380, y=30+i) #warn
        else:
            Label(tab2, text=int(vrijeme.get())*int(minutaza), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme
            Label(tab2, text='Ne', font=("Arial", 8)).place(x=380, y=30+i) #warn))
            

    if(str(combo.get())=="Disarm"):
        Label(tab2, text=str(j)+'.', font=("Arial", 8)).place(x=10, y=30+i) #red broj
        Label(tab2, text=str(nickname.get()), font=("Arial", 8)).place(x=20, y=30+i) #nick
        Label(tab2, text=str(combo.get()), font=("Arial", 8)).place(x=140, y=30+i) #vrsta
        if (minutaza == 1):
            Lab
            el(tab2, text=str(razlog.get()), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        elif (minutaza == 2):
            Label(tab2, text=str(razlog.get()+" Pijaca/Plaza"), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        elif (minutaza == 5):
            Label(tab2, text=str(razlog.get()+" RP Zona"), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        if (int(vrijeme.get())*int(minutaza) >= 120):
            Label(tab2, text=int(vrijeme.get())*int(minutaza), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme
            Label(tab2, text='DA', font=("Arial", 8)).place(x=380, y=30+i) #warn
        else:
            Label(tab2, text=int(vrijeme.get())*int(minutaza), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme
            Label(tab2, text='Ne', font=("Arial", 8)).place(x=380, y=30+i) #warn
            
    #Mute
    if(str(combo.get())=="Mute"):
        Label(tab2, text=str(j)+'.', font=("Arial", 8)).place(x=10, y=30+i) #red broj
        Label(tab2, text=str(nickname.get()), font=("Arial", 8)).place(x=20, y=30+i) #nick
        Label(tab2, text=str(combo.get()), font=("Arial", 8)).place(x=140, y=30+i) #vrsta
        Label(tab2, text=str(razlog.get()), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        Label(tab2, text=int(vrijeme.get()), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme

    #Ban
    if(str(combo.get())=="Ban"):
        Label(tab2, text=str(j)+'.', font=("Arial", 8)).place(x=10, y=30+i) #red broj
        Label(tab2, text=str(nickname.get()), font=("Arial", 8)).place(x=20, y=30+i) #nick
        Label(tab2, text=str(combo.get()), font=("Arial", 8)).place(x=140, y=30+i) #vrsta
        Label(tab2, text=str(razlog.get()), font=("Arial", 8)).place(x=220, y=30+i) #razlog
        Label(tab2, text=str(vrijeme.get()+" Dana"), font=("Arial", 8)).place(x=320, y=30+i) #vrijeme
 
    #BanAd
    if(str(combo.get())=="BanAd"):
        Label(tab2, text=str(j)+'.', font=("Arial", 8)).place(x=10, y=30+i) #red broj
        Label(tab2, text=str(nickname.get()), font=("Arial", 8)).place(x=20, y=30+i) #nick
        Label(tab2, text=str(combo.get()), font=("Arial", 8)).place(x=140, y=30+i) #vrsta
       

    

    razlog.delete(0, END)
    nickname.delete(0, END)
    vrijeme.delete(0, END)
    
i=i+18

Label(tab1, text='Brzi zapis igraca', font=("Arial Bold", 11)).place(x=110, y=5)
Label(tab1, text='Nickname:').place(x=10, y=50)
nickname = Entry(tab1,width=23)
nickname.place(x=80, y=50)
Label(tab1, text='Vrsta:').place(x=40, y=80)
combo['values']= ("Disarm", "Zatvori", "Mute", "Ban", "BanAd")
combo.current(1)
combo.place(x=80, y=80)
Label(tab1, text='Razlog:').place(x=32, y=170)
razlog = Entry(tab1,width=23)
razlog.place(x=80, y=170)
Label(tab1, text='Vrijeme:').place(x=28, y=110)
vrijeme = Entry(tab1,width=5)
vrijeme.place(x=80, y=110)
neutral = Radiobutton(tab1,text='Neutral', value=1, command = neutral)
neutral.place(x=80, y=140)
pp = Radiobutton(tab1,text='Pijaca/Plaza', value=2, command = pp)
pp.place(x=145, y=140)
rp = Radiobutton(tab1,text='RP Zona', value=5, command = rp)
rp.place(x=235, y=140)
Button(tab1,text='Unesi', command =clicked).place(x=130, y=200)
Label(tab1, text='Lokacija:').place(x=25, y=140)




window.mainloop()
