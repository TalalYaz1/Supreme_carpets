import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.cormarcarpets.co.uk"
TARGET_URL = "https://www.cormarcarpets.co.uk/carpet-ranges/soft-deep-pile/riva/"

response = requests.get(TARGET_URL)
print("HTTP status code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# Step 1: Scrape the shared description
desc_text = ""
desc_section = soup.find("section", class_="list-images-29")
if desc_section:
    h2 = desc_section.find("h2", class_="list-images-29__title")
    if h2:
        desc_text = h2.get_text(separator=" ", strip=True)

if not desc_text:
    print("⚠️ Warning: Description not found.")
else:
    print(f"📄 Scraped shared info:\n{desc_text}\n")

# Step 2: Scrape each carpet tile
carpet_divs = soup.find_all("div", class_="col-xs-12 col-sm-4 col-md-3")
print(f"🧵 Found {len(carpet_divs)} carpet tiles")

carpets = []

for div in carpet_divs:
    try:
        title_tag = div.find("span", class_="title")
        title = title_tag.get_text(strip=True) if title_tag else "Unknown"

        main_image_url = ""
        hover_image_url = ""

        # Find main image
        main_picture = div.find("picture", class_="teaser-118--picture-main")
        if main_picture:
            source_tag = main_picture.find("source")
            if source_tag and "data-src" in source_tag.attrs:
                main_image_url = BASE_URL + source_tag["data-src"]

        # Find hover image
        hover_picture = div.find("picture", class_="teaser-118--picture-overlay")
        if hover_picture:
            source_tag = hover_picture.find("source")
            if source_tag and "data-src" in source_tag.attrs:
                hover_image_url = BASE_URL + source_tag["data-src"]

        if not main_image_url:
            print(f"❌ Skipping '{title}' — no main image found.")
            continue

        carpet_data = {
            "name": title,
            "image": main_image_url,
            "info": desc_text
        }

        if hover_image_url:
            carpet_data["hover_image"] = hover_image_url

        carpets.append(carpet_data)

    except Exception as e:
        print("❌ Error parsing a carpet:", e)

# Step 3: Save to JSON
with open("riva_carpets.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"✅ Total carpets scraped: {len(carpets)} and saved to riva_carpets.json")