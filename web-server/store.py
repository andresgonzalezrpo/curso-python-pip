import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text) ## this is a string
    categories =  r.json() # is used to parse the response content of an HTTP request and return it as a JSON object
    #This method converts the response content to a Python dictionary if the content is in JSON format.

    for category in categories:
        print(category["name"])
        

