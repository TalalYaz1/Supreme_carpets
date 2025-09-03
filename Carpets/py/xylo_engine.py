from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

# Setup Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")  # comment this out if you want to see the browser
driver = webdriver.Chrome(options=chrome_options)

# Target page
url = "https://xyloflooring.com/product-category/engineered-flooring/richmond_plank/"
driver.get(url)

# Wait for JavaScript to load content
time.sleep(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

# Each product is inside <li class="product ...">
product_cards = soup.find_all("li", class_="product")
print(f"🧩 Found {len(product_cards)} product cards")

products = []

for card in product_cards:
    try:
        # Product URL
        a_tag = card.find("a", class_="woocommerce-LoopProduct-link")
        product_url = a_tag['href'] if a_tag and a_tag.has_attr('href') else ""

        # Product name
        name_tag = card.find("h2", class_="woocommerce-loop-product__title")
        name = name_tag.get_text(strip=True) if name_tag else ""

        # Product image
        img_tag = card.find("img")
        image_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else ""

        product_data = {
            "name": name,
            "url": product_url,
            "image_url": image_url
        }

        products.append(product_data)

    except Exception as e:
        print(f"❌ Error parsing product card: {e}")

# Save to JSON file
with open("xylo_engine.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Total products scraped: {len(products)} and saved to xylo_products.json")