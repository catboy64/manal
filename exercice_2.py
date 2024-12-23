import matplotlib.pyplot as plt
import numpy as np

class Image:
    def __init__(self, matrice):
        # vérifier si matrice est bidimensionnel
        if len(matrice) < 2:
            print("La matrice n'est pas bidimensionnel.")
            return 0

        self.matrice = matrice
    
    def __str__(self):
        return str(self.matrice)

    def dessiner_histogramme(self):
        plt.title("Image principale")
        plt.xlabel("colonnes")
        plt.ylabel("lignes")
        plt.imshow(self.matrice, interpolation='nearest')
        plt.show()

    def chercher_image(self, sous_image):
        co = 0 # compteur utilisé pour savoir si la matrice est trouvé
        #parcourir la grande image
        for x in range(len(self.matrice)):
            for y in range(len(self.matrice[0])):
                #quand le premier pixel est trouvé
                if self.matrice[x][y] == sous_image[0][0]:
                    #parcourir sous image la comparer avec grande image
                    for i in range(len(sous_image)):
                        for j in range(len(sous_image[0])):
                            #comparer les matrices
                            if self.matrice[x+i][y+j] != sous_image[i][j]:
                                co = 0 #remettre a 0 le compteur
                                break
                            else:
                                co+=1 #ajouter 1 au compteur quand 1 pixel est correspondant
                    if co == len(sous_image[0])+len(sous_image): # quand l'image est trouv
                        return (x,y)


# Exemple de matrices pour les images
matrice_principale = np.array([
    [1, 8, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])
matrice_sous_image = np.array([
    [8, 9],
    [13, 14]
])

img = Image(matrice_principale)
# afficher les deux matrices
print("Image principale:")
print(matrice_principale)
print("\nSous-image:")
print(matrice_sous_image)
cord = img.chercher_image(matrice_sous_image)
if cord: # si sous-image est trouvée
    print("\nSous-image trouvée aux coordonnées: ", cord)
img.dessiner_histogramme()
