import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.cormarcarpets.co.uk"
TARGET_URL = "https://www.cormarcarpets.co.uk/carpet-ranges/wool-twist/hampstead/"

response = requests.get(TARGET_URL)
print("HTTP status code:", response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

# Optional: shared description
desc_text = ""
desc_section = soup.find("section", class_="list-images-29")
if desc_section:
    h2 = desc_section.find("h2", class_="list-images-29__title")
    if h2:
        desc_text = h2.get_text(separator=" ", strip=True)

# Scrape carpet tiles
carpet_divs = soup.find_all("div", class_="col-xs-12 col-sm-4 col-md-3")
print(f"🧵 Found {len(carpet_divs)} carpet tiles")

carpets = []

for div in carpet_divs:
    try:
        link_tag = div.find("a", class_="teaserResultLink")
        url = BASE_URL + link_tag['href'] if link_tag and link_tag.has_attr('href') else ""

        title_tag = div.find("span", class_="title")
        name = title_tag.get_text(strip=True) if title_tag else "Unknown"

        # Main image
        main_img_url = ""
        main_picture = div.find("picture", class_="teaser-118--picture-main")
        if main_picture:
            source_tag = main_picture.find("source")
            if source_tag and source_tag.has_attr("data-src"):
                main_img_url = BASE_URL + source_tag["data-src"]

        # Hover image
        hover_img_url = ""
        hover_picture = div.find("picture", class_="teaser-118--picture-overlay")
        if hover_picture:
            source_tag = hover_picture.find("source")
            if source_tag and source_tag.has_attr("data-src"):
                hover_img_url = BASE_URL + source_tag["data-src"]

        carpet_data = {
            "name": name,
            "image": main_img_url,
            "hover_image": hover_img_url,
            "info": desc_text,
            "url": url
        }

        carpets.append(carpet_data)

    except Exception as e:
        print("❌ Error parsing a carpet:", e)

# Save to JSON
with open("hamp_wool.json", "w") as f:
    json.dump(carpets, f, indent=2)

print(f"✅ Total carpets scraped: {len(carpets)} and saved to primo_ultra_carpets.json")