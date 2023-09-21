import pandas as pd
import pickle
import re
from urllib.parse import urlparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Read data from CSV file
data = pd.read_csv("dataset/test.csv")

# 'url' column for URLs and 'type' column for labels
X = data['url']
y = data['type']

# function to preprocess the URL
def preprocess_url_for_training(url):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Combine the components of the URL
    preprocessed_url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
    
    # Tokenize the URL
    words = word_tokenize(preprocessed_url)
    
    # Reconstruct the URL with tokens
    preprocessed_url = ' '.join(words)
    
    return preprocessed_url

# Preprocess URLs
X_preprocessed = [preprocess_url_for_training(url) for url in X]

# TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Transform URLs into TF-IDF features
X_tfidf = vectorizer.fit_transform(X_preprocessed)

vector_file = 'vectorizer.pkl'
pickle.dump(vectorizer, open(vector_file, 'wb'))

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Train Random Forest classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

model_file = 'url_predict_model.pkl'
pickle.dump(clf, open(model_file, 'wb'))
