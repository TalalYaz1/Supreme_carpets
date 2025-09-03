import requests
from bs4 import BeautifulSoup
import json

URL = "https://carpetsandmore.co.uk/all-flooring/wood/engineered-wood/victoria-design-floors-victorious-14-3-plank"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

carpet_divs = soup.find_all("div", class_="sku-thumbnail")
print(f"Found {len(carpet_divs)} products")

carpets = []

for div in carpet_divs:
    try:
        # Product name
        name_tag = div.find("div", class_="card-body").find("span")
        name = name_tag.get_text(strip=True) if name_tag else "Unknown"

        # Product image
        img_tag = div.find("img")
        img_url = f"https://carpetsandmore.co.uk{img_tag['src']}" if img_tag else ""

        # Product price
        price_tag = div.find("div", class_="card-footer").find("strong")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"

        carpets.append({
            "name": name,
            "image": img_url,
            "price": price
        })

    except Exception as e:
        print("Error parsing product:", e)

# Save to JSON
with open("associated_weavers.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"Scraped {len(carpets)} products")