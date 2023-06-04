import json
import sys

# load the data into an element
with open('results.json') as user_file:
    file_contents = user_file.read()

# dumps the json object into an element
json_str = json.dumps(file_contents)

# load the json to a string
resp = json.loads(json_str)

# print the resp
print(resp)

# extract an element in the response

