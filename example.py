
# Import the import module
import requests
# Getting a webpage
r = requests.get('https://dog.ceo/api/breeds/list/all')
# Now you have a Response object callred r.
# and you can get info from this object
r.status_code

r.headers['content-type']
# Request decode content from server. Unicode charsets are decodeded
r.encoding

# Text encodeing guessed by Request is used when you access r.text
r.text

r.json()
