import json
import re
from bs4 import BeautifulSoup
import requests
import os


def saveToFile():
    if os.path.exists("result.txt"):
        os.remove("result.txt")
    else:
        print("The file does not exist")


url = "https://il.ebay.com/b/Cell-Phones-Smartphones/9355/bn_320094?LH_ItemCondition=1000&Brand=Samsung%7CApple%7CXiaomi%7CGoogle%7COnePlus&rt=nc&_udlo=980&_udhi=1%2C800&mag=1"
liner = "---------------------------------------------------------------------------"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, 'html.parser')
infoBoxs = soup.find_all("li", {"class": "s-item s-item--large"})
count = 0
# f = open("result.txt", "a", encoding='utf-8')
res = []
for infoBox in infoBoxs:
    title = infoBox.find("h3", {"class": "s-item__title"}).text
    price = infoBox.find("span", {"class": "s-item__price"}).text
    href = infoBox.find("a", {"class": "s-item__link"}).get("href")
    img = infoBox.find("img", {"class": "s-item__image-img"})
    img = str(img).replace("<", "").replace(">", "")
    if "data-src=" in img:
        s2 = "data-src="
        s3 = img[img.index(s2) + len(s2):]
        s3 = img.split('data-src=', 1)
        s3 = s3[1].split(' src=', 1)
        res = s3[0]
    else:
        s2 = "src="
        s3 = img[img.index(s2) + len(s2):]
        s3 = s3[:-1]
        res = s3
    if "to" in price:
        price = price.split('to', 1)[0]
    count += 1
    title = title.replace("✅", " ").replace("❖", "").replace("✤", "")
    '''
    result = str(
        count) + "." + "\n" + "Title: " + title + "\n" + "Price: " + price + "\n" + "Link: " + href + "\n" + "Image Source: " + \
             str(res) + "\n" + liner
    '''
    json_result = "Title: " + title, "Price: " + price, "Link: " + href, "Image Source: " + str(res)
    print(str(res))
    # f.write(result + "\n")
    res.append(json_result)

with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=8, ensure_ascii=False)
print("###---Created Json File---###")

'''
saveToFile()
result = "The amount of phones found is : " + str(count)
print(result)
f.write(result)
f.close()
'''
