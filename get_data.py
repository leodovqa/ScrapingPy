import json

# load the data into an element
with open('results.json', encoding='utf-8') as json_file:
    file_contents = json_file.read()

# load the json to a string
json_data = json.loads(file_contents)

# extract an element in the response
for x in json_data:
    print("Title: " + x['Title'])
    print("Price: " + x["Price"])
    print("Link: " + x["Link"])
    print("Image: " + x["Image Source"]+"\n")
