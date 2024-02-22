from voiture import Voiture

mycar1 = Voiture(marque='BMW', modele='M4', puissancefiscale=5, couleur='Noir')
print(f"mycar1 : {mycar1}")

mycar2 = Voiture()
print(f"mycar2 : {mycar2}")

mycar1.set_marque('Nissan')
mycar2.set_modele('GTR')

mycar1.ajouter_option('Autopilote')
mycar1.ajouter_option('Sieges chauffants')
mycar2.ajouter_option('navigation')

print(" ")
print(f"mycar1 : {mycar1}")
print(" ")
print(f"mycar2 : {mycar2}")

mycar1.supprimer_option('Autopilote')

print(" ")
print(f"mycar1 après suppression : {mycar1}")

print(" ")
print(f"Autopilote est present? {mycar1.is_option_present('Autopilote')}")
print(f"Sieges chauffants est present? {mycar1.is_option_present('Sieges chauffants')}")

