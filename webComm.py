import requests

url = "https://www.google.com"
# respObj = requests.get(url)
#
# print("Status code",respObj.status_code)
#
# if respObj.status_code == 200:
#     print("Response:", respObj.content)
# else:
#     print("Unable to get data")

serviceUrl = "http://api.geonames.org/postalCodeSearchJSON?postalcode=9011&maxRows=10&username=shree"

respObj = requests.get(serviceUrl)

if respObj.status_code == 200:
    jsonResp = respObj.json()
    print("JSON:", jsonResp)

    listOfPlaces = jsonResp['postalCodes']
    for placeObj in listOfPlaces:
        city = placeObj['adminName2']
        placeName = placeObj['placeName']
        print("City: {}, Place: {}".format(city,placeName))
else:
    print("Unable to get data", respObj.status_code)

####

import ftplib
ftp = ftplib.FTP("localhost")

import smtplib

smtpObj = smtplib.SMTP("gmail.com")
smtpObj.sendmail()