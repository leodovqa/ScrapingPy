s1 = '<img alt="Samsung Galaxy A73 5G 128GB+8GB RAM Dual Sim Unlocked New-Multi color" class="s-item__image-img" data-src="https://i.ebayimg.com/thumbs/images/g/r6sAAOSwwS9kHfkF/s-l300.jpg" src="https://ir.ebaystatic.com/cr/v/c1/s_1x2.gif"/>'
s2 = "data-src="
x2 = "src="
s3 = s1[s1.index(s2) + len(s2):]
s4 = s3[s3.index(x2) + len(x2):]
s3 = s3.split(' src=', 1)
print(s3[0])