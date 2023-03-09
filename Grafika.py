from tkinter import *
def klikker (event):
    global k
    k+=1
    lbl1.configure(text=k)
    

def klikkermaha (event):
    global k
    k-=1
    lbl1.configure(text=k)#если меняем лбл1 то будет выводиться в другой элемент

def text_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END) #2,7

    

k=0

aken=Tk()
aken.geometry("400x500")
aken.title("Minu esimine aken")
lbl=Label(aken,text="Elemendid", bg="gold",fg="#AA4A44",font="Roboto 20", height=5,width=15)
lbl1=Label(aken,font="Roboto 20", bg="gold",fg="#AA4A44")
btn=Button(aken,text="Vajuta siia",font="Arial 24",relief=RAISED)#relief = SUNKEN, RAISED, GROOVE
ent=Entry(aken,fg="blue",bg="lightblue",width=15,font="Roboto 20",justify=CENTER)#justify-выравнивание
btn.bind("<Button-1>",klikker)#lkm
btn.bind("<Button-3>",klikkermaha)#pkm
ent.bind("<Return>",text_to_lbl)#enter
lbl1.pack()
lbl.pack()#выводит надпись на экран
btn.pack(side=LEFT)
ent.pack(side=LEFT)

aken.mainloop() # благодаря этой функции окно не закрывается сразу и ожидает действия пользователя
