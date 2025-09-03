import requests
from bs4 import BeautifulSoup
import json

url = "https://www.therdex.com/products/?filter%5B223%5D%5B12%5D=planks&filter%5B225%5D%5B9%5D=therdex-dryback&order=standaard&page=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

products = []

# Find all product cards
for card in soup.select(".product-card-sm"):
    title_elem = card.select_one(".card-title a")
    main_image_elem = card.select_one(".card-img-top img")
    hover_image_elem = card.select_one(".hover-image img")

    title = title_elem.text.strip() if title_elem else ""
    main_image = main_image_elem.get("data-srcset") or main_image_elem.get("src") if main_image_elem else ""
    hover_image = hover_image_elem.get("data-srcset") or hover_image_elem.get("src") if hover_image_elem else ""

    products.append({
        "title": title,
        "main_image": main_image,
        "hover_image": hover_image
    })

# Save to JSON
with open("therdex_products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=4, ensure_ascii=False)

print(f"Scraped {len(products)} products and saved to therdex_products.json")