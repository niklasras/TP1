class Voiture:
    def __init__(self, marque='Porsche', modele='GT3RS', puissancefiscale=5, couleur='Vert'):
        self.__marque = marque
        self.__modele = modele
        self.__puissancefiscale = puissancefiscale
        self.__couleur = couleur
        self.__options = []


    def get_marque(self):
        return self.__marque

    def get_modele(self):
            return self.__modele

    def get_puissancefiscale(self):
        return self.__puissancefiscale

    def get_couleur(self):
        return self.__couleur

    def get_options(self):
        return self.__options

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def set_puissancefiscale(self, nouvelle_puissancefiscale):
        self.__puissancefiscale = nouvelle_puissancefiscale

    def set_couleur(self, nouvelle_couleur):
        self.__couleur = nouvelle_couleur

    def set_options(self, nouvelles_options):
        self.__options = nouvelles_options

    def ajouter_option(self, opt):
        self.__options.append(opt)

    def supprimer_option(self, opt):
        if opt in self.__options:
            self.__options.remove(opt)

    def is_option_present(self, opt):
        return opt in self.__options

    def __str__(self):
        return f"Voici les caractéristiques de cette voiture:\n- Marque : {self.__marque}\n- Modele : {self.__modele}\n- Couleur : {self.__couleur}\n- Puissance : {self.__puissancefiscale}\n- Options: {self.__options}"
