import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.cormarcarpets.co.uk"
TARGET_URL = "https://www.cormarcarpets.co.uk/carpet-ranges/soft-deep-pile/riva/"

response = requests.get(TARGET_URL)
print("HTTP status code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

carpet_divs = soup.find_all("div", class_="col-xs-12 col-sm-4 col-md-3")
print(f"🧵 Found {len(carpet_divs)} carpet tiles")

carpets = []

for div in carpet_divs:
    try:
        title_tag = div.find("span", class_="title")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown"

        image_wrap = div.find("span", class_="image-wrap")
        picture = image_wrap.find("picture") if image_wrap else None

        image_url = ""

        if picture:
            source = picture.find("source")
            if source:
                # Try data-src
                if "data-src" in source.attrs:
                    image_url = source["data-src"]
                # Try srcset
                elif "srcset" in source.attrs:
                    image_url = source["srcset"]
        
        # Fallback to <img src> if <source> failed
        if not image_url and picture:
            img = picture.find("img")
            if img and "src" in img.attrs:
                image_url = img["src"]

        # Prepend base URL if it's a relative link
        if image_url.startswith("/"):
            image_url = BASE_URL + image_url

        carpets.append({
            "name": title,
            "image": image_url
        })

    except Exception as e:
        print("❌ Error parsing a carpet:", e)

# Save to JSON
with open("riva_carpets.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"✅ Total carpets scraped: {len(carpets)}")