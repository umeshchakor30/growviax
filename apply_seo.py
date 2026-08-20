import os
import re

seo_data = {
    'index.html': {
        'title': 'Growviax Global - Premium Agricultural Exports | Spices, Dehydrated Products & Dairy',
        'desc': 'Growviax Global is a premium international corporate export company specializing in high-quality Spices, Honey, Vegetables, Dairy, and Fresh Produce. Connecting global markets with trust.',
        'url': 'https://growviaxglobal.com/'
    },
    'products.html': {
        'title': 'Our Products | Growviax Global - Export Quality Spices & Produce',
        'desc': 'Explore our premium range of export-quality spices, dehydrated powders, fresh goods, and dairy products. Sourced sustainably for global markets.',
        'url': 'https://growviaxglobal.com/products.html'
    },
    'videos.html': {
        'title': 'Videos & Media | Growviax Global Export Operations',
        'desc': 'Watch videos showcasing Growviax Global\'s export operations, quality control processes, and premium agricultural product sourcing.',
        'url': 'https://growviaxglobal.com/videos.html'
    },
    'contact.html': {
        'title': 'Contact Us | Growviax Global - Inquiries & Bulk Orders',
        'desc': 'Get in touch with Growviax Global for bulk export inquiries, product specifications, and global shipping details. We connect you with premium agriculture.',
        'url': 'https://growviaxglobal.com/contact.html'
    },
    'privacy-policy.html': {
        'title': 'Privacy Policy | Growviax Global',
        'desc': 'Read the Privacy Policy of Growviax Global. We are committed to protecting your personal information and ensuring data security.',
        'url': 'https://growviaxglobal.com/privacy-policy.html'
    },
    'terms-of-service.html': {
        'title': 'Terms of Service | Growviax Global',
        'desc': 'Terms of Service and conditions for using the Growviax Global website and engaging in our agricultural export business.',
        'url': 'https://growviaxglobal.com/terms-of-service.html'
    }
}

base_keywords = "Export, Spices, Dehydrated Onion, Garlic Powder, Honey, Vegetables, Fresh Produce, Global Trade, Growviax Global, India Export"
site_name = "Growviax Global"
image_url = "https://growviaxglobal.com/images/logo.jpeg"

def generate_seo_block(page_data):
    return f"""
    <!-- SEO Meta Tags -->
    <title>{page_data['title']}</title>
    <meta name="description" content="{page_data['desc']}">
    <meta name="keywords" content="{base_keywords}">
    <meta name="author" content="{site_name}">
    <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
    <meta name="language" content="English">
    <link rel="canonical" href="{page_data['url']}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="{page_data['url']}">
    <meta property="og:title" content="{page_data['title']}">
    <meta property="og:description" content="{page_data['desc']}">
    <meta property="og:image" content="{image_url}">
    <meta property="og:site_name" content="{site_name}">

    <!-- Twitter -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:url" content="{page_data['url']}">
    <meta name="twitter:title" content="{page_data['title']}">
    <meta name="twitter:description" content="{page_data['desc']}">
    <meta name="twitter:image" content="{image_url}">
"""

def update_seo(filepath):
    filename = os.path.basename(filepath)
    if filename not in seo_data:
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find where <meta name="viewport" ...> ends
    viewport_pattern = re.compile(r'(<meta name="viewport"[^>]*>)')
    match = viewport_pattern.search(content)
    if not match:
        print(f"Viewport meta tag not found in {filepath}. Skipping.")
        return

    viewport_end_idx = match.end()
    
    # We want to replace everything from viewport_end_idx up to <!-- Favicon placeholder --> or <!-- Bootstrap 5 CSS -->
    # We'll use a regex to find the end boundary
    end_pattern = re.compile(r'(<!-- Favicon placeholder -->|<!-- Bootstrap 5 CSS -->|<!-- Bootstrap 5 -->)')
    end_match = end_pattern.search(content, viewport_end_idx)
    
    if not end_match:
        print(f"End boundary not found in {filepath}. Skipping.")
        return
        
    end_idx = end_match.start()
    
    # Construct new content
    new_content = content[:viewport_end_idx] + "\n" + generate_seo_block(seo_data[filename]) + "    " + content[end_idx:]
    
    # Also clean up any lingering old tags if they exist outside that block (unlikely, but just in case)
    # Actually, replacing the chunk between viewport and Bootstrap/Favicon is the safest and cleanest way
    # as it completely wipes the old `<title>` and `<meta>` tags.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated SEO tags in {filepath}")

for filename in seo_data.keys():
    if os.path.exists(filename):
        update_seo(filename)
