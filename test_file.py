import json
import re

from test_to_test_file import getResultsF

open('test_file_res.txt', 'w').close()

f = open("test_file_res.txt", "a", encoding='utf-8')

# load the data into an element
with open('results.json', encoding='utf-8') as json_file:
    file_contents = json_file.read()

# load the json to a string
json_data = json.loads(file_contents)

count = 0
# priceCheck = 1500
priceCheck = int(input("Enter a Price: "))
# extract an element in the response
for x in json_data:
    separator = "."
    r = x['Price'].split(separator, 1)[0]
    result = re.sub(r'[^0-9]', '', r)
    getResultsF(result, priceCheck, x, f)
    if int(result) > priceCheck:
        count += 1
print("Number of items with higher cost from {0} are -{1}-".format(priceCheck, count))

f.close()
