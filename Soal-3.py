import requests
import json

provNameMilea       = "JAWA BARAT"
cityNameMilea       = "BANDUNG"
subDistNameMilea    = "BANDUNG WETAN"
urbanNameMilea      = "CITARUM"

provNameDilan       = "BANTEN"
cityNameDilan       = "TANGERANG"
subDistNameDilan    = "CISAUK"
urbanNameDilan      = "SAMPORA"

with open ("prov.json", "r") as jsonFile:
    dataProv = json.load(jsonFile)

with open ("postalcode.json", "r") as jsonFile:
    dataPost = json.load(jsonFile)

for key, name in dataProv.items():
    if name == provNameMilea:
        provCodeMilea = key

for key, name in dataProv.items():
    if name == provNameDilan:
        provCodeDilan = key

index = 0
for item in range(len(dataPost[provCodeMilea])):

    if dataPost[provCodeMilea][index]['urban'] == urbanNameMilea:
        kodePosMilea = dataPost[provCodeMilea][index]['postal_code']
    index +=1

index2 = 0
for item in range(len(dataPost[provCodeDilan])):

    if dataPost[provCodeDilan][index2]['urban'] == urbanNameDilan:
        kodePosDilan = dataPost[provCodeDilan][index2]['postal_code']
    index2 +=1

apiKey = "7CcAbVeeIzPagE3yvmpUqwT24nBRYGdDmCb3mNWENLiFVzevJ8dW7pWTSFVZyhm8"
url    = f"http://www.zipcodeapi.com/rest/{apiKey}/distance.json/{kodePosDilan}/{kodePosMilea}/km"

data = requests.get(url)
distance = data.json()

print(f"Kode Pos lokasi Dilan adalah: {kodePosDilan}")
print(f"Kode Pos lokasi Milea adalah: {kodePosMilea}")
print(f"Jarak Dilan & Milea adalah {distance['distance']} km")
