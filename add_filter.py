import os

js_code = """
// Product Filtering Logic
document.addEventListener("DOMContentLoaded", () => {
    const filterBtns = document.querySelectorAll('.filter-btn');
    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active state
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.getAttribute('data-filter');
                const items = document.querySelectorAll('.product-item');
                
                items.forEach(item => {
                    if (filterValue === 'all' || item.classList.contains(filterValue)) {
                        item.style.display = 'block';
                        // Re-trigger AOS animation
                        item.classList.remove('aos-animate');
                        setTimeout(() => item.classList.add('aos-animate'), 10);
                    } else {
                        item.style.display = 'none';
                        item.classList.remove('aos-animate');
                    }
                });
                
                // Refresh AOS offsets if elements moved
                if (typeof AOS !== 'undefined') {
                    setTimeout(() => AOS.refresh(), 100);
                }
            });
        });
    }
});
"""

with open('js/main.js', 'r', encoding='utf-8') as f:
    content = f.read()

if 'Product Filtering Logic' not in content:
    with open('js/main.js', 'a', encoding='utf-8') as f:
        f.write(js_code)
    print("Added filtering logic to js/main.js")
else:
    print("Filtering logic already in js/main.js")
