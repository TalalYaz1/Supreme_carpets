import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.franklyflooring.co.uk/product-category/lvt/victoria/universal-55-plank/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

products = []

# Each product is inside a <div class="product-small box ">
product_divs = soup.find_all("div", class_="product-small")

for div in product_divs:
    try:
        # Product name (inside <a> tag)
        name_tag = div.find("a", class_="woocommerce-LoopProduct-link")
        full_name = name_tag.get_text(strip=True) if name_tag else "Unknown"

        # Extract only the part after the dash (– or -)
        if "–" in full_name:  # en dash
            name = full_name.split("–", 1)[1].strip()
        elif "-" in full_name:  # normal dash fallback
            name = full_name.split("-", 1)[1].strip()
        else:
            name = full_name  # no dash, keep whole name

        # Product image
        img_tag = div.find("img")
        img_url = img_tag["src"] if img_tag else ""

        products.append({
            "full_name": full_name,
            "name": name,
            "image": img_url
        })
    except Exception as e:
        print("Error parsing product:", e)

# Save to JSON
with open("victoria_universal55.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Scraped {len(products)} products")