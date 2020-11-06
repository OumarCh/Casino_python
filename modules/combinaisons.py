import pandas as pd

class Combinaison:
    def __init__(self):
        pass


    def verifier_game(self, game: list):
        dic = {}
        keys = [1,2,3,4,5]
        value = []
        color = []
        
        for i,k in zip(game,keys):
            dic[k] = i.split('-')
        for key in dic.keys():
            value.append(dic[key][0])
            color.append(dic[key][1])
                
        return value, color


    def convert_card(self, listing: list):
        for e,i in zip(listing, range(0,5)):
            try:
                listing[i] = int(e)
            except:
                if e == 'J':
                    listing[i] = 11
                if e == 'Q':
                    listing[i] = 12
                if e == 'K':
                    listing[i] = 13
                if e == 'A':
                    listing[i] = 1
        return listing


    def quinte_flush_royale(self, game: list):
        winner = ['10', 'J', 'Q', 'K', 'A']
        value, color = self.verifier_game(game)
        #retourne True si quinte_flush_royale sinon False        
        result = True if sorted(winner) == sorted(value) and color.count(color[0]) == 5 else False
        return result


    def quinte_flush(self, game: list):
        value, color = self.verifier_game(game)
        value = self.convert_card(value)
        value = sorted(value)
        following = []
        [following.append('True') for e,i in zip(value[0:-1], range(len(value)-1)) if e+1 == value[i+1]]
        #retourne True si quinte flush sinon False        
        result = True if following.count('True') == 4 and color.count(color[0]) == 5 else False
        return result

        
    def carre(self, game: list):
        value, color = self.verifier_game(game)
        first_value = pd.Series(value)
        unique_value = first_value.unique()
        counter = []
        [counter.append(value.count(i)) for i in unique_value]
        #retourne True si carre sinon False  
        result = True if len(unique_value) == 2 and sorted(counter) == [1, 4] else False
        return result
        
        
    def full(self, game: list):
        value, color = self.verifier_game(game)
        first_value = pd.Series(value)
        unique_value = first_value.unique()
        counter = []
        [counter.append(value.count(i)) for i in unique_value]
        #retourne True si full sinon False  
        result = True if len(unique_value) == 2 and sorted(counter) == [2, 3] else False
        return result

        
    def flush(self, game: list):
        value, color = self.verifier_game(game)
        #retourne True si flush sinon False
        result = True if color.count(color[0]) == 5 else False
        return result
        

    def quinte(self, game: list):
        value, color = self.verifier_game(game)
        value = self.convert_card(value)
        value = sorted(value)
        following = []
        [following.append('True') for e,i in zip(value[0:-1], range(len(value)-1)) if e+1 == value[i+1]]
        #retourne True si quinte sinon False
        result = True if following.count('True') == 4 or value == [1, 10, 11, 12, 13] else False
        return result
        
        
    def brelan(self, game: list):
        value, color = self.verifier_game(game)
        first_value = pd.Series(value)
        unique_value = first_value.unique()
        counter = []
        [counter.append(value.count(i)) for i in unique_value]
        #retourne True si brelan sinon False
        result = True if len(unique_value) == 3 and sorted(counter) == [1, 1, 3] else False
        return result
        
        
    def double_paire(self, game: list):
        value, color = self.verifier_game(game)
        first_value = pd.Series(value)
        unique_value = first_value.unique()
        counter = []
        [counter.append(value.count(i)) for i in unique_value]
        #retourne True si double_paire sinon False
        result = True if len(unique_value) == 3 and sorted(counter) == [1, 2, 2] else False
        return result
        

    def paire(self, game: list):
        value, color = self.verifier_game(game)
        first_value = pd.Series(value)
        unique_value = first_value.unique()
        counter = []
        [counter.append(value.count(i)) for i in unique_value]
        #retourne True si paire sinon False
        result = True if len(unique_value) == 4 and sorted(counter) == [1, 1, 1, 2] else False
        return result