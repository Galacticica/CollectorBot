import json

#writes file
details = {'Name': "Bob",
           'Age': 28}

with open('convert.txt', 'w') as convert_file:
    convert_file.write(json.dumps(details))



# reading the data from the file
with open('convert.txt') as f:
    data = f.read()

print("Data type before reconstruction : ", type(data))

# reconstructing the data as a dictionary
js = json.loads(data)

print("Data type after reconstruction : ", type(js))
print(js)
testV = 'Name'
print((js[testV])[0])