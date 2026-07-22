import os
import re

def main():
    target_dir = r"d:\mearn\Growviax"
    index_path = os.path.join(target_dir, "index.html")
    
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
        
    # Extract footer from index.html using the footer tag
    footer_match = re.search(r'<footer class="footer-custom">.*?</footer>', index_content, re.DOTALL)
    if not footer_match:
        print("Could not find footer in index.html")
        return
        
    new_footer = footer_match.group(0)
    print(f"Extracted footer from index, length: {len(new_footer)}")
    
    html_files = [
        "about.html", "contact.html", "privacy-policy.html", 
        "products.html", "terms-of-service.html", "videos.html"
    ]
    
    for filename in html_files:
        filepath = os.path.join(target_dir, filename)
        if not os.path.exists(filepath):
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace existing footer
        if re.search(r'<footer class="footer-custom">.*?</footer>', content, re.DOTALL):
            new_content = re.sub(r'<footer class="footer-custom">.*?</footer>', lambda m: new_footer, content, flags=re.DOTALL)
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated footer in {filename}")
        else:
            print(f"No footer found in {filename}")

if __name__ == "__main__":
    main()
