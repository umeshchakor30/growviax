import re

with open('products.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('grid.html', 'r', encoding='utf-8') as f:
    grid = f.read()

filters = '''<div class="d-flex flex-wrap justify-content-center gap-2">
                    <button class="filter-btn active" data-filter="all">All Products</button>
                    <button class="filter-btn" data-filter="spices">Spices</button>
                    <button class="filter-btn" data-filter="dehydrated">Dehydrated Powder</button>
                    <button class="filter-btn" data-filter="dairy">Dairy Products</button>
                    <button class="filter-btn" data-filter="fresh">Fresh Goods</button>
                </div>'''

content = re.sub(r'<div class="d-flex flex-wrap justify-content-center gap-2">.*?</div>', filters, content, flags=re.DOTALL)
content = re.sub(r'<div class="row g-4" id="product-grid">.*?</div>\s*</div>\s*</section>', grid + '\n        </div>\n    </section>', content, flags=re.DOTALL)

with open('products.html', 'w', encoding='utf-8') as f:
    f.write(content)
