import my_sudoku as h
T=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
h.remplir(T)
h.affichage(T)
k=0
while (k!=h.test0(T))and (h.test(T)==1):
    while (k!=h.test0(T))and (h.test(T)==1):
        k=h.test0(T)
        v=0
        for i in range(9):
            for j in range(9):
                y=h.probability(T,i,j)
                z=len(y)
                if not(z==1)  :
                    if T[i][j]==0:
                        s = False
                        p = False
                        y = h.probability(T,i,j)
                        z = len(y)
                        for r in range(z):
                            s = h.trouvable(T,y[r],i,j)
                            p = h.not_ligne_colonne(T,y[r],i,j)
                            if (s == True) or (p==True)  :
                                T[i][j] = y[r]
                                v=1
                                break
                else:
                    T[i][j] = y[0]
                    v=1
                    break
            if v==1:
                break
    if h.test(T)==0:
        break
    else:
        k=h.test0(T)
        z=h.min_liste(T)
        v=0
        for i in range(9):
            for j in range(9):
                t=h.probability(T,i,j)
                if t==z and T[i][j]==0:
                    T[i][j]=h.pplp(z,T)
                    v=1
                    break
            if v==1:
                break
h.affichage(T)
"""
import tkinter
from tkinter import ttk
form = tkinter.Tk()
form.title('resolver sudoku')
form.geometry('900x900')
form.config( background="lightblue")



remp = ttk.Label(form, text="combient de nombre")
ent = ttk.Entry(form)


remp.config(background='orange',font=("arial",15),padding="5")
ent.config(font=('arial',15))


remp.pack()
ent.pack()

form.mainloop()
input('Press enter to exit ...')"""
                    
                
                
                
    

