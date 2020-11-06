import pandas as pd
import modules.tirage as t
import modules.combinaisons as comb

c = comb.Combinaison()


def calculer_gain(final_game: list, money: int):
    if c.quinte_flush_royale(final_game) == True:
        total = money*250
        result = "Quite Flush Royale !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.quinte_flush(final_game) == True:
        total = money*50
        result = "Quite Flush !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.carre(final_game) == True:
        total = money*25
        result = "Carre !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.full(final_game) == True:
        total = money*9
        result = "Full !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.flush(final_game) == True:
        total = money*6
        result = "Flush !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.quinte(final_game) == True:
        total = money*4
        result = "Quinte !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.brelan(final_game) == True:
        total = money*3
        result = "Brelan !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.double_paire(final_game) == True:
        total = money*2
        result = "Double paire !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    elif c.carre(final_game) == True:
        total = money*1
        result = "Paire !!! Vous gagnez " + str(total) + "euros !"
        return total, result
    else:
        total = 0
        result = "C'est perdu ! Retentez votre chance !"
        return total, result
    
    
def partie(money: int, hand: list, bankroll: int):
    total, result = calculer_gain(hand, money)
    bankroll = bankroll - money
    bankroll += total
    return result, total


def video_poker():
    bankroll = int(input("Bank: "))
    player = int(input("Faites vos jeux: "))
    
    while bankroll - player >= 0:
        result, bankroll = partie(player, bankroll)
        print(result)
        print("Bank: " + str(bankroll))
        if bankroll == 0:
            print("Game Over")
            break
        else:
            player = int(input("Faites vos jeu"))
            if bankroll - player < 0:
                print("Mise trop élévée !")
                player = int(input("Faites vos jeux"))


