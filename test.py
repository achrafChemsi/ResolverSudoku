T=[[0]*9]*9
for i in range(9):
    for j in range(9):
        T[i][j]=5
def test(T):
    s=0
    for i in range(9):
        if 0 in T[i]:
            s = 1
    return s
if test(T)==0:
    print(True)


    while test(T)==1:
    for i in range(9):
        for j in range(9):
            if len(probability(T,i,j))==1:
                T[i][i] = probability(T,i,j)      
    affichage(T)
