from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# loading the trained model
with open('url_predict_model','rb') as trained_model:
    loaded_model = pickle.load(trained_model)


# loading the vectorizer
with open('vectorizer','rb') as saved_vectorizer:
    vectorizer = pickle.load(saved_vectorizer)


# Create your views here.
# the API request handler that takes in the URL
# and passes it to the ML model 
# and returns a response

@csrf_exempt
def check_url(request):
        if request.method == 'POST':
            data = json.loads(request.body)
            url = data.get('url')


            def preprocess_url_for_app(url):
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
            

            processed_url = preprocess_url_for_app(url)

            url_tfidf = vectorizer.transform([processed_url])

         


            prediction = loaded_model.predict(url_tfidf)
            print(prediction)
            is_malicious = bool(prediction[0])

            result = {"is_malicious": is_malicious}
            return JsonResponse(result)
        else:
            return JsonResponse({"error": "Only POST requests are allowed."}, status=405)

