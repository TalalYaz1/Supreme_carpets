import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.onlinecarpets.co.uk/products/megatex-vinyl-flooring"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# Grab all product images
img_tags = soup.find_all("img", alt=True, src=True)

products = []

for img in img_tags:
    try:
        name = img["alt"].strip()
        image_url = img["src"]

        # Ensure full URL (add https: if it's missing)
        if image_url.startswith("//"):
            image_url = "https:" + image_url

        products.append({
            "name": name,
            "image": image_url
        })
    except Exception as e:
        print("Error parsing product:", e)

# Save to JSON
with open("megatex_vinyl.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Scraped {len(products)} products")