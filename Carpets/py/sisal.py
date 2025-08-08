import requests
from bs4 import BeautifulSoup
import json
import os

BASE_URL = "https://www.sisalandseagrass.co.uk"
TARGET_URL = f"{BASE_URL}/product-category/ranges/sisal-carpet/page/2/"

# Create output folder if not exists
os.makedirs("sisal", exist_ok=True)

response = requests.get(TARGET_URL)
print("HTTP status code:", response.status_code)

if response.status_code != 200:
    print("❌ Failed to fetch the page.")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Find all carpet items
product_list = soup.find("ul", class_="products")
if not product_list:
    print("⚠️ Warning: No products found on the page.")
    exit()

product_items = product_list.find_all("li", class_="product")
print(f"🧵 Found {len(product_items)} carpet tiles")

carpets = []

for item in product_items:
    try:
        # Product name
        name_tag = item.find("h3", class_="product-title")
        name = name_tag.get_text(strip=True) if name_tag else "Unknown"

        # Product URL
        link_tag = item.find("a", class_="product-images")
        url = link_tag['href'] if link_tag and 'href' in link_tag.attrs else ""

        # Product image
        img_tag = item.find("img")
        image_url = img_tag['src'] if img_tag and 'src' in img_tag.attrs else ""
        if image_url.startswith("/"):
            image_url = BASE_URL + image_url

        # Price
        price_tag = item.find("span", class_="woocommerce-Price-amount")
        price = price_tag.get_text(strip=True) if price_tag else "Price not found"

        carpets.append({
            "name": name,
            "url": url,
            "image": image_url,
            "price": price
        })

    except Exception as e:
        print("❌ Error parsing a carpet:", e)

# Save to JSON
output_path = os.path.join("sisal", "page2.json")
with open(output_path, "w") as f:
    json.dump(carpets, f, indent=2)

print(f"✅ Total carpets scraped: {len(carpets)} and saved to {output_path}")