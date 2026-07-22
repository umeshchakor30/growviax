import os
import glob
import re

footer_new_ul = """<ul class="list-unstyled opacity-75">
                        <li class="mb-3 d-flex gap-2"><i class="ph-fill ph-map-pin text-light-green mt-1"></i> <span style="line-height:1.4;">Ravikiran Rowhouse, Bunglow No. 1, Peth Road, PO Meri Colony, Nashik-422004, Maharashtra, India</span></li>
                        <li class="mb-3 d-flex gap-2 align-items-start">
                            <i class="ph-fill ph-phone text-light-green mt-1"></i> 
                            <div class="d-flex flex-column">
                                <a href="tel:+918347167497" class="text-white text-decoration-none contact-link hover-primary">+91 8347167497</a>
                                <a href="tel:+919765173553" class="text-white text-decoration-none contact-link hover-primary">+91 9765173553</a>
                            </div>
                        </li>
                        <li class="mb-3 d-flex gap-2"><i class="ph-fill ph-envelope-simple text-light-green mt-1"></i> <a href="mailto:growviaxglobal@gmail.com" class="text-white text-decoration-none contact-link hover-primary">growviaxglobal@gmail.com</a></li>
                    </ul>"""

html_files = glob.glob('*.html')
pattern = re.compile(r'<h4 class="footer-title">Contact Us</h4>\s*<ul class="list-unstyled opacity-75">.*?</ul>', re.DOTALL)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = pattern.sub(f'<h4 class="footer-title">Contact Us</h4>\n                    {footer_new_ul}', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated footer in {file}")
    else:
        print(f"Footer pattern not found or already updated in {file}")
