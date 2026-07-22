import re

new_offcanvas = """    <div class="offcanvas offcanvas-end" tabindex="-1" id="productQuickView" aria-labelledby="productQuickViewLabel">
        <div class="offcanvas-header border-bottom">
            <h5 class="offcanvas-title fw-bold" id="productQuickViewLabel">Product Details</h5>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class="offcanvas-body">
            <div class="mb-4 text-center">
                <img id="qv-img" src="" alt="Product Image" class="img-fluid w-100" style="max-height: 40vh; object-fit: contain; border-radius: 8px;">
            </div>
            <h3 id="qv-title" class="fw-bold mb-3 text-dark fs-4"></h3>
            <p id="qv-desc" class="text-muted mb-4 fs-6">Premium export-quality product sourced sustainably. Contact us for bulk pricing, specifications, and shipping details.</p>
            
            <div class="pt-3 mt-4 border-top">
                <a href="contact.html" class="btn-custom btn-primary-custom w-100 text-center py-3">Request a Quote</a>
            </div>
        </div>
    </div>"""

def update_offcanvas(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the offcanvas block and replace it
    pattern = re.compile(r'    <div class="offcanvas offcanvas-end" tabindex="-1" id="productQuickView".*?</div>\s*</div>', re.DOTALL)
    new_content = pattern.sub(new_offcanvas, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath} or pattern not found.")

update_offcanvas('index.html')
update_offcanvas('products.html')
