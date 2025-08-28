import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.hughmackay.co.uk/product-category/axminster-carpets/natures-own/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = []

# Each product is in an <li> with class "product"
product_items = soup.find_all("li", class_="product")

for item in product_items:
    try:
        # Name
        name_tag = item.find("h2", class_="woocommerce-loop-product__title")
        name = name_tag.get_text(strip=True) if name_tag else "Unknown"

        # Image
        img_tag = item.find("img")
        img_url = img_tag["src"] if img_tag else ""

        products.append({
            "name": name,
            "image": img_url
        })
    except Exception as e:
        print("Error parsing product:", e)

# Save to JSON
with open("hughmackay_natures_own.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"Scraped {len(products)} products")