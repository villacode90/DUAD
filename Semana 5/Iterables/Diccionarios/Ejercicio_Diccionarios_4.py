sales = [
    {
        'date': '27/02/23',
        'customer_email': 'joe@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Iron',
                'upc': 'ITEM-324',
                'unit_price': 32.45,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 12.54,
            },
        ],
    },
    {
        'date': '27/02/23',
        'customer_email': 'david@gmail.com',
        'items': [
            {
                'name': 'Lava Lamp',
                'upc': 'ITEM-453',
                'unit_price': 65.76,
            },
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 5.42,
            },
        ],
    },
    {
        'date': '26/02/23',
        'customer_email': 'amanda@gmail.com',
        'items': [
            {
                'name': 'Key Holder',
                'upc': 'ITEM-23',
                'unit_price': 3.42,
            },
            {
                'name': 'Basketball',
                'upc': 'ITEM-432',
                'unit_price': 17.54,
            },
        ],
    },
]

sales_by_upc = {}
upc_sales = {}

for i in sales:

    for item in i['items']:
        upc = item['upc']
        unit_price = item['unit_price']

        if upc in upc_sales:
            upc_sales[upc] += unit_price
        else:
            upc_sales[upc] = unit_price
print(f'result = {upc_sales}')
