import requests

path_url = 'http://api.postcodes.io/postcodes/'
postcode_input = input('What is your postcode? ')
postcode = requests.get(path_url + postcode_input)
dictionary_response = postcode.json()

class New_postcode():
    def __init__(self, postcode):
        self.postcode = postcode

    def get_latitude(self, file_name):
        try:
            with open(file_name, 'w+') as file_create:
                file_create.write(f"Your latitude is: {dictionary_response['result']['latitude']}")
        finally:
            print('')

