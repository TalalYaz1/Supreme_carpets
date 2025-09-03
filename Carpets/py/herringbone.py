import requests
from bs4 import BeautifulSoup
import json

url = "https://www.renovatedirect.co.uk/collections/herringbone-laminate-flooring"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

data = []

# Loop through each product-card
for product in soup.select("product-card"):
    # Extract name
    name_tag = product.select_one(".product-card__title a")
    name = name_tag.get_text(strip=True) if name_tag else None

    # Extract images (hover + main)
    images = product.select(".product-card__figure img")
    hover_image, main_image = None, None
    if len(images) >= 2:
        hover_image = "https:" + images[0].get("src")
        main_image = "https:" + images[1].get("src")
    elif len(images) == 1:
        main_image = "https:" + images[0].get("src")

    # Save to JSON-like dict
    if name:
        data.append({
            "name": name,
            "image": main_image,
            "hover-image": hover_image
        })

# Export to JSON file
with open("herringbone_flooring.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(json.dumps(data, indent=2, ensure_ascii=False))