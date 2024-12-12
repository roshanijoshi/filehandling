import csv
import random

stocks = [
    {"Name": "NIMB", "Price": random.randint(100, 10000)},
    {"Name": "NABIL", "Price": random.randint(100, 10000)},
    {"Name": "HBL", "Price": random.randint(100, 10000)},
    {"Name": "NTC", "Price": random.randint(100, 10000)},
    {"Name": "SCB", "Price": random.randint(100, 10000)},
    {"Name": "EBL", "Price": random.randint(100, 10000)},
    {"Name": "ADBL", "Price": random.randint(100, 10000)},
    {"Name": "CIT", "Price": random.randint(100, 10000)},
    {"Name": "NICA", "Price": random.randint(100, 10000)},
    {"Name": "NLIC", "Price": random.randint(100, 10000)},
]

with open('stocks.csv', 'w', newline='') as file:  
    fieldnames = ["Name", "Price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(stocks)  

with open('stocks.csv','r') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

import pandas as pd
df=pd.read_csv('stocks.csv')
print(df)
threshold = 5000
df['If we can buy this stock'] = lambda price: 'You can buy this stock' if price <= threshold else 'Too expensive'
print(df.describe())
df.to_csv('output.csv')






