import os
import glob
import re

new_footer = """<footer class="footer-custom">
        <div class="container">
            <div class="row">
                <div class="col-lg-4 mb-4 mb-lg-0">
                    <h3 class="text-white mb-4 d-flex align-items-center gap-2"><img src="images/logo.jpeg"
                            alt="Growviax Global Logo" class="footer-logo"> Growviax</h3>
                    <p class="opacity-75 mb-4 pe-lg-4">Connecting global markets with quality & trust. Your premium
                        partner in agricultural exports.</p>
                    <div class="d-inline-flex align-items-center gap-2 px-3 py-2 rounded-pill mb-4" style="background: rgba(85, 166, 48, 0.15); border: 1px solid rgba(85, 166, 48, 0.3);">
                        <i class="ph-fill ph-certificate text-light-green fs-5"></i>
                        <span class="text-white fw-semibold" style="font-size: 0.85rem; letter-spacing: 0.5px;">100% Authorized & Certified</span>
                    </div>
                </div>
                <div class="col-lg-4 col-md-6 mb-4 mb-md-0 ps-lg-5">
                    <h4 class="footer-title">Quick Links</h4>
                    <ul class="list-unstyled">
                        <li class="mb-2"><a href="index.html">Home</a></li>
                        <li class="mb-2"><a href="products.html">Products</a></li>
                        <li class="mb-2"><a href="privacy-policy.html">Privacy Policy</a></li>
                        <li class="mb-2"><a href="terms-of-service.html">Terms of Service</a></li>
                        <li class="mb-2"><a href="contact.html">Contact Us</a></li>
                    </ul>
                </div>
                <div class="col-lg-4 col-md-6">
                    <h4 class="footer-title">Contact Us</h4>
                    <ul class="list-unstyled opacity-75">
                        <li class="mb-3 d-flex gap-2"><i class="ph-fill ph-map-pin text-light-green mt-1"></i> <span
                                style="line-height:1.4;">Ravikiran Rowhouse, Bunglow No. 1, Peth Road, PO Meri Colony,
                                Nashik-422004, Maharashtra, India</span></li>
                        <li class="mb-3 d-flex gap-2 align-items-start">
                            <i class="ph-fill ph-phone text-light-green mt-1"></i>
                            <div class="d-flex flex-column">
                                <a href="tel:+918347167497"
                                    class="text-white text-decoration-none contact-link hover-primary">+91
                                    8347167497</a>
                                <a href="tel:+919765173553"
                                    class="text-white text-decoration-none contact-link hover-primary">+91
                                    9765173553</a>
                            </div>
                        </li>
                        <li class="mb-3 d-flex gap-2"><i class="ph-fill ph-envelope-simple text-light-green mt-1"></i>
                            <a href="mailto:growviaxglobal@gmail.com"
                                class="text-white text-decoration-none contact-link hover-primary">growviaxglobal@gmail.com</a>
                        </li>
                    </ul>
                </div>
            </div>
            
            <!-- Registration Numbers Banner -->
            <div class="row mt-5 pt-4 border-top border-secondary align-items-center">
                <div class="col-md-4 mb-4 mb-md-0 d-flex gap-3 align-items-center">
                    <i class="ph-fill ph-globe-hemisphere-west text-light-green fs-1"></i>
                    <div>
                        <small class="d-block text-white-50 text-uppercase fw-semibold" style="font-size:0.7rem; letter-spacing: 1px;">Import Export Code</small>
                        <strong class="text-white fs-5">ALXPL1671J</strong>
                    </div>
                </div>
                <div class="col-md-4 mb-4 mb-md-0 d-flex gap-3 align-items-center justify-content-md-center border-md-start border-md-end border-secondary">
                    <i class="ph-fill ph-shield-check text-light-green fs-1"></i>
                    <div>
                        <small class="d-block text-white-50 text-uppercase fw-semibold" style="font-size:0.7rem; letter-spacing: 1px;">FSSAI License</small>
                        <strong class="text-white fs-5">21526072001794</strong>
                    </div>
                </div>
                <div class="col-md-4 d-flex gap-3 align-items-center justify-content-md-end">
                    <i class="ph-fill ph-receipt text-light-green fs-1"></i>
                    <div>
                        <small class="d-block text-white-50 text-uppercase fw-semibold" style="font-size:0.7rem; letter-spacing: 1px;">GSTN</small>
                        <strong class="text-white fs-5">27ALXPL1671J1ZG</strong>
                    </div>
                </div>
            </div>

            <div class="row mt-4 pt-4 border-top border-secondary">
                <div class="col-md-6 text-center text-md-start">
                    <p class="mb-0 opacity-50">&copy; 2026 Growviax Global. All Rights Reserved.</p>
                </div>
                <div class="col-md-6 text-center text-md-end mt-3 mt-md-0">
                    <a href="privacy-policy.html" class="opacity-50 me-3">Privacy Policy</a>
                    <a href="terms-of-service.html" class="opacity-50">Terms of Service</a>
                </div>
            </div>
        </div>
    </footer>"""

def update_footer(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the footer block
    # Matches from <footer class="footer-custom"> to </footer>
    pattern = re.compile(r'<footer class="footer-custom">.*?</footer>', re.DOTALL)
    
    if pattern.search(content):
        new_content = pattern.sub(new_footer, content)
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated footer in {filepath}")
        else:
            print(f"Footer is already up to date in {filepath}")
    else:
        print(f"No footer block found in {filepath}")

for html_file in glob.glob('*.html'):
    update_footer(html_file)
