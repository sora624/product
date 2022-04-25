products = []
with open('products.csv', 'r', encoding='utf-8') as f:
    for line in f:
        if '求Item,Price' in line:
            continue
        name, price = line.strip().split(',')
        # products.append(name, price)
        products.append([name, price])
print(products)

while True:
    name = input('Please input product name: ')
    if name == 'q':
        break
    price = input('Please input price: ')
    price = int(price)
    products.append([name, price])

# b = input('check item')
print(products)

for p in products:
    print(p[0], " Price is", p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('求Item,Price, '\n')
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n')