# -URL-Safety-Authenticity-Checker-Web-App# 🔐 URL Safety & Authenticity Checker

> A Flask-based web app that uses a machine learning model to detect whether a given website URL is safe, suspicious, or malicious. Trained on a real-world phishing dataset from Kaggle.

---

## 🚀 Features

- 🌐 Web interface to input and analyze any URLss
- 🧠 ML model trained on 600k+ malicious & benign URLs
- 🧪 Detects phishing, suspicious domains (like g00gle.com), and patterns like SQLi/XSS
- ⚡ Works locally with no internet/API needed
- 📁 Clean and lightweight codebase for learning and extension

---

## 🖼️ Demo


https://github.com/user-attachments/assets/ac445eba-649e-4516-9367-a08c1a234193


Output: 🔴 Malicious or Suspicious URL



## 📁 Project Structure

url-safety-checker/
├── app.py # Flask web server
├── train_model.py # Model training script
├── malicious_phish.csv # Dataset from Kaggle
├── url_model.pkl # Trained ML model
├── url_vectorizer.pkl # TF-IDF vectorizer
├── templates/
│ └── index.html # Frontend interface
└── README.md # This file ✨



## 📊 Dataset Used

- **Source**: [Kaggle – Malicious and Benign URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- Contains URLs labeled as:
  - `benign`, `malware`, `phishing`, `defacement`
- Preprocessed into binary labels:
  - `benign` = Safe → 0
  - everything else = Malicious → 1

---

## ⚙️ How It Works

1. User submits a URL.
2. The app vectorizes the URL using `TfidfVectorizer`.
3. A pre-trained Random Forest model predicts whether it's malicious or not.
4. The result is displayed on the screen.

---

## 🧠 Getting Started

### 🔧 Install dependencies
```bash
pip install flask pandas scikit-learn joblib
🧠 Train the ML model

python train_model.py
🚀 Run the web app

python app.py
Visit http://127.0.0.1:5000 in your browser.

📌 Example Input

http://g00gle.com/login.php?user=admin
Prediction: 🔴 Malicious or Suspicious URL

🧠 Model Info
Vectorizer: TfidfVectorizer

Model:  LogisticRegression

Accuracy: ~96–98% on validation set

Training Time: ~1–2 mins on 10k samples

💡 Ideas for Future
🌍 Deploy to Hugging Face Spaces or Render

🌐 WHOIS or domain trust checks

🛡️ Add heuristics for XSS, SQLi, and Obfuscated URLs

📲 Convert to browser extension or mobile app

👨‍💻 Author
Manav Barot
🧠 Machine Learning | 🕸️ Web Developer | 🛡️ Security Curious
📬 [mbarot2008@gmail.com] 
🔗 [LinkedIn=manavbarot] 
