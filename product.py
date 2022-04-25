products = []
while True:
    name = input ('Please input product name: ')
    if name == 'q':
        break
    price = input('Please input price: ')
    # item = name + price
    item = []
    item.append(name)
    item.append(price)
    products.append(item)

# b = input('check item')
print(products)

for p in products:
    print(p[0], " Price is", p[1])

with open('products.csv', 'w') as f:
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')