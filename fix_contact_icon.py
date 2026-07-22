import os
import re

files = ['contact.html', 'privacy-policy.html', 'terms-of-service.html']

for file in files:
    filepath = os.path.join(r"d:\mearn\Growviax", file)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace the CSS definition
    content = content.replace('.contact-icon {', '.page-contact-icon {')
    
    # 2. Replace the HTML class usage, but NOT in the footer!
    footer_idx = content.find('<footer class="footer-custom">')
    if footer_idx != -1:
        pre_footer = content[:footer_idx]
        footer = content[footer_idx:]
        
        pre_footer = pre_footer.replace('"contact-icon"', '"page-contact-icon"')
        
        new_content = pre_footer + footer
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
    else:
        print(f"Could not find footer in {file}")
