import json

def articles_call():
    with open('data/newsapi_ap_example.json') as f:
        data = json.load(f)
        return data['articles']

