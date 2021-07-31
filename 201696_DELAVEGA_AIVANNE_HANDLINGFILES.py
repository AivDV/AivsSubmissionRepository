products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
##Problem1
def get_product(code):
    return products[code]
##Problem 2
def get_property(code, property):
    return products[code][property]
##Problem3
def main(): 
    total = 0
    text = ''
    error_count = 0
    dicts = {}
    while error_count != 1:
        try: 
            quant = 0
            text,quant = input("What is your order, select from the order codes given, 'americano', 'brewedcoffee', 'cappuccino', 'dalgona', 'espresso', 'frappuccino'.").split(',')
            quant = int(quant)
            if text == '/':
                break
            else:
                pass
            if text not in products:
                print('Sorry that was an invalid order')
                break
            else:
                pass
            if text in dicts:
                dicts[text]['price'] = (dicts[text]['price'] + quant*float(products[text]['price']))
                dicts[text]['quantity'] = dicts[text]['quantity'] + quant
            elif text not in dicts:
                dicts[text] = {'name': products[text]['name'], 'price': (quant*float(products[text]['price'])), 'quantity': quant}
        except: 
            error_count +=1 
    with open('receipt.txt', 'w') as receipt:
            receipt.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
        ''')
            sortedDict = dict( sorted(dicts.items(), key=lambda x: x[0].lower()) )
            for key in sortedDict:
                code = sortedDict[key]['name']
                price = sortedDict[key]['price']
                quantity = sortedDict[key]['quantity']
                total += price
                receipt.write(f'\n{key}\t\t\t{code}\t\t\t{quantity}\t\t\t{price}')
            receipt.write(f'''\nTotal:\t\t\t\t\t\t\t\t\t\t{total}
        ==
        ''')
main()