from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.json.get("message").lower()

    # Basic rule-based replies
    if "hello" in user_input:
        reply = "Hello! How can I help you today?"
    elif "bye" in user_input:
        reply = "Goodbye! Take care."
    elif "your name" in user_input or "who are you" in user_input:
        reply = "I'm MiniBot, your AI friend!"

    # Fun: Joke
    elif "joke" in user_input:
        reply = "Why don’t scientists trust atoms? Because they make up everything! 😂"

    # Fun: Weather (offline)
    elif "weather" in user_input:
        reply = "It's always sunny in the console world ☀️ (offline version!)"

    # Fun: Fact
    elif "fun fact" in user_input:
        reply = "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey in Egypt and it was still edible!"

    # Smart: Simple calculation
    elif "calculate" in user_input or "what is" in user_input:
        try:
            expression = user_input.replace("calculate", "").replace("what is", "").strip()
            result = eval(expression)
            reply = f"The answer is: {result}"
        except:
            reply = "Sorry, I couldn't calculate that. Try something like 'what is 12 / 4'."

    # Fallback
    else:
        reply = "Hmm... I didn't understand that. Try asking me for a joke, weather, fun fact, or a simple math problem!"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
