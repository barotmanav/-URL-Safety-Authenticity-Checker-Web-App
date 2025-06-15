# app.py

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load("url_model.pkl")
vectorizer = joblib.load("url_vectorizer.pkl")

# Whitelist of trusted domains
trusted_domains = [
    "youtube.com", "google.com", "github.com", "wikipedia.org",
    "facebook.com", "microsoft.com", "apple.com", "linkedin.com",
    "instagram.com", "twitter.com", "openai.com"
]

def is_whitelisted(url):
    return any(domain in url for domain in trusted_domains)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probability = None
    url_input = ""

    if request.method == "POST":
        url_input = request.form.get("url", "").strip().lower()
        try:
            # Step 1: Check whitelist
            if is_whitelisted(url_input):
                prediction = "🟢 Safe — Trusted website (whitelisted)."
                probability = None
            else:
                # Step 2: Predict using ML model
                vector = vectorizer.transform([url_input])
                result = model.predict(vector)[0]
                proba = model.predict_proba(vector)[0][1]

                # Step 3: Interpret confidence
                if proba > 0.75:
                    prediction = "🔴 Unsafe — This URL is likely malicious."
                elif proba < 0.3:
                    prediction = "🟢 Safe — This URL appears legitimate."
                else:
                    prediction = "🟡 Suspicious — Cannot confidently classify."

                probability = f"Confidence of being malicious: {proba:.2%}"
        except Exception as e:
            prediction = f"⚠️ Error: {e}"

    return render_template("index.html", prediction=prediction, probability=probability, url=url_input)

if __name__ == "__main__":
    app.run(debug=True)
