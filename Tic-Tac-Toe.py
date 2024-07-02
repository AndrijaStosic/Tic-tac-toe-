from tkinter import *
from tkinter import messagebox

igrac = 1

def jedan():
    global igrac
    if igrac % 2 == 0:
        pos1.config(text="O", state=DISABLED)
    else:
        pos1.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def dva():
    global igrac
    if igrac % 2 == 0:
        pos2.config(text="O", state=DISABLED)
    else:
        pos2.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def tri():
    global igrac
    if igrac % 2 == 0:
        pos3.config(text="O", state=DISABLED)
    else:
        pos3.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def cetiri():
    global igrac
    if igrac % 2 == 0:
        pos4.config(text="O", state=DISABLED)
    else:
        pos4.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def pet():
    global igrac
    if igrac % 2 == 0:
        pos5.config(text="O", state=DISABLED)
    else:
        pos5.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def sest():
    global igrac
    if igrac % 2 == 0:
        pos6.config(text="O", state=DISABLED)
    else:
        pos6.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def sedam():
    global igrac
    if igrac % 2 == 0:
        pos7.config(text="O", state=DISABLED)
    else:
        pos7.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def osam():
    global igrac
    if igrac % 2 == 0:
        pos8.config(text="O", state=DISABLED)
    else:
        pos8.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def devet():
    global igrac
    if igrac % 2 == 0:
        pos9.config(text="O", state=DISABLED)
    else:
        pos9.config(text="X", state=DISABLED)
    igrac += 1
    proveri_pobedu()

def proveri_pobedu():
    sanse_za_nereseno=0
    dobici = [[pos1, pos2, pos3],
        [pos4, pos5, pos6],
        [pos7, pos8, pos9],
        [pos1, pos4, pos7],
        [pos2, pos5, pos8],
        [pos3, pos6, pos9],
        [pos1, pos5, pos9],
        [pos3, pos5, pos7]]

            
    for kombinacija in dobici:
        simboli = [button.cget("text") for button in kombinacija]
        if simboli == ["X", "X", "X"]:
            sanse_za_nereseno=1
            messagebox.showinfo("Winner is player X")

            resetuj_tablu()
            return
        elif simboli == ["O", "O", "O"]:
            sanse_za_nereseno=1
            messagebox.showinfo("Winner is player O")
            resetuj_tablu()
            return
        elif sanse_za_nereseno == 1:
            messagebox.showinfo("It is draw")
            resetuj_tablu()
            return
  
        
def resetuj_tablu():
    global igrac
    igrac = 1
    for dugme in [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9]:
        dugme.config(text="", state=NORMAL)


prozor = Tk()
prozor.title("Tic Tac Toe")
prozor.geometry("250x250")
prozor.config(bg="peachpuff")

pos1 = Button(text="", width=11, height=5, command=jedan)
pos1.grid(row=0, column=0)

pos2 = Button(text="", width=11, height=5, command=dva)
pos2.grid(row=0, column=1)

pos3 = Button(text="", width=11, height=5, command=tri)
pos3.grid(row=0, column=2)

pos4 = Button(text="", width=11, height=5, command=cetiri)
pos4.grid(row=1, column=0)

pos5 = Button(text="", width=11, height=5, command=pet)
pos5.grid(row=1, column=1)

pos6 = Button(text="", width=11, height=5, command=sest)
pos6.grid(row=1, column=2)

pos7 = Button(text="", width=11, height=5, command=sedam)
pos7.grid(row=2, column=0)

pos8 = Button(text="", width=11, height=5, command=osam)
pos8.grid(row=2, column=1)

pos9 = Button(text="", width=11, height=5, command=devet)
pos9.grid(row=2, column=2)

mainloop()