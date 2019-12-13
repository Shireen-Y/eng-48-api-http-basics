import requests

path_url = 'http://api.postcodes.io/postcodes/'
postcode_input = input('What is your postcode? ')
postcode = requests.get(path_url + postcode_input)
dictionary_response = postcode.json()

ask_file = input('Please name the file you would like to insert your postcode data into: ')
file_name = ask_file + '.txt'

try:
    with open(file_name, 'w+') as file_created:
        file_created.write(f"Postcode: {dictionary_response['result']['postcode']}" + "\n")
        file_created.write(f"Longitude: {dictionary_response['result']['longitude']}" + "\n")
        file_created.write(f"Latitude: {dictionary_response['result']['latitude']}" + "\n")
        file_created.write(f"Nut: {dictionary_response['result']['nuts']}" + "\n")
        file_created.write(f"Admin ward: {dictionary_response['result']['admin_ward']}" + "\n")

except TypeError as error:
    print('Please ensure you have all the correct information')

finally:
    print('All complete')

