import pandas as pd
import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Read data from CSV file
data = pd.read_csv("dataset/test.csv")
data.head()


# 'url' column for URLs and 'label' column for labels
X = data['url']
y = data['type']


# function to preprocess the URL
def preprocess_url_for_training(url):
    # Convert to lowercase
    url = url.lower()

    # Remove special characters and digits
    url = re.sub(r'[^a-z\s]', '', url)

    # Tokenize and remove stopwords
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(url)
    filtered_words = [word for word in words if word not in stop_words]

    # Reconstruct URL
    preprocessed_url = ' '.join(filtered_words)

    return preprocessed_url

# X is the 'url' column of your training data
X_preprocessed = [preprocess_url_for_training(url) for url in X]


# TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Transform URLs into TF-IDF features
X_tfidf = vectorizer.fit_transform(X_preprocessed)

vector_file = 'vectorizer'
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


filename = 'url_predict_model'
pickle.dump(clf, open(filename, 'wb'))
