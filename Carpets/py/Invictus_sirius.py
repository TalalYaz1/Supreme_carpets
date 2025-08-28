import requests
from bs4 import BeautifulSoup
import json

URL = "https://invictus.co.uk/carpet/the-collection/sirius"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = []

# find all product cards
for card in soup.find_all("div", class_="product-card"):
    try:
        # Get title
        title_tag = card.find("h5", class_="product-card__title")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown"

        # Get color swatch image
        color_img_tag = card.find("img", class_="product-color-media")
        color_img = f"https://invictus.co.uk{color_img_tag['src']}" if color_img_tag else ""

        products.append({
            "title": title,
            "color_image": color_img
        })

    except Exception as e:
        print("Error parsing product:", e)

# Save as JSON
with open("sirius_products.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"Scraped {len(products)} products")