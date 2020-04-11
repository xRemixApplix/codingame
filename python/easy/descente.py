while True:
    hauteurs = dict()
    for i in range(8): hauteurs[i]= int(input())

    montagne = hauteur = 0
    for cle, valeur in hauteurs.items() :
        if valeur > hauteur : montagne, hauteur = cle, valeur

    print (montagne)