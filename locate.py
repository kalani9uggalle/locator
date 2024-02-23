from time import time
from numpy import number
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your phone number: ")
phone = phonenumbers.parse(number)
time = timezone.time_zones_for_number(phone)
car = carrier.name_for_number(phone, 'en')
reg = geocoder.description_for_number(phone, 'en')

print("Phone:", phone)
print("time:", time)
print("carrier:", car)
print("region:", reg)
# There are more lines below which are not fully visible
