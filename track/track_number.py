import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter your number :\n")
phone = phonenumbers.parse("+91" + number)
time = timezone.time_zones_for_number(phone)
cr = carrier.name_for_number(phone, "en")
reg = geocoder.description_for_number(phone, "hi")
print(phone)
print(time)
print(cr)
print(reg)
