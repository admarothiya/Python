from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

CHOICES = ["rock", "paper", "scissor"]

def decide_winner(user, comp):
    if user == comp:
        return "draw"
    wins = {
        "rock": "scissor",     # rock beats scissor
        "paper": "rock",       # paper beats rock
        "scissor": "paper"     # scissor beats paper
    }
    return "user" if wins[user] == comp else "computer"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user_choice = data.get("user_choice", "").lower()
    if user_choice not in CHOICES:
        return jsonify({"error": "invalid choice"}), 400

    comp_choice = random.choice(CHOICES)
    result = decide_winner(user_choice, comp_choice)
    message = {
        "draw": "match draw",
        "user": "user winner🎉",
        "computer": "computer winner 🤖"
    }[result]

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": comp_choice,
        "result": result,
        "message": message
    })

if __name__ == "__main__":
    app.run(debug=True)
