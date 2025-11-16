import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import os


df = pd.read_csv('data/sample_tweets.csv')


X = df['text']
y = df['label']


vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)


X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.3, random_state=42)


model = MultinomialNB()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


acc = accuracy_score(y_test, y_pred)
print(f"✅ Accuracy: {acc*100:.2f}%")


cm = confusion_matrix(y_test, y_pred, labels=["positive","negative"])


os.makedirs('images', exist_ok=True)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["positive","negative"], yticklabels=["positive","negative"])
plt.title("Confusion Matrix")
plt.savefig('images/confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

