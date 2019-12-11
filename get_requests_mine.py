import requests

# Build URL
# path_url = 'http://api.postcodes.io/postcodes/'
# arguments = 'sw1v4et'
# post_codes = requests.get(path_url + arguments)
#
# # Turn this into a dictionary
# dict_response = post_codes.json()

# Getting out Longitude, Latitude, Nuts, Admin_ward:
# print('Longitude:', dict_response['result']['longitude'])
# print('Latitude:', dict_response['result']['latitude'])
# print('Nuts:', dict_response['result']['nuts'])
# print('Admin Ward:', dict_response['result']['admin_ward'])

# Build a function that returns the Latitude and Longitude of a postcode
path_url = 'http://api.postcodes.io/postcodes/'
postcode_input = input('What is your postcode? ')
postcode = requests.get(path_url + postcode_input)
dictionary_response = postcode.json()

def get_latitude():
    print('Your latitude is:', dictionary_response['result']['latitude'])
    return ''
print(get_latitude())

def get_longitude():
    print('Your longitude is:', dictionary_response['result']['longitude'])
    return ''
print(get_longitude())