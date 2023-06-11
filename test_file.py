
import json
import re

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
    if int(result) < priceCheck:
        title = ("Title: " + x['Title'])
        price = ("Price: " + x["Price"])
        link = ("Link: " + x["Link"])
        image = ("Image: " + x["Image Source"])
        results = title, price, link, image
        f.write("--==IF TRUE==--")
        f.write(str(results))
        f.write("\n")
    else:
        count += 1
        title = ("Title: " + x['Title'])
        price = ("Price: " + x["Price"])
        link = ("Link: " + x["Link"])
        image = ("Image: " + x["Image Source"])
        results = title, price, link, image
        f.write("--==IF FALSE==--")
        f.write(str(results))
        f.write("\n")

print("Number of items > {0} are -{1}-".format(priceCheck, count))

f.close()
