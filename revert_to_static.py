import os
import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace('<div id="featured-products-grid" class="row g-4"></div>', 
'''<div class="row g-4" id="featured-products-grid">
                <!-- DYNAMIC_PRODUCTS_START -->
                <!-- DYNAMIC_PRODUCTS_END -->
            </div>''')
index_content = index_content.replace('    <script src="js/products.js"></script>\n', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)


# 2. Update products.html
with open('products.html', 'r', encoding='utf-8') as f:
    prod_content = f.read()

prod_content = prod_content.replace(
'''<div class="row g-4" id="product-grid">
                <!-- Products will be loaded here dynamically -->
            </div>''',
'''<div class="row g-4" id="product-grid">
                <!-- DYNAMIC_PRODUCTS_START -->
                <!-- DYNAMIC_PRODUCTS_END -->
            </div>''')
prod_content = prod_content.replace('    <script src="js/products.js"></script>\n', '')

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(prod_content)

# 3. Clean up JS/JSON
if os.path.exists('js/products.js'):
    os.remove('js/products.js')
if os.path.exists('products.json'):
    os.remove('products.json')

print("Reverted HTML and removed JS approach.")
