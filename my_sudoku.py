""" fonction remplis T ,n nbr de valeur """
#my_sudoku
def remplir(T):
    n=int(input("entrer le nbr de valeur connus sur ce sudoku: "))
    for i in range(n):
        ligne=int(input("entrer la ligne de la valeur  connus: " ))
        col = int(input("entrer la colonne de la valeur  connus: " ))
        T[ligne-1][col-1] = int(input("entrer la valeur connus: "))
    return T
"""afichage """
def affichage(T):
    for i in range(9):
        for j in range(9):
            print(T[i][j], end=" ")
        print()
""" """ """not""" """ """
def not_nb(T,i,j):
    if T[i][j]==0:
        non=[]
        s=i//3
        q=j//3
        for r in range(3*s,3*s+3):
            for t in range(3*q,3*q+3):
                if T[r][t]!=0:
                    non+=[T[r][t]]
        for r in range(9):
            if T[i][r]!=0:
                non+=[T[i][r]]
            if T[r][j]!=0:
                non+=[T[r][j]]
        return non
    return [0]
""" valeur possible """
def probability(T,i,j):
    prob=[]
    for r in range(9):
        if (r+1) in not_nb(T,i,j):
            continue
        else:
            prob += [r+1]
    return prob
""" not """
def not_ligne_colonne(T,n,i,j):
    for r in range(9):
        if (r==i) or (n in not_nb(T,r,j)) or (T[r][j]!=0):
            s=True
        else :
            s=False
            break
        if (r==j) or (n in not_nb(T,i,r)) or (T[i][r]!=0):
            s=True
        else :
            s=False
            break
    return s          
""" augmentation du not bloc """
def trouvable(T,n,i,j):
    s=i//3
    q=j//3
    for r in range(3*s,3*s+3):
        for t in range(3*q,3*q+3):
            if ((r==i)and (t==j)) or (n in not_nb(T,r,t)) or (T[r][t]!=0):
                s=True
            else :
                s=False
                break
        if s==False:
            break
    return s
""" test s'il existe un 0 """
def test(T):
    s=0
    for i in range(9):
        if 0 in T[i]:
            s = 1
    return s

""" nbr de zero sur matrice """
def test0(T):
    s=0
    for i in range(9):
        for j in range(9):
            if T[i][j]==0:
                s+=1
    return s    
""" la plus petite liste de proba qui contient le nombre qui appartient a un grand nombre de liste de proba  """
""" la lpus petite liste qui contient n"""
def min_liste(T):
    s=8
    z=0
    for i in range(9):
        for j in range(9):
            if len(probability(T,i,j))<s and T[i][j]==0:
                s=len(probability(T,i,j))
                z = probability(T,i,j)
    return z
""" n qui appartient a un nombre de probabilite """                
def nbr_des_liste(n,T):
    s=0
    for i in range(9):
        for j in range(9):
            g = probability(T,i,j)
            if n in g:
                s +=1
    return s
"""   """
def pplp(L,T):
    s=0
    k=0
    for i in L:
        if nbr_des_liste(i,T)>=s :
            k=i
            s=nbr_des_liste(i,T)
    return k
            
        
        
    
    
    
