from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

# Setup Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # Comment this out if you want to see the browser

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amtico.com/products/")

# Wait for JavaScript to load content (adjust time as needed)
time.sleep(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

product_cards = soup.find_all("div", class_="af-productcard")
print(f"🧩 Found {len(product_cards)} product cards")

products = []

for card in product_cards:
    try:
        # Code (e.g. AR0W8750)
        code_tag = card.find("span", class_="uppercase")
        code = code_tag.get_text(strip=True) if code_tag else ""

        # Collection label (e.g. Amtico Signature)
        collection_tag = card.find("span", class_="af-collectionlabel")
        collection = collection_tag.get_text(strip=True) if collection_tag else ""

        # Name (e.g. Friston Oak)
        name_tag = card.find("h3")
        name = ""
        product_url = ""
        if name_tag:
            a_tag = name_tag.find("a")
            if a_tag:
                name = a_tag.get_text(strip=True)
                product_url = "https://www.amtico.com" + a_tag.get('href', "")

        # Images
        pictures = card.find_all("picture")
        main_image_url = ""
        hover_image_url = ""

        if len(pictures) > 0:
            main_img = pictures[0].find("img")
            if main_img and main_img.has_attr('src'):
                main_image_url = main_img['src']

        if len(pictures) > 1:
            hover_img = pictures[1].find("img")
            if hover_img and hover_img.has_attr('src'):
                hover_image_url = hover_img['src']

        product_data = {
            "af-productcard": {
                "code": code,
                "collection": collection,
                "name": name,
                "product_url": product_url,
                "main_image_url": main_image_url,
                "hover_image_url": hover_image_url
            }
        }

        products.append(product_data)

    except Exception as e:
        print(f"❌ Error parsing product card: {e}")

# Save to JSON file
with open("amtico_products.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Total products scraped: {len(products)} and saved to amtico_products.json")