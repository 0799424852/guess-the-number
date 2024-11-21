from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Temporary in-memory game state
game_state = {
    "attempts": 3,
    "correct_number": random.randint(0, 9),
}

@app.route('/', methods=['GET', 'POST'])
def index():
    print("GET request received")

    # Initialize the game state for a GET request
    if request.method == 'GET':
        game_state["attempts"] = 3  # Reset attempts on page load
        game_state["correct_number"] = random.randint(0, 9)

    # Handle POST request when the user submits a guess
    if request.method == 'POST':
        print("POST request received")
        user_choice = int(request.form['choice'])
        correct_number = game_state["correct_number"]
        attempts = game_state["attempts"]

        # Check the guess
        if user_choice == correct_number:
            message = "You won!"
            game_state["attempts"] = 0  # End game
        else:
            attempts -= 1
            game_state["attempts"] = attempts
            if attempts == 0:
                message = "GAME OVER!!!!"
                game_state["attempts"] = 0  # End game
            else:
                message = f"You're left with {attempts} attempts."

        return jsonify({'message': message, 'attempts': attempts})

    return render_template('index.html')


@app.route('/reset')
def reset():
    # Reset game state
    game_state["attempts"] = 3
    game_state["correct_number"] = random.randint(0, 9)
    return jsonify({'message': 'Game reset', 'attempts': 3})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 debug=True)