import json
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
f = open("result.txt", "a", encoding='utf-8')
res = []
for infoBox in infoBoxs:
    title = infoBox.find("h3", {"class": "s-item__title"}).text
    price = infoBox.find("span", {"class": "s-item__price"}).text
    href = infoBox.find("a", {"class": "s-item__link"}).get("href")
    img = infoBox.find("img", {"class": "s-item__image-img"})
    test = infoBox.find(img, {"img": "data-src"})
    print(img)
    print(test)
    if "to" in price:
        price = price.split('to', 1)[0]
    count += 1
    title = title.replace("✅", " ").replace("❖", "").replace("✤", "")
    result = str(
        count) + "." + "\n" + "Title: " + title + "\n" + "Price: " + price + "\n" + "Link: " + href + "\n" + "Image Source: " + \
             img[
                 "src"] + "\n" + liner
    json_result = "Title: " + title, "Price: " + price, "Link: " + href

    f.write(result + "\n")
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
