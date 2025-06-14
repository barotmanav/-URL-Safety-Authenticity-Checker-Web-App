# app.py

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model and TF-IDF vectorizer
model = joblib.load("url_model.pkl")
vectorizer = joblib.load("url_vectorizer.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    url_input = ""

    if request.method == "POST":
        url_input = request.form["url"]
        try:
            # Transform URL into feature vector
            url_vec = vectorizer.transform([url_input])
            result = model.predict(url_vec)[0]

            # Interpret prediction
            if result == 0:
                prediction = "🔴 Malicious or Suspicious URL"
            else:
                prediction = "🟢 Safe URL"
        except Exception as e:
            prediction = f"⚠️ Error: {str(e)}"

    return render_template("index.html", prediction=prediction, url=url_input)

if __name__ == "__main__":
    app.run(debug=True)
