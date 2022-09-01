# Track phone number
#### pip install phonenumbers 
import phonenumbers
# import geocoder to get country
from   phonenumbers import geocoder
# get phonenumber from user
phone = input("Please enter phone number in format +1123456789")

phonenumber = phonenumbers.parse(phone)

# Print location for given phone number
print(geocoder.description_for_number(phonenumber,'en')) 