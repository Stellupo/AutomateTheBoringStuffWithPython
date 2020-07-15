#Ce programme vous dit bonjour et me demande mon nom
print('Hello World !')
print ('Quel est votre nom?')#Demandez le nom
myName=input()
print('Il est bon de vous retrouver,'+myName)
print('la longueur de votre nom est:')
print(len(myName))
print('Quel est votre âge')#Demandez l'âge
myAge=input()
print('Tu auras '+str(int(myAge)+1)+'ans dans un an.')