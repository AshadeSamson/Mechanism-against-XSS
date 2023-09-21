from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import re
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from django.shortcuts import render
from urllib.parse import urlparse




# loading the trained model
with open('url_predict_model.pkl','rb') as trained_model:
    loaded_model = pickle.load(trained_model)


# loading the vectorizer
with open('vectorizer.pkl','rb') as saved_vectorizer:
    vectorizer = pickle.load(saved_vectorizer)


# Create your views here.
# the API request handler that takes in the URL
# and passes it to the ML model 
# and returns a response


def preprocess_url(url):
    parsed_url = urlparse(url)
    preprocessed_url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
    return preprocessed_url

@csrf_exempt
def check_url(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            url = data.get('url')

            # Preprocess the URL
            preprocessed_url = preprocess_url(url)
            
            # Tokenize the URL
            words = word_tokenize(preprocessed_url)
            preprocessed_url = ' '.join(words)

            # Vectorize the preprocessed URL
            url_vector = vectorizer.transform([preprocessed_url])

            prediction = loaded_model.predict(url_vector)

            if prediction == 'benign':
                 result = {"is_malicious": False}
                 return JsonResponse(result)
            else:
                 result = {"is_malicious": True}
                 return JsonResponse(result)
        else:
            return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
            

            




         




