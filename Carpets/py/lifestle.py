import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

# Target page
url = "https://www.lifestyle-floors.co.uk/laminate-ranges/chelsea"
base_url = "https://www.lifestyle-floors.co.uk/"

# Fetch page
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

data = []

# Each product is in this wrapper
products = soup.select("div.swatchpadding")

for product in products:
    # Image inside <input type="image">
    img_tag = product.find("input", {"class": "ProductImage"})
    img_url = None
    if img_tag and img_tag.get("src"):
        img_url = urljoin(base_url, img_tag["src"])  # make absolute
    
    # Title inside <a class="SwatchDesignText">
    title_tag = product.find("a", {"class": "SwatchDesignText"})
    title = title_tag.get_text(strip=True) if title_tag else None

    if title and img_url:
        data.append({
            "title": title,
            "image": img_url
        })

# Save to JSON
with open("chelsea.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Scraped {len(data)} products")