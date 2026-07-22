import os

modal_html = """
    <!-- Full Size Image Modal -->
    <div class="modal fade" id="imageModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered modal-xl">
            <div class="modal-content bg-transparent border-0">
                <div class="modal-header border-0 pb-0 justify-content-end" style="position: absolute; right: 0; z-index: 10;">
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close" style="background-color: white; opacity: 1; border-radius: 50%; padding: 0.8rem; margin: 0.5rem;"></button>
                </div>
                <div class="modal-body text-center p-0 position-relative">
                    <img id="fullSizeImg" src="" alt="Full Size" class="img-fluid rounded shadow" style="max-height: 90vh;">
                </div>
            </div>
        </div>
    </div>
"""

js_code = """
// Image Full Size Modal Logic
document.addEventListener("DOMContentLoaded", () => {
    // We need to attach this using event delegation since the image src changes dynamically
    document.body.addEventListener('click', (e) => {
        if (e.target && e.target.id === 'qv-img') {
            const imgSrc = e.target.src;
            if (imgSrc) {
                const fullSizeImg = document.getElementById('fullSizeImg');
                if (fullSizeImg) {
                    fullSizeImg.src = imgSrc;
                    // Close offcanvas first to prevent overlay z-index issues
                    const qvOffcanvas = document.getElementById('productQuickView');
                    const bsOffcanvas = bootstrap.Offcanvas.getInstance(qvOffcanvas);
                    if (bsOffcanvas) {
                        bsOffcanvas.hide();
                    }
                    
                    // Show modal after a tiny delay
                    setTimeout(() => {
                        const imageModalEl = document.getElementById('imageModal');
                        let bsModal = bootstrap.Modal.getInstance(imageModalEl);
                        if (!bsModal) {
                            bsModal = new bootstrap.Modal(imageModalEl);
                        }
                        bsModal.show();
                    }, 300);
                }
            }
        }
    });
    
    // Add pointer cursor to indicate it's clickable
    const style = document.createElement('style');
    style.innerHTML = '#qv-img { cursor: pointer; transition: transform 0.2s; } #qv-img:hover { transform: scale(1.02); }';
    document.head.appendChild(style);
});
"""

def add_modal_to_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'id="imageModal"' not in content:
        # Insert just before closing body tag
        content = content.replace('</body>', modal_html + '\n</body>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added modal to {filepath}")

add_modal_to_html('index.html')
add_modal_to_html('products.html')

with open('js/main.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'Image Full Size Modal Logic' not in js_content:
    with open('js/main.js', 'a', encoding='utf-8') as f:
        f.write("\n" + js_code)
    print("Added logic to js/main.js")
