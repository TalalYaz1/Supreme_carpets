import requests
from bs4 import BeautifulSoup
import json

URL = "https://elementscarpet.com/collection/Symphony-Sheen-Velvet/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

carpets = []

# Find all thumbnail divs
thumbnails = soup.find_all("div", class_="thumbnail")

for div in thumbnails:
    try:
        # Image and name
        img_tag = div.find("img", class_="thumbnail-img")
        if img_tag:
            img_url = img_tag["src"]
            name = img_tag.get("alt", "").strip()

            # Sometimes name also appears in thumbnail-title div
            title_div = div.find("div", class_="thumbnail-title")
            if title_div:
                name = title_div.get_text(strip=True)

            # Fix relative image paths
            if img_url.startswith("/"):
                img_url = f"https://elementscarpet.com{img_url}"

            carpets.append({
                "name": name,
                "image": img_url
            })
    except Exception as e:
        print("Error parsing:", e)

# Save to JSON
with open("symphony_sheen_velvet.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"Scraped {len(carpets)} products")