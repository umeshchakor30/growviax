import os
import re

# This script reads images from images/products/ and directly injects 
# the HTML product cards into index.html and products.html.
# This keeps the site 100% static with no Javascript fetching.

PRODUCTS_DIR = os.path.join('images', 'products')

if not os.path.exists(PRODUCTS_DIR):
    os.makedirs(PRODUCTS_DIR)
    print(f"Created directory {PRODUCTS_DIR}")

def format_product_name(filename):
    name = os.path.splitext(filename)[0]
    name = name.replace('-', ' ').replace('_', ' ')
    return name.title()

products = []
valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')

for root, dirs, files in os.walk(PRODUCTS_DIR):
    for filename in files:
        if filename.lower().endswith(valid_extensions):
            filepath = os.path.join(root, filename).replace('\\', '/')
            
            # Determine category from subdirectory
            rel_path = os.path.relpath(root, PRODUCTS_DIR)
            if rel_path == '.':
                category = 'all' # Default
            else:
                category = rel_path.lower().replace('\\', '/').split('/')[0]
            
            product_name = format_product_name(filename)
            timestamp = int(os.path.getmtime(filepath))
            
            products.append({
                "name": product_name,
                "image": f"{filepath}?v={timestamp}",
                "category": category
            })

# Sort by custom category sequence, then alphabetically by name
category_order = {
    'dehydrated powder': 1,
    'spices': 2,
    'fresh goods': 3,
    'dairy products': 4
}
products.sort(key=lambda x: (category_order.get(x["category"], 99), x["name"]))

# Function to generate HTML cards
def generate_html(prod_list, limit=None):
    html = "\n"
    for i, p in enumerate(prod_list):
        if limit and i >= limit:
            break
            
        display_category = 'Premium' if p['category'] == 'all' else p['category'].title()
        delay = (i % 3 + 1) * 100
        
        html += f"""                <!-- Product {i+1} -->
                <div class="col-lg-4 col-md-6 product-item {p['category']}" data-aos="fade-up" data-aos-delay="{delay}">
                    <div class="product-card">
                        <div class="product-img-wrapper">
                            <img src="{p['image']}" alt="{p['name']}">
                        </div>
                        <div class="product-content">
                            <h3 class="product-title"><a href="#" class="quick-view-trigger" data-bs-toggle="offcanvas" data-bs-target="#productQuickView">{p['name']}</a></h3>
                            <p class="small mb-3">Premium quality export grade.</p>
                            <a href="#" class="text-primary fw-semibold d-flex align-items-center gap-1 quick-view-trigger" data-bs-toggle="offcanvas" data-bs-target="#productQuickView">View Details <i class="ph ph-arrow-right"></i></a>
                        </div>
                    </div>
                </div>\n"""
    return html

# 1. Update index.html (Show all products)
featured_html = generate_html(products)
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = re.sub(
    r'(<!-- DYNAMIC_PRODUCTS_START -->).*?(<!-- DYNAMIC_PRODUCTS_END -->)',
    r'\1' + featured_html + r'                \2',
    index_content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

# 2. Update products.html (All products)
all_html = generate_html(products)
with open('products.html', 'r', encoding='utf-8') as f:
    prod_content = f.read()

prod_content = re.sub(
    r'(<!-- DYNAMIC_PRODUCTS_START -->).*?(<!-- DYNAMIC_PRODUCTS_END -->)',
    r'\1' + all_html + r'                \2',
    prod_content,
    flags=re.DOTALL
)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(prod_content)

print(f"Successfully injected {len(products)} products into HTML files statically.")
