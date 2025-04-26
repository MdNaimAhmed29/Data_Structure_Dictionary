"""
dictonary/object/map-almost used everywhere{}
    -keys()
    -values()
    -finding each value for the respective key
    -items()
    -copy()
    -update()
    -pop()
    -clear()
    -len()
    -update()
    -get()

---------------------------------------------------------

jSON -javascript object notation-Uses
    -common interchange format
    -python, js, dart, java
    -back end to front end(B2C)
    -back end to back end(B2B)
    -rest API development
    -rest API implement
    -payment gateway
    -sms API
 **object to json string conversion->json.dumps()
 **json string to object conversion->json.loads()
"""

#map/dictonary

adlof_hitler = {
    "Name": "Adlof Hitler",
    "Age": 56,
    "Country": "Germany",
    "Occupation": "President",
    "Gender": "Male",
}
print(adlof_hitler)
print(adlof_hitler.keys())
print(adlof_hitler.values())
print(adlof_hitler.items())
print(adlof_hitler.copy())
print(adlof_hitler.pop('Gender'))
print(len(adlof_hitler))
print(adlof_hitler['Name'])
print(adlof_hitler.get('Age'))
adlof_hitler.update(
    {
        "Age": 76,
        "Country": "USA",
    }
)
print(adlof_hitler)


#JSON-javascript object notation

import json

adlof_hitlerJSON = json.dumps(adlof_hitler, indent=4)
print(adlof_hitlerJSON)

ahobject = json.loads(adlof_hitlerJSON)
print(ahobject)

peoples = [
    {"name" : "A", "age" : 24},
    {"name" : "B", "age" : 25},
    {"name" : "C", "age" : 26},
    {"name" : "D", "age" : 27},
    {"name" : "E", "age" : 28},
    {"name" : "F", "age" : 29},
    {"name" : "G", "age" : 30},
]

peoplesJSONArray = json.dumps(peoples, indent=4)
print(peoplesJSONArray)
