mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Russia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'UK'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchange_rate': 107.25
}

for mobile in mobile_data['data']:
    name = mobile['name']
    price_usd = float(mobile['price'].split()[0])  # Extract the USD price as a float
    made_in = mobile['made']
    price_bdt = price_usd * mobile_data['exchange_rate']

    print(f"{name} is made in {made_in}. The price is {price_usd} USD which is almost equal to {price_bdt:.2f} BDT")
