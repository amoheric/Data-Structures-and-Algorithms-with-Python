import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


reviews = pd.read_csv('amazon_reviews.csv')

# Preprocessing and feature extraction
# [Insert text preprocessing and TF-IDF vectorization steps here]
vectorizer = TfidfVectorizer()
tfidf_features = vectorizer.fit_transform(reviews['review_text'])


# Splitting dataset
X_train, X_test, y_train, y_test = train_test_split(tfidf_features, reviews['Sentiment'], test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print(classification_report(y_test, predictions))
