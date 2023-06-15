def getResultsF(result, priceCheck, x, f):
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
        title = ("Title: " + x['Title'])
        price = ("Price: " + x["Price"])
        link = ("Link: " + x["Link"])
        image = ("Image: " + x["Image Source"])
        results = title, price, link, image
        f.write("--==IF FALSE==--")
        f.write(str(results))
        f.write("\n")
