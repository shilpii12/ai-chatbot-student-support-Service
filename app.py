from flask import Flask, render_template, request, jsonify
from google import genai

app = Flask(__name__)

# Replace with your NEW Gemini API Key
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=user_message
        )

        reply = response.text

    except Exception as e:
        reply = f"Sorry, error: {str(e)}"

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)