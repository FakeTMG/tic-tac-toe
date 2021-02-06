from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint

ActivePlayer=1
p1=[] #what player one selected
p2=[] #what player two selected
root=Tk()
root.title("X/O:Player 1")
style=ttk.Style()
style.theme_use("classic")
style.configure("TButton", background='#427949')
style.map("Info.TButton", background=[('disabled', '#6d1b1b')])

bu1=ttk.Button(root,text='')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: ButtonClick(1))

bu2=ttk.Button(root,text='')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: ButtonClick(2))
bu3=ttk.Button(root,text='')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: ButtonClick(3))

bu4=ttk.Button(root,text='')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5=ttk.Button(root,text='')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6=ttk.Button(root,text='')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7=ttk.Button(root,text='')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8=ttk.Button(root,text='')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9=ttk.Button(root,text='')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: ButtonClick(9))

def ButtonClick(id):
    global ActivePlayer
    global p1
    global p2
    if(ActivePlayer==1):
        SetLayout(id,"X")
        p1.append(id)
        root.title("X/O:Player 2")
        ActivePlayer=2
        print("P1:{}".format(p1))
        AutoPlay()
    elif(ActivePlayer==2):
        SetLayout(id,"O")
        p2.append(id)
        root.title("X/O:Player 1")
        ActivePlayer=1
        print("P2:{}".format(p2))
    CheckWinner()
def SetLayout(id,PlayerSymbol):
    if id==1:
        bu1.config(text=PlayerSymbol)
        bu1.state(['disabled'])
        bu1.configure(style='Info.TButton')
    elif id==2:
        bu2.config(text=PlayerSymbol)
        bu2.state(['disabled'])
        bu2.configure(style='Info.TButton')
    elif id==3:
        bu3.config(text=PlayerSymbol)
        bu3.state(['disabled'])
        bu3.configure(style='Info.TButton')
    elif id==4:
        bu4.config(text=PlayerSymbol)
        bu4.state(['disabled'])
        bu4.configure(style='Info.TButton')
    elif id == 5:
        bu5.config(text=PlayerSymbol)
        bu5.state(['disabled'])
        bu5.configure(style='Info.TButton')
    elif id == 6:
        bu6.config(text=PlayerSymbol)
        bu6.state(['disabled'])
        bu6.configure(style='Info.TButton')
    elif id == 7:
        bu7.config(text=PlayerSymbol)
        bu7.state(['disabled'])
        bu7.configure(style='Info.TButton')
    elif id == 8:
        bu8.config(text=PlayerSymbol)
        bu8.state(['disabled'])
        bu8.configure(style='Info.TButton')
    elif id == 9:
        bu9.config(text=PlayerSymbol)
        bu9.state(['disabled'])
        bu9.configure(style='Info.TButton')
def CheckWinner():
    Winner=-1
    if(1 in p1) and (2 in p1) and (3 in p1):
        Winner=1
    if(1 in p2) and (2 in p2) and (3 in p2):
        Winner=2
    if(4 in p1) and (5 in p1) and (6 in p1):
        Winner=1
    if(4 in p2) and (5 in p2) and (6 in p2):
        Winner=2
    if(7 in p1) and (8 in p1) and (9 in p1):
        Winner=1
    if(7 in p2) and (8 in p2) and (9 in p2):
        Winner=2
    if(1 in p1) and (4 in p1) and (7 in p1):
        Winner=1
    if(1 in p2) and (4 in p2) and (7 in p2):
        Winner=2
    if(2 in p1) and (5 in p1) and (8 in p1):
        Winner=1
    if(2 in p2) and (5 in p2) and (8 in p2):
        Winner=2
    if(3 in p1) and (6 in p1) and (9 in p1):
        Winner=1
    if(3 in p2) and (6 in p2) and (9 in p2):
        Winner=2
    if(3 in p1) and (5 in p1) and (7 in p1):
        Winner=1
    if(3 in p2) and (5 in p2) and (7 in p2):
        Winner=2
    if(1 in p1) and (5 in p1) and (9 in p1):
        Winner=1
    if(1 in p2) and (5 in p2) and (9 in p2):
        Winner=2
    if Winner==1:
        messagebox.showinfo(title="Congrats",message="Player 1 is the Winner!!")
        exit()
    elif Winner==2:
        messagebox.showinfo(title="Congrats",message="Player 2 is the Winner!!")
        exit()

def AutoPlay():
    global p1
    global p2
    EmptyCells=[]
    for cell in range(9):
        if (not((cell+1 in p1) or (cell+1 in p2))):
            EmptyCells.append(cell+1)
    RandIndex=randint(0,len(EmptyCells)-1)
    if (1 in p1) and (2 in p1) or (6 in p1) and (9 in p1) or (5 in p1) and (7 in p1):
        ButtonClick(3)
    elif (4 in p1) and (5 in p1) or (3 in p1) and (9 in p1):
        ButtonClick(6)
    elif (7 in p1) and (8 in p1) or (3 in p1) and (6 in p1) or (1 in p1) and (5 in p1):
        ButtonClick(9)
    elif (1 in p1) and (4 in p1) or (3 in p1) and (5 in p1) or (8 in p1) and (9 in p1):
        ButtonClick(7)
    elif (2 in p1) and (5 in p1) or (7 in p1) and (9 in p1):
        ButtonClick(8)
    elif (1 in p1) and (3 in p1) or (5 in p1) and (8 in p1):
        ButtonClick(2)
    elif (4 in p1) and (6 in p1) or (2 in p1) and (8 in p1) or (3 in p1) and (7 in p1) or (1 in p1) and (9 in p1):
        ButtonClick(5)
    elif (1 in p1) and (7 in p1) or (5 in p1) and (6 in p1):
        ButtonClick(4)
    elif (2 in p1) and (3 in p1) or (4 in p1) and (7 in p1) or (5 in p1) and (9 in p1):
        ButtonClick(1)
    else:
        ButtonClick(EmptyCells[RandIndex])


root=mainloop()