import phonenumbers
import folium
from myphone import number

from phonenumbers import geocoder

PhoneNumber = phonenumbers.parse(number)
location = geocoder.description_for_number(PhoneNumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = "216e1a3f2c814982a38211cbc24ffe60"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)


lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save('my-location.html')
