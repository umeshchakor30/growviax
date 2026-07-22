import random

products = [
    # Spices
    ("Turmeric (Haldi)", "spices", "Spices"),
    ("Cumin (Jeera)", "spices", "Spices"),
    ("Coriander (Dhaniya)", "spices", "Spices"),
    ("Black Pepper (Kali Mirch)", "spices", "Spices"),
    ("Cardamom (Elaichi)", "spices", "Spices"),
    ("Cinnamon (Dalchini)", "spices", "Spices"),
    ("Cloves (Laung)", "spices", "Spices"),
    ("Mustard Seeds", "spices", "Spices"),
    ("Red chilli", "spices", "Spices"),
    ("Sauf", "spices", "Spices"),
    
    # Dehydrated powder
    ("Red Onion powder", "dehydrated", "Dehydrated"),
    ("Onion Flakes", "dehydrated", "Dehydrated"),
    ("Fried onion", "dehydrated", "Dehydrated"),
    ("Onion Powder", "dehydrated", "Dehydrated"),
    ("Fresh Ginger", "dehydrated", "Dehydrated"),
    ("Ginger Powder", "dehydrated", "Dehydrated"),
    ("Fresh Garlic", "dehydrated", "Dehydrated"),
    ("Garlic Powder", "dehydrated", "Dehydrated"),
    ("Turmeric Powder", "dehydrated", "Dehydrated"),
    ("Spinach Powder", "dehydrated", "Dehydrated"),
    ("Tomato Powder", "dehydrated", "Dehydrated"),
    ("Red Chilli Powder", "dehydrated", "Dehydrated"),
    
    # Dairy
    ("Cow Ghee / A2 Cow Ghee", "dairy", "Dairy"),
    
    # Fresh
    ("Onion (Fresh)", "fresh", "Fresh Goods")
]

html = '<div class="row g-4" id="product-grid">\n'
for name, filter_class, badge in products:
    img_num = random.randint(1, 10)
    html += f'''                <div class="col-lg-4 col-md-6 product-item {filter_class}">
                    <div class="product-card">
                        <span class="product-category-badge">{badge}</span>
                        <div class="product-img-wrapper">
                            <img src="images/sample{img_num}.jpeg" alt="{name}">
                        </div>
                        <div class="product-content">
                            <h3 class="product-title"><a href="product-detail.html">{name}</a></h3>
                            <a href="product-detail.html" class="text-primary fw-semibold d-flex align-items-center gap-1">View Details <i class="ph ph-arrow-right"></i></a>
                        </div>
                    </div>
                </div>\n'''

html += '            </div>'

with open('grid.html', 'w', encoding='utf-8') as f:
    f.write(html)
