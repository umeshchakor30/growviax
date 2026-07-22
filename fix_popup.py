import re

new_modal = """
    <!-- Full Size Image Modal -->
    <div class="modal fade" id="imageModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-fullscreen">
            <div class="modal-content" style="background-color: rgba(0,0,0,0.85); border: none; border-radius: 0;">
                <div class="modal-header border-0 position-absolute w-100 p-4" style="z-index: 1055; top: 0;">
                    <button type="button" class="btn-close ms-auto" data-bs-dismiss="modal" aria-label="Close" style="opacity: 1; background-color: white; border-radius: 50%; padding: 1rem; box-shadow: 0 4px 12px rgba(0,0,0,0.2);"></button>
                </div>
                <div class="modal-body d-flex justify-content-center align-items-center p-4" style="height: 100vh;">
                    <img id="fullSizeImg" src="" alt="Full Size" class="img-fluid" style="max-height: 90vh; max-width: 90vw; object-fit: contain; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
                </div>
            </div>
        </div>
    </div>
"""

def update_modal(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find the modal block and replace it
    pattern = re.compile(r'    <!-- Full Size Image Modal -->.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    new_content = pattern.sub(new_modal, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated modal in {filepath}")
    else:
        print(f"No changes for {filepath} or pattern not found.")

update_modal('index.html')
update_modal('products.html')
