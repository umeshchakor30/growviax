import os
import re

# 1. Fix CTA background in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

index_content = index_content.replace("url('images/cta-bg.jpg')", "url('images/cta-bg.jpeg')")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Fixed CTA background in index.html")

# 2. Append JS block to privacy-policy.html and terms-of-service.html
js_block = """
    <!-- JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://unpkg.com/aos@next/dist/aos.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/studio-freight/lenis@1.0.29/bundled/lenis.min.js"></script>
    <script src="js/main.js"></script>
    <script src="js/animations.js"></script>
</body>
</html>
"""

for file in ['privacy-policy.html', 'terms-of-service.html']:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # If the file does not have the JS block, append it before </body></html>
    if '<script src="https://unpkg.com/aos@next/dist/aos.js"></script>' not in content:
        # replace </body></html> (which might not even be there if I didn't include it in apply_changes.py)
        # Actually my apply_changes.py had:
        # html += f"<!-- Footer placeholder -->\n    <footer class=\"footer-custom\"></footer>\n    \n    {scripts}\n"
        # Since scripts was empty, it ended at </footer>. Let's append js_block.
        if '</body>' in content:
            content = content.replace('</body>', js_block.replace('</body>\n</html>', ''))
        else:
            content += js_block
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added JS block to {file}")
    else:
        print(f"JS block already exists in {file}")

