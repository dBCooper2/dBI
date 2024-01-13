import json

def get_account_data(path: str)->dict: # Gets api key, account_number, redirect_uri, and token path and returns them as a dict from a specified filename and path
    with open(path) as f: # f = file
        return json.load(f) # return file contents as a json