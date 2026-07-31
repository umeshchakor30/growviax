import os

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the text inside the span
    if '>9049261203</span>' in content:
        content = content.replace('>9049261203</span>', '>+91 9049261203</span>')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {f}')
