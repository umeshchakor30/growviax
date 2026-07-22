import os
import glob
import re

navbar_brand_new = """<a class="navbar-brand d-flex align-items-center gap-2" href="index.html">
                <img src="images/logo.jpeg" alt="Growviax Global Logo" style="width: 45px; height: 45px; object-fit: cover; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                <div class="d-flex flex-column justify-content-center lh-1">
                    <span class="fw-bold" style="font-family: 'Poppins', sans-serif; font-size: 1.6rem; letter-spacing: -0.5px;">
                        <span style="color: #0b4a22;">Growvia</span><span style="color: #55a630;">x</span>
                    </span>
                    <span class="fw-semibold" style="font-family: 'Inter', sans-serif; font-size: 0.6rem; letter-spacing: 5px; color: #0b4a22; margin-top: 2px; padding-left: 2px;"> GLOBAL</span>
                </div>
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
        print(f"Updated navbar brand in {file}")
    else:
        print(f"Navbar brand pattern not found or already updated in {file}")
