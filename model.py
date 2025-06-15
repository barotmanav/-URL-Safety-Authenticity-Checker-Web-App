# model.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# === STEP 1: Load and clean dataset ===
df = pd.read_csv(r"C:\Users\manav\OneDrive\Desktop\project-4\SQLiXSS detection web app\malicious_phish.csv")
df = df[['url', 'type']]
df.columns = ['url', 'label']
df['label'] = df['label'].apply(lambda x: 0 if x.lower() == 'benign' else 1)

# === STEP 2: Add trusted real-world benign URLs ===
trusted_urls = pd.DataFrame({
    'url': [
        'https://www.google.com',
        'https://www.youtube.com',
        'https://www.wikipedia.org',
        'https://www.github.com',
        'https://www.facebook.com',
        'https://www.microsoft.com',
        'https://www.apple.com',
        'https://www.linkedin.com'
    ],
    'label': 0
})
df = pd.concat([df, trusted_urls], ignore_index=True)

# === STEP 3: Balance dataset ===
benign_df = df[df['label'] == 0].sample(n=10000, random_state=42)
malicious_df = df[df['label'] == 1].sample(n=10000, random_state=42)
df = pd.concat([benign_df, malicious_df]).sample(frac=1).reset_index(drop=True)

# === STEP 4: Split ===
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['label'], test_size=0.2, random_state=42)

# === STEP 5: Vectorization ===
vectorizer = TfidfVectorizer(ngram_range=(2, 5), analyzer='char_wb')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# === STEP 6: Train model ===
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# === STEP 7: Evaluate ===
y_pred = model.predict(X_test_vec)
print("\n📊 Classification Report:\n")
print(classification_report(y_test, y_pred))
print("🧩 Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# === STEP 8: Save model and vectorizer ===
joblib.dump(model, "url_model.pkl")
joblib.dump(vectorizer, "url_vectorizer.pkl")
print("✅ Model and vectorizer saved successfully!")
