"""
print("on est quel jour ? \n")
d=int(input("jour : "))
print()
m=int(input("mois : "))
print()
y=int(input("année : "))
print()
"""
def tomorrow(d,m,y) :
    if y>2021 or (m>12 or m<1) or (y%4==1 and m==2 and d>28) or (y%4==0 and m==2 and d>29) or (d>30 and (m==4 or m==6 or m==9 or m==11)) :
        print("non valide")
    elif d==30 and (m==4 or m==6 or m==9 or m==11) :
        print(1,"/",m+1,"/",y)
    elif d==31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10) :
        print(1,"/",m+1,"/",y)
    elif d==31 and m==12 :
        print(1,"/",1,"/",y+1)
    else :
        print(d+1,"/",m,"/",y)

def list_to_9(n,t=0) :
    t+=1
    reverse = (n%10)*10+n//10
    a=n
    if a>99 :
        print(a,"is not a 2-digit positive integer")
        print(0)
    elif n==0 :
        print("no list to 9!")
        print(n)
    elif a<=9 :
        print(a)
        print(t)
    elif reverse>n :
        n,reverse = reverse,n
        a=reverse
        print(a)
        n = n-reverse
        return(list_to_9(n,t))
    elif reverse<n :
        print(a)
        n = n-reverse
        return(list_to_9(n,t))


def premier(n) :
    if n<=1 :
        raise Exception ("n must be > 1")
    else :
        nombre = n-1
        while (n%nombre)!=0:
            nombre -= 1
        return nombre==1

def premiers(n) :
    i=2
    liste = []
    while i<n :
        if premier(i) :
            liste.append(i)
        i+=1
    return liste

def factorielle(limite) :
    if limite <= 0 :
        raise Exception ("n must be positive")
    else :
        n=1
        compteur = 0
        while n<limite :
            n = n*(n+1)
            compteur+=1
        return compteur

def pgcd(a,b) :
    if a<0 or b<0 :
        raise Exception ("positif non nul")
    elif b == 0 :
        return a
    else :
        return pgcd(b,a%b)
#print(pgcd(17,4))

"""
def insert(L,x) :
    i = len(L)-1
    L.append(L[i])
    a = False
    while i>0 and a==False :
        if L[i]==x :
            raise Exception ("deja dans la liste")
        elif L[i-1]<x :
            L[i]=x
            a = True
        else :
            L[i]=L[i-1]
        i -= 1
    return L,a"""

def binaire(i) :
    liste = []
    j=i
    while i!=0 :
        if i==1 :
            liste.append(i)
            i-=1
        else :
            liste.append(i%2)
            i=i//2
    liste2 = []
    print(len(liste))
    if len(liste)<8 :
        count = 8-len(liste)
        while count < 8 :
            liste2.append(0)
            count+=1
    while len(liste)!=0 :
        a = liste.pop()
        liste2.append(a)
        i+=1
    return liste2

def complement_1(x) :
    if x<0 :
        x = -1*x
    liste = binaire(x)
    liste2 = []
    i = len(liste)
    while i != 0 :
        a=liste.pop()
        if a==1 :
            liste2.append(0)
        else :
            liste2.append(1)
        i-=1
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def complement_2(x) :
    liste = complement_1(x)
    liste2 =[]
    retenue = 1
    while len(liste)!=0 :
        a = liste.pop()
        a = a + retenue
        if a == 2 :
            a=0
            retenue=1
        elif a==1 :
            retenue=0
        liste2.append(a)
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def retourner(liste2) :
    liste=[]
    while len(liste2)!=0 :
        a = liste2.pop() 
        liste.append(a)
    return liste

def from_int(x) :
    if x>0 :
        return binaire(x)
    elif x<0 :
        return complement_2(x)
    
def equals(a,b) :
    return b==2*a
def find2 (p,l1,l2) :
    if len(l1)!=len(l2) :
        raise Exception ("error : size")
    else :
        i=0
        while not p(l1[i],l2[i]) and i!=len(l1)-1 :
            i+=1
            
        if i==len(l1) :
            raise Exception ("error : it's not working")
        else :
            return l1[i],l2[i]

def search_indexes(liste,val) :
    if val not in liste :
        return (-1,-1)
    else :
        last_ind = 0
        premier = max(liste)+1
        for i in range(len(liste)) :
            if premier != max(liste)+1 and liste[i]==val :
                last_ind = i
            elif liste[i]==val :
                premier = i
        return premier,last_ind

def multiplication_11(n_liste) :
    liste = []
    i = len(n_liste)
    liste.append(n_liste[i-1])
    retenue = 0
    resultat = 0
    while i!= 0 :
        i-=1
        if i==0 :
            resultat = n_liste[i]+retenue
            if resultat >= 10 :
                liste.append(resultat-10)
                retenue = 1
                liste.append(retenue)
            else :
                liste.append(resultat)
        else :
            resultat = n_liste[i]+n_liste[i-1]+retenue
            if resultat >=10 :
                liste.append(resultat-10)
                retenue = 1
            else :
                liste.append(resultat)
                retenue = 0
    return retourner(liste)

def mult_10(n,i) :
    if i == 0 : 
        return 1
    else :
        return n*mult_10(n,i-1)


def mult_11(n) :
    n_liste = []
    j=0
    i = int(input("nombre de chiffres de votre nombre : "))
    i=i-1
    while i!=-1 :
        n_liste.append(n//(mult_10(10,i)))
        n=n%(mult_10(10,i))
        i-=1
        j+=1
    if n_liste[0]>9 or n_liste[0]<1 :
        raise Exception("Vous ne savez pas compter.")
    else :
        liste = multiplication_11(n_liste)
        i = 0
        j=len(liste)-1
        resultat = 0
        while j>=0 :
            resultat = liste[j]*mult_10(10,i) + resultat
            i+=1
            j-=1
        return resultat
print(mult_11(56))

def int_to_list(n) :
    liste = []
    i = int(input("nombre de chiffres de votre nombre : "))
    i-=1
    while i!=0 :
        liste.append(n//(mult_10(10,i)))
        n=n%(mult_10(10,i))
        i-=1
    if n!=0 :
        return ("vous ne savez pas compter")
    return liste

def select_sort(L) :
    for i in range(len(L)-1) :
        j = i
        indice = 0
        memory = L[i]
        while j<len(L) :
            if memory>L[j] :
                memory = L[j]
                indice = j
            j+=1
        if L[i] != L[indice] :
            (L[i], L[indice]) = (L[indice],L[i])
    return L

def insert(x,L) :
    L.append(0)
    i, intermediaire = 0, 0
    while i<len(L) :
        if x<L[i] :
            intermediaire = L[i]
            L[i] = x
            x = intermediaire
        elif i==len(L)-1 and L[i]==0 :
            L[i] = x
        i+=1
    return L

def dicho_list(x,L) :
    left, right = 0, len(L)
    middle = right//2
    while left != right and L[middle]!=x :
        if x < L[middle] :
            right = middle
        else :
            left = middle + 1
        middle = (left + right)//2
    if L[middle]==x :
        return middle
    else :
        return right