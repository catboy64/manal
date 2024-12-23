class CV:

    # initialiser les attributs du CV
    def __init__(self, nbreAnneesExperience, languesParlees, contenu):
        self.nbreAnneesExperience = nbreAnneesExperience
        self.languesParlees = languesParlees
        self.contenu = contenu
   
    # afficher les informations du CV sous forme lisible
    def __str__(self):
        return "Années d'expérience: " +str(self.nbreAnneesExperience)+"\nLangues parlées: " +str(self.languesParlees)+"\nContenu: " +str(self.contenu)
    
    # ajouter une langue à la liste des langues parlées
    def addLangue(self, langue):
        if langue not in self.languesParlees:
            self.languesParlees.append(langue)
        else:
            print("Erreur: "+langue+" est déjà dans la liste!")
   
    # retirer une langue de la liste des langues parlées
    def removeLangue(self, langue):
        if langue in self.languesParlees:
            self.languesParlees.remove(langue)
        else:
            print("Erreur: "+langue+" n'est pas dans la liste!")

    # définir le nombre d'années d'expérience
    def setNbreAnneesExperience(self, nbreAnneesExperience):
        self.nbreAnneesExperience = nbreAnneesExperience
    
    # définir le contenu du CV
    def setContenu(self, contenu):
        self.contenu = contenu

    # vérifier si le CV possède un nombre d'années d'expérience supérieur ou égal à la valeur minimum
    def validateExperience(self, minExperience):
        if minExperience <= self.nbreAnneesExperience:
            print("Nombre d'années d'expérience supérieur ou égal au nombre d'années minimums.")
            return True
        else:
            print("Nombre d'années d'expérience inférieur au nombre d'années minimums.")
            return False

    # vérifier si le candidat parle au moins un minimum de langues
    def validateLanguages(self, minLanguages):
        for langue in minLanguages:
            if langue not in self.languesParlees:
                print("Le CV ne contient pas la langue",langue)
                return False
        print("Le CV contient les langues nécessaires.")
        return True

    # vérifier si le contenu du CV contient des mots-clés avec un score total supérieur au seuil minimum
    def validateKeywords(self, keywordScores, scoreThreshold):

        # rendre le CV lisible par l'algorithme en effacant la ponctuation
        ponctuation = [',', '.', '!', '?']
        for char in ponctuation:
            self.contenu = self.contenu.replace(char, '')
        self.contenu = self.contenu.lower()
        split_contenu = self.contenu.split()
        score = 0

        for word in split_contenu:
            if word in keywordScores.keys():
                score += keywordScores[word]
        if score > scoreThreshold:
            print("Le score du CV est suffisant avec un score de:", score)
            return True
        else:
            print("Le score du CV n'est pas suffisant avec un score de:", score)
            return False

# définition des critères de validation
minExperience = 3
minLanguages = ["francais", "anglais"]
keywordScores = {
    "informatique" : 1,
    "java": 3,
    "data analyst": 3,
    "mathématique" : 7,
    "python": 4,
    "linux": 10,
    "git": 4,
    "c": 5,
    "rust": 4,
    "c++": 5,
    "web": 2
}
scoreThreshold = 10

# Test du système
liste_cv = [CV(13, ["francais", "anglais", "espagnol"], "Développeur expert en Rust, Zig, C et Assembleur, passionné par la création de logiciels efficaces et optimisés pour le bas niveau, familié avec linux."), 
            CV(12, ["francais", "anglais", "arabe"], "Programmeur passionné maîtrisant Python, C, JavaScript, HTML, CSS et Git, avec une solide compréhension en informatique, mathématique et développement web."),
            CV(4, ["francais", "anglais"], "Spécialiste en ChatGPT, technologie d'intelligence artificielle, Web 3.0, NFT, avec une expertise sur GPT-4, Claude, Gemini, Copilot, DALLE, Hugging Face, et prompt engineer certifié. ")]

for cv in liste_cv:
    print(cv)

    # vérifie si le cv est valide selon les différents critères.
    xp = cv.validateExperience(minExperience)
    lg = cv.validateLanguages(minLanguages)
    sc = cv.validateKeywords(keywordScores, scoreThreshold)
    if xp and lg and sc == True:
        print("Le CV est valide.")
    else:
        print("Le CV n'est pas valide.")
    print('\n')