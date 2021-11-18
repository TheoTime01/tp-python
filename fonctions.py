
#exo_1
def  bissextile(annee):
    """
   Test si une année est bissextile

   :param annee : annee à tester
   :return: True si annee est bissextile, False sinon
   """
    if(annee%4==0 and annee%100!=0 or annee%400==0):
        return True
    else:
        return False


def m(mois,annee):
    """
    Test le nombre de jour dans un mois
    :param annee : mois a tester
    :param annee : annee à tester
    :return: le nombre de jours dans le mois testé
   """
    if mois== 1 or mois== 3 or mois== 5 or mois== 7 or mois== 8 or mois== 10 or mois== 12:
        return 31
    elif mois== 4 or mois==6 or mois==9 or mois==11:
        return 30
    else:
        if bissextile(annee)== True:
            return 29
        else:
            return 28

def valid_date(date,mois,annee):
    d=m(mois,annee)
    if date>= 1 and date <= d:
        return True
    else:
        return False

#exo_2

def mesImpots(revenu):
    R=[0,10085,25711,73157,158123]
    T= [0,0.11,0.30,0.41,0.45]
    n =0
    impot=0
    for i in range(1,len(R)):
        if revenu< R[i] and revenu>R[i-1]:
            n=i-1
        elif revenu >= R[4]:
            n=4
    if n==0:
        return 0
    else:
        o = (revenu-R[n])*T[n]   
        for k in range(n,0,-1):
            impot+= (R[k]-1-R[k-1])*T[k-1]     
        return o + impot

        

#exo3

def multiplication(B,C):
    A=[]
    m=0
    k=0
    while k<len(B):
        m=0
        for i in B:
            aii=0
            ind=0
            indC=0      
            for j in C:
                aii+=i[ind]*j[indC+k]
                ind+=1
            indC+=1
            if len(A)!=len(B):
                A.append([aii])
            else:
                A[m].append(aii)
                m+=1
        k+=1
    return A


def affichage(A):
    for i in A:
        print (i)

#exo4

#exo5
def syracuse(N):
    L=[]
    while N>1:
        if N%2==0:
            N=N/2
        else:
            N=N*3 +1
        L.append(N)
    return L


def altitudemax(N):
    b=max(syracuse(N))
    return b

def tempsdevol(N):
    return len(syracuse(N))






