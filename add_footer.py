import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

credit_html = '''
            <!-- Developer Credit -->
            <div class="row mt-4 pt-4 border-top align-items-center" style="border-color: rgba(255,255,255,0.05) !important;">
                <div class="col-12 text-center">
                    <div class="d-inline-flex align-items-center justify-content-center gap-2 px-4 py-2 rounded-pill developer-credit" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.08); transition: all 0.3s ease;">
                        <span class="text-white-50" style="font-size: 0.8rem; letter-spacing: 0.5px;">Design & Developed by</span>
                        <span class="fw-bold" style="font-size: 0.85rem; letter-spacing: 1px; color: #8BC34A;">Umesh Chakor</span>
                        <span class="text-white-50 opacity-50 mx-1">|</span>
                        <a href="tel:+919049261203" class="text-white-50 text-decoration-none d-flex align-items-center gap-1 hover-white" style="font-size: 0.85rem; transition: all 0.3s ease;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='rgba(255,255,255,0.5)'">
                            <i class="ph-fill ph-phone-call" style="color: #8BC34A;"></i>
                            <span class="fw-medium">9049261203</span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </footer>'''

pattern = re.compile(r'(All Rights Reserved\.\s*</p>\s*</div>\s*<div.*?</div>\s*</div>\s*</div>\s*)</div>\s*</footer>', re.DOTALL)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if 'Umesh Chakor' in content:
        continue

    new_content, count = pattern.subn(r'\g<1>' + credit_html.lstrip(), content)
    
    if count > 0:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
