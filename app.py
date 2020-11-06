from flask import Flask, render_template, request, flash, url_for, redirect, session

import modules.helpers as h #import du module helpers
import modules.tirage as t #import du module tirage

app = Flask(__name__)
app.secret_key = "P@ndor@p@ss8rd"

#appel à l'url http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')


#appel à l'url http://localhost:5000/aide
@app.route('/aide')
def aide():
    return render_template('aide.html')


#appel à l'url http://localhost:5000/premier-tirage
@app.route('/premier-tirage', methods=['GET', 'POST'])
def premierTirage():
    deck = ['2-h','3-h','4-h','5-h','6-h','7-h','8-h','9-h','10-h','J-h','Q-h','K-h','A-h','2-d','3-d','4-d','5-d','6-d','7-d','8-d','9-d','10-d','J-d','Q-d','K-d','A-d','2-c','3-c','4-c','5-c','6-c','7-c','8-c','9-c','10-c','J-c','Q-c','K-c','A-c','2-s','3-s','4-s','5-s','6-s','7-s','8-s','9-s','10-s','J-s','Q-s','K-s','A-s']
    
    if request.method == 'GET': #Appel à la page
        return render_template('bank.html')

    if request.method == 'POST': #post du form avec bankroll
        bank, mise_joueur = int(request.form['bankroll']), int(request.form['mise'])
        session["bank"] = bank - mise_joueur
        session["mise_joueur"] = mise_joueur

        if bank - mise_joueur >= 0:
            tirage1, new_deck = t.premier_tirage(deck)
            session["deck"] = new_deck
        return render_template('premier-tirage.html', **locals())

#appel à l'url http://localhost:5000/deuxieme-tirage
@app.route('/deuxieme-tirage', methods=['POST'])
def deuxiemeTirage():
    if request.method == 'POST': #post du form avec bankroll
        choices = []
         
        for choix in request.form:
            choices.append(choix)
        
        tirage2, deck = t.deuxieme_tirage(choices, session['deck']) #deuxième tirage
        session["deck"] = deck
        session["tirage2"] = tirage2 #stockage du deuxième tirage
        result, total = h.partie(session["mise_joueur"], tirage2, session["bank"])
        
        if total == 0:
            session["bank"] -= session["mise_joueur"]
        else:
            session["bank"] +=  total #le gain

        if session["bank"] < 0:
            session["bank"] = 0
        return render_template('deuxieme-tirage.html', **locals())

