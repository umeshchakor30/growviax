import os
import glob
import re

# Increase logo height to 120px, and apply negative margin so the navbar doesn't get ridiculously tall.
navbar_brand_new = """<a class="navbar-brand" href="index.html" style="margin-top: -30px; margin-bottom: -30px;">
                <img src="images/logo.jpeg" alt="Growviax Global Logo" style="height: 140px; width: auto; mix-blend-mode: multiply;">
            </a>"""

html_files = glob.glob('*.html')
pattern = re.compile(r'<a class="navbar-brand.*?</a>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(navbar_brand_new, content, count=1)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated navbar brand logo size in {file}")
    else:
        print(f"Navbar brand pattern not found or already updated in {file}")
