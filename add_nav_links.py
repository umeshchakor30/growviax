import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to insert the two new links right before the Contact Us li
    # The Contact Us li might be on one line or multiple lines.
    pattern = re.compile(r'(<li class="nav-item">\s*<a class="nav-link[^>]*?" href="contact\.html">Contact Us</a>\s*</li>)')
    
    new_links = """<li class="nav-item"><a class="nav-link" href="privacy-policy.html">Privacy Policy</a></li>
                    <li class="nav-item"><a class="nav-link" href="terms-of-service.html">Terms of Service</a></li>
                    \\1"""
    
    new_content = pattern.sub(new_links, content)
    
    # Check if privacy-policy.html is already in there to avoid double insertion
    if 'href="privacy-policy.html"' not in content and new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added nav links to {file}")
    elif 'href="privacy-policy.html"' in content and '<li class="nav-item"><a class="nav-link" href="privacy-policy.html">Privacy Policy</a></li>' not in content:
        # It's in the footer but not in the navbar
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Added nav links to {file}")
