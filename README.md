# Mechanism-against-XSS

A security meachanism that prevents user from visiting malicious URLs in their broswer.

An ML model was trained using the Random forest classifier and incorporated into a Django web server, the Django API receives requests
with URLs in the body of the request and passes it to the trained model for prediction, It returns the prediction of the URL as being malicious or not as the response to the request.
The final client-side project will be a web browser extension communicating with the Django API.
