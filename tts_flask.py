from flask import Flask, request, send_file
from gtts import gTTS

app = Flask(__name__)

@app.route("/speak", methods=["POST"])
def speak():
    data = request.get_json()

    # Validate request
    if not data or "text" not in data:
        return {"error": "Missing 'text' in request body"}, 400

    text = data["text"]
    tts = gTTS(text=text, lang="en", tld="us")
    
    # Save and return audio file
    output_file = "output.mp3"
    tts.save(output_file)

    return send_file(output_file, mimetype="audio/mpeg", as_attachment=True, download_name="output.mp3")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)