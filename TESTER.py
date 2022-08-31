
import my_sudoku as h
T=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[8,0,9,0,0,0,0,4,3],[0,0,1,0,0,0,8,3,0],[3,0,0,0,0,0,0,0,0],[0,0,8,0,0,0,4,0,0],[1,0,0,0,0,2,0,0,0],[0,0,2,0,0,0,0,6,0],[0,0,0,0,0,0,0,0,0]]
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
                            if (s == True)  :
                                print("############     "+str(r+1)+"    ##########")
                                print("ligne:   "+str(i+1)+"    colonne:     "+str(j+1))
                                print(y)
                                T[i][j] = y[r]
                                print("-----------")
                                h.affichage(T)
                                v=1
                                break
                            elif p==True :
                                print("############     "+str(r+1)+"    ##########")
                                print("ligne:   "+str(i+1)+"    colonne:     "+str(j+1))
                                print(y)
                                T[i][j] = y[r]
                                print("-''''''''''''-")
                                h.affichage(T)
                                v=1
                                break
                                
                else:
                    T[i][j] = y[0]
                    print("ligne:   "+str(i+1)+"    colonne:     "+str(j+1))
                    print(y)
                    print("++++++++++")
                    h.affichage(T)
                    v=1
                    break
            if v==1:
                break
        print('\n#####################\n') 
        h.affichage(T)
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
                    
                    print("ligne:   "+str(i+1)+"    colonne:     "+str(j+1))
                    print(t)
                    print(h.pplp(z,T))
                    T[i][j]=h.pplp(z,T)
                    print(T[i][j])
                    print("*****************")
                    h.affichage(T)
                    v=1
                    break
            if v==1:
                break
h.affichage(T)
import tkinter
form = tkinter.Tk()
form.title('resolver sudoku')
form.mainloop()


input('Press enter to exit ...')
                    
                
                
                
    

