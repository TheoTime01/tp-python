"""
Code realisé par Perrichet Théotime
le 18/11/2021

"""
import fonctions as f

jour= int(input("Entrez le jour:"))
mois= int(input("Entrez le mois:"))
annee= int(input("Entrez l'annee:"))

if f.valid_date(jour,mois,annee): 
    print("date valide")
else:
    print("date non valide")

