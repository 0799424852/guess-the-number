from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You can change this to something more secure

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'attempts' not in session:
        session['attempts'] = 3
        session['correct_number'] = random.randint(0, 9)

    if request.method == 'POST':
        user_choice = int(request.form['choice'])
        correct_number = session['correct_number']
        attempts = session['attempts']

        if user_choice == correct_number:
            message = "You won!"
            session.pop('attempts', None)  # End game
        else:
            attempts -= 1
            session['attempts'] = attempts
            if attempts == 0:
                message = "GAME OVER!!!!"
                session.pop('attempts', None)  # End game
            else:
                message = f"You're left with {attempts} attempts."

        return jsonify({'message': message, 'attempts': attempts})

    return render_template('index.html')

@app.route('/reset')
def reset():
    session.pop('attempts', None)
    session.pop('correct_number', None)
    return jsonify({'message': 'Game reset', 'attempts': 3})

if __name__ == '__main__':
    app.run(debug=True)
