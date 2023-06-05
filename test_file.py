import json
import re

# load the data into an element
with open('results.json', encoding='utf-8') as json_file:
    file_contents = json_file.read()

# load the json to a string
json_data = json.loads(file_contents)

count = 0
# extract an element in the response
for x in json_data:
    separator = "."
    r = x['Price'].split(separator, 1)[0]
    result = re.sub(r'[^0-9]', '', r)
    if int(result) < 999:
        print("Title: " + x['Title'])
        print("Price: " + x["Price"])
        print("Link: " + x["Link"])
        print("Image: " + x["Image Source"])
    else:
        count += 1
print(count)
