from tkinter import *
def klikker (event):
    global k
    k+=1
    lbl1.configure(text=k)
    if k %2==0:
        tahvel.itemconfigure(img_kast=img1)
    else:
        tahvel.itemconfigure(img_kast=img)
def klikkermaha (event):
    global k
    k-=1
    lbl1.configure(text=k)#если меняем лбл1 то будет выводиться в другой элемент

def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END) #2,7

def valik():
    val=var.get()
    ent.insert(END,val)
    pass

def checklist_to_l(event):
    v1=var1.get()
    v2=var2.get()
    jarjend=[var1,var2]
    l.delete(0,1)
    for item in jarjend:
        l.insert(END, item)
k=0

aken=Tk()
aken.geometry("400x500")
aken.title("Minu esimine aken")
aken.iconbitmap("appicon2.ico")
f=Frame(aken,bg="blue")

var=IntVar() #stringVar()
r1=Radiobutton(f,text="Esimine",font="Algerian 20",variable=var,value=1, command=valik)
r2=Radiobutton(f,text="Teine",font="Algerian 20",variable=var,value=2, command=valik)
r3=Radiobutton(f,text="Kolmas",font="Algerian 20",variable=var,value=3, command=valik)
var1=StringVar()
var2=StringVar()
c1=Checkbutton(f,text="Esimene",font="Arial 24",variable=var1,onvalue="Esimene on valitud",offvalue="Esimine on peidetud")
c2=Checkbutton(f,text="Teine",font="Arial 24",variable=var2,onvalue="Teine on valitud",offvalue="Teine on peidetud")
l=Listbox(f,height=2,width=20)
lbl=Label(f,text="Elemendid", bg="gold",fg="#AA4A44",font="Roboto 20", height=5,width=15)
lbl1=Label(f,font="Roboto 20", bg="gold",fg="#AA4A44")
btn=Button(f,text="Vajuta siia",font="Arial 24",relief=RAISED)#relief = SUNKEN, RAISED, GROOVE
ent=Entry(f,fg="blue",bg="lightblue",width=15,font="Roboto 20",justify=CENTER)#justify-выравнивание

tahvel=Canvas(aken,width=260,height=260,bg="gold")
img=PhotoImage(file="kass2.png").subsample(6)
img1=PhotoImage(file="cat.png").subsample(2)
img_kast=tahvel.create_image(2,2,image=img,anchor=NW)

btn.bind("Button-1",checklist_to_l)
btn.bind("<Double-1>",klikker)#lkm
btn.bind("<Button-3>",klikkermaha)#pkm
ent.bind("<Return>",text_to_lbl)#enter

ob=[lbl1,lbl,btn,ent,r1,r2,r3,c1,c2]
for item in ob:
    item.pack()
c1.deselect()
c2.deselect()
f.grid(row=0,column=0)
tahvel.grid(row=0,column=1)
aken.mainloop() # благодаря этой функции окно не закрывается сразу и ожидает действия пользователя
