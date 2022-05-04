def init(l,c,val) :
    L=[]
    for i in range(l) :
        L1 = []
        for j in range(c) :
            L1.append(val)
        L.append(L1)
    return L

def str2intlist(s) :
    L,string = [],""
    i=0
    string_1 = ""
    while i<len(s) and string_1 != "\\n" :
        if s[i] != " " and s[i]!='\\' and s[i]!='n' :
            string = string + s[i]
        elif s[i]=='\\' :
            string_1 += s[i]
        elif string_1 == "\\" :
            if s[i]=='n' :
                string_1 += s[i]
            else :
                raise Exception ("after \\ it has to be 'n'")   
        else:
            L.append(int(string))
            string = ""
        i+=1
    if s[i-1]!='n' :
        L.append(int(s[i-1]))
    return L

def load(filename) :
    f = open(filename)
    L = f.readlines()
    M = []
    for x in L :
        li = str2intlist(x)
        M.append(li)
    f.close()
    return M

def add_matrices(A,B) :
    if len(A)!=len(B) :
        raise Exception ("Les matrices ne sont pas de meme taille.")
    else :
        for i in range(len(A)) :
            if len(A[i])!=len(B[i]) :
                raise Exception ("Les matrices ne sont pas de meme taille.")
            else :
                for j in range(len(A[i])) :
                    A[i][j] += B[i][j]
        return A

def mult_matrices(A,B) :
    if len(A[0])!=len(B) :
        raise Exception("error")
    M = []
    p,n = len(B[0]),len(B)
    for i in range(len(A)) :
        line = []
        for j in range(p) :
            s = 0
            for k in range(n) :
                s+=A[i][k]*B[k][j]
            line.append(s)
        M.append(line)
    return M

def gaplist(L) :
    maxi, mini = L[0], L[0]
    for i in range(1,len(L)) :
        maxi,mini = max(maxi,L[i]),min(mini,L[i]) 
    return maxi-mini

def maxgap(M) :
    maxgap = gaplist(M[0])
    for i in range(1,len(M)) :
        maxgap = max(maxgap,gaplist(M[i]))
    return maxgap

def symetric(M) :
    test = True
    i=1
    while i<len(M) and test :
        j=0
        while j<i and test :
            test = M[i][j]==M[j][i]
            j+=1
        i+=1
    return test

def list_sorted(L) :
    n = len(L)
    test = True
    i=1
    while i<n and test==True :
        if not(L[i-1]<L[i]) :
            test=False
        i+=1
    return test

def matrix_sorted(M) :
    n,m=len(M),len(M[0])
    test,i = True,1
    list_sorted(M[0])
    value = M[0][m-1]
    while i<n and test==True :
        m1 = len(M[i])
        if M[i][0]<value or not(list_sorted(M[i])):
            test = False
        else :
            value = M[i][m1-1]
        i+=1
    return test

"""
def siamoise(n) :
    if n%2==0 or n<=2 :
        raise Exception("Siamoise : n is not valid.")
    M=init(n,n,0)
    x, y = n//2, n-1
    i = 2
    j=0
    M[i][x] = 1
    while i<(n*n)+1 :
        x1 = (x+1)%n
        y1 = (j+1)%n
        if M[y1][x1]==0 :
            M[y1][x1]=i
            x, y = x1, y1
        else :
            y-=1
            if y==-1 :
                y=n-1
            M[y][x]=i
        i+=1
    return M
print(siamoise(9))
"""


"""
Harry potter :
methode 1 : algorithe glouton 
    -> chercher le max local a chaque iteration
    -> construire le chemin d'une ligne a une autre
"""

def pos_max(L) :
    maxi = L[0]
    j, n = 1, len(L)
    for i in range (n) :
        maxi = max(maxi,L[i])
    while i<n or L[j]!=maxi :
        j+=1
    return j

def glouton(T) :
    c = len(T[0])
    n = len(T)
    j = pos_max(T[0])
    s = T[0][j]
    chemin = [j]
    for i in range(1, n) :
        jmax = j
        if j>0 and T[i][j-1]>T[i][jmax] :
            jmax = j-1
        if j<c-1 and T[i][j+1]>T[i][jmax] :
            jmax=j+1
        s+=T[i][jmax]
        chemin.append(jmax)
        j=jmax
    return (s,chemin)

def brut_force(T,i,j) :
    c=len(T[0])
    if i==len(T) :
        return T[i][j]
    else :
        m=brut_force(T,i+1,j)
        if j>0 :
            m1=brut_force(T,i+1,j-1)
            m=max(m,m1)
        if j<c-1 :
            m2 = brut_force(T,i+1,j+1)
            m=max(m,m2)
        return m+T[i][j]
        








"""
resultat = int

# 1)
resultat = c*nbr
print (resultat)

def f(c):
    resultat2 = c*nbr
    return resultat2
print(f(c))
"""
# 2)
"""
resultat = int#(input("saisir un nombre : "))
"""



