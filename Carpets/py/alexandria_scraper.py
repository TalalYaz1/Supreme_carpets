from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import json
import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Remove this line to see browser window

# Start Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.unnaturalflooring.com/products/new-england/"
driver.get(url)

# Wait for JavaScript to load
time.sleep(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

# This targets actual product containers
product_containers = soup.select("div.product-image > a")

print(f"🧩 Found {len(product_containers)} products")

products = []

for container in product_containers:
    try:
        product = {
            "name": "",
            "code": "",
            "product_url": "",
            "main_image_url": "",
            "hover_image_url": ""
        }

        # Product URL
        href = container.get("href")
        if href:
            product["product_url"] = "https://www.unnaturalflooring.com" + href

        # Images
        img_a = container.select_one(".product-image-a img")
        img_b = container.select_one(".product-image-b img")

        if img_a and img_a.get("src"):
            product["main_image_url"] = "https://www.unnaturalflooring.com" + img_a["src"]

        if img_b and img_b.get("src"):
            product["hover_image_url"] = "https://www.unnaturalflooring.com" + img_b["src"]

        # Go into the product info block
        sibling_div = container.find_next("div", class_="col-12 col-xxl-6")
        if sibling_div:
            name_tag = sibling_div.find("h3")
            code_tag = sibling_div.find("span", class_="code")

            if name_tag:
                product["name"] = name_tag.get_text(strip=True)

            if code_tag:
                product["code"] = code_tag.get_text(strip=True)

        if product["name"]:
            products.append({"product": product})

    except Exception as e:
        print(f"❌ Error parsing product: {e}")

# Save to JSON
with open("unnatural_flooring_products.json", "w") as f:
    json.dump(products, f, indent=2)

print(f"✅ Scraped {len(products)} products and saved to unnatural_flooring_products.json")