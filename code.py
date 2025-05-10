import requests
from bs4 import BeautifulSoup
import csv

# OLX search URL
url = "https://www.olx.in/items/q-car-cover"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Result list
results = []

# Find listings
listings = soup.find_all('li', class_='css-19ucd76')  # OLX listing class

for item in listings:
    title_tag = item.find('span', class_='css-2tgytl')
    price_tag = item.find('span', class_='css-1s1zksu')
    link_tag = item.find('a', href=True)

    if title_tag and link_tag:
        title = title_tag.text.strip()
        price = price_tag.text.strip() if price_tag else "N/A"
        link = "https://www.olx.in" + link_tag['href']
        results.append([title, price, link])

# Write to CSV
with open('car_covers.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Price', 'Link'])
    writer.writerows(results)

print("Scraped", len(results), "car covers. Saved to car_covers.csv")
