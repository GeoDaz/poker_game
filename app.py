# imports
from flask import Flask, render_template, request, escape, session, redirect
from modules.draw import HAND_NB, init_deck, multiple_draw
from modules.score import get_coeff

# const
POST = 'POST'
GET = 'GET'

# app
app = Flask(__name__)
app.secret_key = "PokerMachine$$$"


# routes
@app.route('/')
def home():
    return render_template(
        'index.html',
        bankroll=session['bankroll'] if 'bankroll' in session else None
    )


@app.route('/reset', methods=[GET])
def reset():
    session.clear()
    return redirect("/", code=302)


@app.route('/first-draw', methods=[GET])
@app.route('/second-draw', methods=[GET])
def go_home():
    return redirect("/", code=302)


@app.route('/first-draw', methods=[POST])
def first_draw():
    # banroll check
    bankroll = int(escape(request.form['bankroll']))
    bet = int(escape(request.form['bet']))
    if not bankroll or not bet or bankroll < 0 or bet < 0:
        return render_template(
            'error.html',
            error="La cagnotte et la mise sont requises."
        )
    if bet > bankroll:
        return render_template(
            'error.html',
            error="La mise doit être inférieure a la cagnotte."
        )
    session['bankroll'] = bankroll
    session['bet'] = bet
    # draw
    hand, deck = multiple_draw(init_deck(), cards=[])
    session['deck'] = deck
    return render_template('first-draw.html', hand=hand)


@app.route('/second-draw', methods=[POST])
def second_draw():
    # get hand
    hand = []
    for key in request.form:
        hand.append(escape(key))
    # draw
    hand, deck = multiple_draw(session['deck'], HAND_NB - len(hand), hand)
    # second draw
    coeff, score_text = get_coeff(hand)
    session['bankroll'] = session['bankroll'] - session['bet'] \
        + session['bet'] * coeff
    return render_template(
        'second-draw.html',
        hand=hand,
        bankroll=session['bankroll'],
        bet=session['bet'],
        coeff=coeff,
        score_text=score_text
    )


# run debug
app.run(debug=True)
