from .models import Quote
import urllib.request, json

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['BASE_URL']

def get_quote():
    with urllib.request.urlopen(base_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        if quote_response:
            author = quote_response.get('author')
            quote = quote_response.get('quote')
        
            new_quote = Quote(author, quote)

            return new_quote
    

    default_quote = Quote("Kennedy", "Writing is a way of talking without being interrupted")
    return default_quote
