# spam_classifier.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Load dataset (you can download from https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
url = "https://raw.githubusercontent.com/justmarkham/pycon-2016-tutorial/master/data/sms.tsv"
df = pd.read_table(url, header=None, names=['label', 'message'])

# Convert labels to binary (ham=0, spam=1)
df['label'] = df.label.map({'ham': 0, 'spam': 1})

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['message'], df['label'], test_size=0.2, random_state=42)

# Convert text messages into numeric feature vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Predict and evaluate
y_pred = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Try with your own input
while True:
    user_input = input("\nEnter a message to classify (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    user_vec = vectorizer.transform([user_input])
    prediction = model.predict(user_vec)
    print("Prediction: SPAM" if prediction[0] else "Prediction: NOT SPAM")
