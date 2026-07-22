import re

# 1. Clean index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = re.sub(
    r'(<div class="section-title text-start mb-0"[^>]*>.*?Featured Products.*?</div>\s*<a[^>]*>.*?</a>\s*</div>\s*)<div class="row g-4">.*?<!-- Product 3 -->.*?</div>\s*</div>\s*(<div class="text-center mt-4 d-md-none">)',
    r'\1<div id="featured-products-grid" class="row g-4"></div>\n            \2',
    index_content,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)
print("Cleaned index.html featured products grid.")

# 2. Clean products.html
with open('products.html', 'r', encoding='utf-8') as f:
    prod_content = f.read()

prod_content = re.sub(
    r'(<div class="row g-4" id="product-grid">).*?(</div>\s*</div>\s*</section>)',
    r'\1\n                <!-- Products will be loaded here dynamically -->\n            \2',
    prod_content,
    flags=re.DOTALL
)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(prod_content)
print("Cleaned products.html grid.")

# 3. Add js/products.js to both
for file in ['index.html', 'products.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'js/products.js' not in content:
        content = content.replace('</body>', '    <script src="js/products.js"></script>\n</body>')
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added products.js script tag to {file}")
