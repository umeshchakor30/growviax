import os
import glob
import re

navbar_brand_new = """<a class="navbar-brand d-flex align-items-center gap-3" href="index.html">
                <img src="images/logo.jpeg" alt="Growviax Global Logo" style="width: 55px; height: 55px; object-fit: cover; border-radius: 50%; box-shadow: 0 4px 15px rgba(0,0,0,0.1);">
                <div class="d-flex flex-column justify-content-center lh-1 mt-1 pe-2" style="min-width: 180px;">
                    <span class="fw-bold text-center" style="font-family: 'Poppins', sans-serif; font-size: 2.0rem; letter-spacing: -0.5px;">
                        <span style="color: #0b4a22;">Gr</span><span style="position: relative; display: inline-block; color: #0b4a22;">o<i class="ph-fill ph-leaf" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotate(-45deg); font-size: 0.45em; color: #55a630;"></i></span><span style="color: #0b4a22;">wvia</span><span style="color: #55a630; position: relative;">x<i class="ph-bold ph-arrow-up-right" style="position: absolute; top: 0px; right: -14px; font-size: 0.55em;"></i></span>
                    </span>
                    <div class="d-flex align-items-center justify-content-center w-100 mt-2" style="gap: 8px;">
                        <i class="ph-fill ph-leaf" style="font-size: 0.55rem; color: #55a630; transform: rotate(90deg);"></i>
                        <div style="height: 1px; flex-grow: 1; background-color: #0b4a22; opacity: 0.5;"></div>
                        <span style="font-family: 'Inter', sans-serif; font-size: 0.75rem; letter-spacing: 4px; color: #0b4a22; font-weight: 700; padding-left: 4px; line-height: 1;">GLOBAL</span>
                        <div style="height: 1px; flex-grow: 1; background-color: #0b4a22; opacity: 0.5;"></div>
                        <i class="ph-fill ph-leaf" style="font-size: 0.55rem; color: #55a630; transform: scaleX(-1) rotate(90deg);"></i>
                    </div>
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
        print(f"Updated navbar brand font sizes in {file}")
    else:
        print(f"Navbar brand pattern not found or already updated in {file}")
