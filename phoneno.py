# simple program which gives information about  particular mobile number with their carrier informationa and country where we have imported a package phonenumbers




import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

phone = phonenumbers.parse("+917558792274")

print(geocoder.description_for_number(phone, 'en'))
print(carrier.name_for_number(phone, 'en'))