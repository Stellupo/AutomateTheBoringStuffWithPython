import random, math

def resultat (number):
    global argent #cette valeur, tu dois la chercher dans le scope global
    if number==case:
        somme = 3*(argent)
        print ('Vous avez gagné !')
    elif (number)%2==0 and (case)%2==0: #si le nombre choisi et la case sont paires
        somme = 1/2*(argent)
        print("La roulette s'est arrêtée sur un nombre noir et vous avez misé sur du noir,vous gagnez en partie")
    elif (number)%2==1 and (case)%2==1: #si le nombre choisi et la case sont impaires
        somme = 1/2*(argent)
        print("La roulette s'est arrêtée sur un nombre rouge et vous avez misé sur du rouge, vous gagnez en partie")
    else:
        somme = 0
        print('Vous avez perdu')

    Newsomme = math.ceil(int(somme))
    print ("Pour ce tour, vous avez gagné", Newsomme, "$")
    argent = Newsomme
    return Newsomme # retiens que ce résultat dans toute la fonction, mon programme !
    #le code après return n'est jamais exécuté ! la fonction s'arrête là

argentTotal=-1
while argentTotal<=0: #tant que le portefeuille est inf ou égal à 0, on redemande la valeur
    print ("Combien avez-vous de $ dans votre portefeuille ce soir?")
    try:
        argentTotal = int(input())
        argent = None #la variable est globale car décrite dans le code global !
    except ValueError:
        print("Veuillez ne tapez que des valeurs nominales, sinon la partie s'arrête")
        argentTotal=-1
        continue

while True:
        print('Combien souhaitez vous miser en $?')
        try:
            argent=int(input())
            if argent>argentTotal:
                print("Vous ne pouvez pas miser plus que ce que vous n'avez dans votre portefeuille")
                continue
            elif argent<=0:
                print("Vous devez miser quelque chose, cette valeur est négative ou nulle")
            else:
                print("Vous misez",argent,"$")

        except ValueError:
            print("Veuillez ne tapez que des valeurs nominales, sinon la partie s'arrête")
            continue

        argentTotal=argentTotal-argent
        number = -1

        while number>=50 or number<0: #tant que le nombre n'est pas valide, on répéte le tour
            print('Maintenant, choississez un numéro entre 0 et 49')
            try:
                number=int(input())
            except ValueError:
                print("Veuillez ne tapez que des valeurs nominales, sinon la partie s'arrête")
                continue
            if number>=50 or number<0:
                print ("Le nombre est soit en dessous de 0 soit au dessus de 49!")

        print('Vous avez choisi le numéro ',number,'.Bien, maintenant la roulette se lance!')
        case = random.randrange(50)
        print("La bille s'est arrêtée sur le numéro", case)
        argentTotal= argentTotal + resultat(number)

        print("Il vous reste", argentTotal,"$")

        if argentTotal<=0: # Inf ou égal à 0 au lieu d'égal à 0
            print ("Il ne vous reste plus d'argent, revenez demain !")
            break






