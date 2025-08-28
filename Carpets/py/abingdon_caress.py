import requests
from bs4 import BeautifulSoup
import json

URL = "https://www.abingdonflooring.co.uk/range/caress/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

carpet_divs = soup.find_all("div", class_="jet-listing-grid__item")
print(f"Found {len(carpet_divs)} products")

carpets = []

for div in carpet_divs:
    try:
        # Product name & URL
        h2_tag = div.find("h2", class_="elementor-heading-title")
        name = h2_tag.get_text(strip=True) if h2_tag else "Unknown"
        url_tag = h2_tag.find("a") if h2_tag else None
        url = url_tag["href"] if url_tag else ""

        # Product image
        img_tag = div.find("img")
        img_url = img_tag["src"] if img_tag else ""

        carpets.append({
            "name": name,
            "image": img_url,
            "url": url
        })

    except Exception as e:
        print("Error parsing product:", e)

# Save to JSON
with open("caress_carpets.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"Scraped {len(carpets)} products")