# Mechanism-against-XSS

A security meachanism that prevents user from visiting malicious URLs in their broswer.

An ML model was trained using the Random forest classifier and incorporated into a Django web server, the Django API receives requests
with URLs in the body of the request and passes it to the trained model for prediction, it hten returns a response of the URL as being
malicious or not.
The final client-side project is going to be a web browser extension that communicates with the Django API.
