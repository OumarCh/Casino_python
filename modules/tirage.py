import random


deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']


def premier_tirage(deck):
    randomlist = [];
    #Retourne une liste aléatoire de 5 cartes
    randomlist = random.sample(deck, 5) if len(deck) >= 5 else randomlist
    #Supprime les 5 cartes retournées
    [deck.remove(i) for i in randomlist]
         
    return randomlist, deck


def deuxieme_tirage(game, deck):
    nb_choices = len(game)
    card_stay_chosen = 5 - nb_choices
    randomlist = random.sample(deck, card_stay_chosen)
    #crée le deuxième tirage
    [game.append(i) for i in randomlist]
    #retourne les cartes pour le jeu final
    return game, deck


