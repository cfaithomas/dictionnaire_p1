#************************************************Exercice 1.1*******************************
personne={"nom":"David","prenom":"phil","age":18,"ville":"Bordeaux"}
print(personne["nom"])
print(personne["prenom"])
print(str(personne["age"]))
print(personne['ville'])
#**********************************************Exercice 1.2********************************
numfavoris={"Etienne":"0240263042","Remi":"0123235689","Antoine":"0785631245"}
for key, values in numfavoris.items():
        print("nom ",key)
        print("numéro",values)
print("Le numéro d'etienne est",numfavoris["Etienne"])

#********************************************Exercice 1.3***********************************************************************
keywordspython={"print":"afficher","for":"boucle pour","if":"condition","str":"conversion en string","range":"plage de valeurs"}
for key, values in keywordspython.items():
        print(key+":",values)

#*********************************************rivieres***********************************************************************
rivieres={"Loire":"France","Colorado":"USA","Amozone":"Bresil"}

for key in rivieres.keys():
        print("Nom rivière:",key);
for value in rivieres.values():
        print("Pays:",value)
#********************************************les gens*************************************************************************
personne_a_sonder={"jen":"python","sarah":"C","edward":"ruby","phil":"python"}
personne_s={"jen":"python","phil":"python"}
for key in personne_a_sonder.keys():
        if key in personne_s.keys():
                print(key,", merci d'avoir repondu")
        else:
                print(key,", merci de répondre à notre sondage")
#*******************************************Animaux domestiques*****************************************************************
fido={"nom":"chien","proprietaire":"jack"}
charly={"nom":"oiseau","proprietaire":"phil"}
flicka={"nom":"cheval","proprietaire":"emilie"}
animauxcompagnie=[fido,charly,flicka]
for animal in animauxcompagnie:
        for key,value in animal.items():
                print(key,value)
#*****************************************Endroits Favoris***********************************************************************
favorites_places={"lea":["Montagne","Mer"],"Rene":["Mer"],"Jacques":["Campagne","Mer","Montagne"]}
for key,values in favorites_places.items():
        print(key,values);

#***************************************Numéros préférés V2**********************************************************************
numfavoris={"Etienne":["0240263042","07215863223"],"Remi":["0123235689","0245562312"],"Antoine":["0785631245","0240353317"]}
for key,values in numfavoris.items():
        print(key)
        for tel in values:
                print(tel)
#*******************************************villes*******************************************************************************
madrid={"pays":"Espagne","population":2000000,"fait":"Capitale"}
dijon={"pays":"France","population":100000,"fait":"Moutarde"}
nantes={"pays":"France","population":500000,"fait":"Capitale régionale"}
villes={"madrid":madrid,"dijon":dijon,"nantes":nantes}
for key,values in villes.items():
        print(key)
        for keyinfo,valueinfo in values.items():
                print(keyinfo,valueinfo)







