import os
files = ['videos.html', 'terms-of-service.html', 'products.html', 'privacy-policy.html', 'index.html', 'contact.html', 'apply_seo.py']
for f in files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        new_content = content.replace('www.growviax.com', 'growviaxglobal.com')
        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
    except Exception as e:
        print(f"Error processing {f}: {e}")
