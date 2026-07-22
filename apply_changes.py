import os
import glob
import re

# 1. Update unify_footers.py
with open('unify_footers.py', 'r', encoding='utf-8') as f:
    unify_content = f.read()

unify_content = unify_content.replace(
    '<a href="#" class="opacity-50 me-3">Privacy Policy</a>',
    '<a href="privacy-policy.html" class="opacity-50 me-3">Privacy Policy</a>'
)
unify_content = unify_content.replace(
    '<a href="#" class="opacity-50">Terms of Service</a>',
    '<a href="terms-of-service.html" class="opacity-50">Terms of Service</a>'
)

with open('unify_footers.py', 'w', encoding='utf-8') as f:
    f.write(unify_content)

print("Updated unify_footers.py")

# 2. Extract header and footer templates from contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    contact_html = f.read()

header_match = re.search(r'(<!DOCTYPE html>.*?)<!-- Page Header -->', contact_html, re.DOTALL)
footer_match = re.search(r'(<!-- Footer.*?|<!-- Back to Top.*?|<footer class="footer-custom">.*?)(</footer>.*)', contact_html, re.DOTALL)

if not header_match:
    print("Could not find header in contact.html")
    exit(1)

header_template = header_match.group(1)

# We can just use the unify_footers.py footer logic later, but we need the scripts at the bottom
# Let's extract scripts from contact.html
scripts_match = re.search(r'(<!-- Back to Top -->.*?</html>)', contact_html, re.DOTALL)
scripts = scripts_match.group(1) if scripts_match else ""

# 3. Create dummy pages
def create_page(filename, title, content):
    html = header_template.replace('<title>Contact Us - Growviax Global</title>', f'<title>{title} - Growviax Global</title>')
    
    html += f"""<!-- Page Header -->
    <section class="page-header" style="padding: 150px 0 80px;">
        <div class="container">
            <h1 data-aos="fade-up">{title}</h1>
        </div>
    </section>

    <section class="section-padding bg-white">
        <div class="container" style="max-width: 800px; padding-bottom: 80px;">
            <div data-aos="fade-up" data-aos-delay="100">
                {content}
            </div>
        </div>
    </section>
    
    <!-- Footer placeholder -->
    <footer class="footer-custom"></footer>
    
    {scripts}
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Created {filename}")

privacy_content = """
<h3 class="mb-4">1. Introduction</h3>
<p class="text-muted mb-4">This is a dummy Privacy Policy for Growviax Global. Replace this section with your actual privacy policy content provided by your legal counsel. This page is currently a placeholder to demonstrate the layout and structure.</p>

<h3 class="mb-4">2. Information Collection</h3>
<p class="text-muted mb-4">We collect information to provide better services to our users. This may include basic information such as your name, email address, and phone number when you fill out a contact form.</p>

<h3 class="mb-4">3. Use of Information</h3>
<p class="text-muted mb-4">Any information collected is used strictly for internal purposes to process your requests and improve our services. We do not sell your personal data to third parties.</p>

<h3 class="mb-4">4. Contact Us</h3>
<p class="text-muted">If you have any questions about this Privacy Policy, please contact us at growviaxglobal@gmail.com.</p>
"""

terms_content = """
<h3 class="mb-4">1. Acceptance of Terms</h3>
<p class="text-muted mb-4">By accessing and using the Growviax Global website, you accept and agree to be bound by the terms and provisions of this agreement. This is a dummy Terms of Service page.</p>

<h3 class="mb-4">2. Description of Service</h3>
<p class="text-muted mb-4">Growviax Global provides agricultural export services. We reserve the right to modify or discontinue, temporarily or permanently, the services with or without notice.</p>

<h3 class="mb-4">3. User Conduct</h3>
<p class="text-muted mb-4">You agree to use our website only for lawful purposes. You are prohibited from violating or attempting to violate the security of the website.</p>

<h3 class="mb-4">4. Limitation of Liability</h3>
<p class="text-muted">Growviax Global shall not be liable for any direct, indirect, incidental, special or consequential damages resulting from the use or the inability to use the service.</p>
"""

create_page('privacy-policy.html', 'Privacy Policy', privacy_content)
create_page('terms-of-service.html', 'Terms of Service', terms_content)

# 4. Hide Videos Link in all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find the videos link li tag and add d-none
    new_content = re.sub(
        r'(<li class="nav-item[^>]*?>\s*<a class="nav-link.*?" href="videos\.html">Videos</a>\s*</li>)',
        r'<li class="nav-item d-none"><a class="nav-link" href="videos.html">Videos</a></li>',
        content
    )
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Hid videos link in {file}")

print("Done. Now running unify_footers.py to propagate the footer to all files (including new ones).")
os.system("python unify_footers.py")
