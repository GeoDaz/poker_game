from flask import Flask, render_template, request, escape, session, redirect
from functions import multiple_draw, get_coeff

app = Flask(__name__)
app.secret_key = "PokerMachine$$$"

HAND_NB = 5
POST = 'POST'
GET = 'GET'


def DECK():
    return [
        '2-h', '3-h', '4-h', '5-h', '6-h', '7-h', '8-h', '9-h', '10-h',
        'J-h', 'Q-h', 'K-h', 'A-h',
        '2-d', '3-d', '4-d', '5-d', '6-d', '7-d', '8-d', '9-d', '10-d',
        'J-d', 'Q-d', 'K-d', 'A-d',
        '2-c', '3-c', '4-c', '5-c', '6-c', '7-c', '8-c', '9-c', '10-c',
        'J-c', 'Q-c', 'K-c', 'A-c',
        '2-s', '3-s', '4-s', '5-s', '6-s', '7-s', '8-s', '9-s', '10-s',
        'J-s', 'Q-s', 'K-s', 'A-s'
    ]


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
    hand, deck = multiple_draw(DECK(), cards=[])
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
    session['bankroll'] = session['bankroll'] - \
        session['bet'] + session['bet'] * coeff
    return render_template(
        'second-draw.html',
        hand=hand,
        bankroll=session['bankroll'],
        bet=session['bet'],
        coeff=coeff,
        score_text=score_text
    )


app.run(debug=True)
