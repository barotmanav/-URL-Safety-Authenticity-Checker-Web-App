# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression


from sklearn.metrics import classification_report
import joblib

#  STEP 1: Load Data
df = pd.read_csv(r"C:\Users\manav\OneDrive\Desktop\project-4\SQLiXSS detection web app\malicious_phish.csv")  # Update if your file has a different name

#  STEP 2: Check column names
print(" Available columns:", df.columns.tolist())

# Use only needed columns and rename for consistency
df = df[['url', 'type']]
df.columns = ['url', 'label']  # Rename 'type' → 'label'


#  STEP 3: Encode Labels (0 = benign, 1 = malicious/phishing/etc.) 
df['label'] = df['label'].apply(lambda x: 0 if x.lower() == 'benign' else 1)

#  STEP 4: Train-Test Split 
X_train, X_test, y_train, y_test = train_test_split(df['url'], df['label'], test_size=0.2, random_state=42)

# STEP 5: Convert URLs into Features using TF-IDF 
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

#  STEP 6: Train Model 

model = LogisticRegression(max_iter=1000)

model.fit(X_train_vec, y_train)

#  STEP 7: Evaluate Model 
y_pred = model.predict(X_test_vec)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

#  STEP 8: Save Model and Vectorizer 
joblib.dump(model, "url_model.pkl")
joblib.dump(vectorizer, "url_vectorizer.pkl")
print(" Model and vectorizer saved.")
