"""
Code realisé par Perrichet Théotime
le 18/11/2021

"""
import fonctions as f

tempsvolmax=0
altitudemax=0
ind1=0
ind2=0

for i in range(1,1001):
    if f.tempsdevol(i)> tempsvolmax:
        tempsvolmax=f.tempsdevol(i)
        ind1=i
    if f.altitudemax(i)> altitudemax:
        altitudemax=f.altitudemax(i)
        ind2=i

print("l'altitude la plus haute est",ind2)
print("le temps de vol max est",ind1)