import re

def update_images(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the image src for the specific products.
    # The structure is:
    # <img src="images/sampleX.jpeg" alt="ProductName">
    # We can just search for alt="Garlic Powder" and replace the src before it.
    
    replacements = {
        'Garlic Powder': 'images/garlic_powder.jpeg',
        'Ginger Powder': 'images/ginger_powder.jpeg',
        'Onion Powder': 'images/onion_powder.jpeg',
        'Red Onion Powder': 'images/onion_powder.jpeg', # For index.html which uses Red Onion Powder
        'Red Onion powder': 'images/onion_powder.jpeg'  # For products.html
    }
    
    for alt_text, new_img in replacements.items():
        pattern = r'<img src="[^"]+" alt="' + re.escape(alt_text) + r'">'
        replacement = f'<img src="{new_img}" alt="{alt_text}">'
        content = re.sub(pattern, replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_images('products.html')
update_images('index.html')
