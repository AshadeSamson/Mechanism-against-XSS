from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import pickle
from nltk.tokenize import word_tokenize
from urllib.parse import urlparse




# loading the trained model
with open('url_predict_model.pkl','rb') as trained_model:
    loaded_model = pickle.load(trained_model)


# loading the vectorizer
with open('vectorizer.pkl','rb') as saved_vectorizer:
    vectorizer = pickle.load(saved_vectorizer)


# URL preprocessing function
def preprocess_url(url):
    parsed_url = urlparse(url)
    preprocessed_url = parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path
    return preprocessed_url

# receiving request from client
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

            # Pass the tokenized url to the loaded model for prediction
            prediction = loaded_model.predict(url_vector)

            # response sent back to client
            if prediction == 'benign':
                 result = {"is_malicious": False}
                 return JsonResponse(result)
            else:
                 result = {"is_malicious": True}
                 return JsonResponse(result)
        else:
            return JsonResponse({"error": "Only POST requests are allowed."}, status=405)
            

            




         




