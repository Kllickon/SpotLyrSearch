thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "horsepower": 200
}

del thisdict[list(thisdict.keys())[0]]

print(thisdict) 