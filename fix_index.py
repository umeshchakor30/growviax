import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

index_to_cut = -1
for i, line in enumerate(lines):
    if "gsap.min.js" in line:
        index_to_cut = i + 1
        break

if index_to_cut != -1:
    correct_end = """    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
    <script type="module">
        import { CountUp } from 'https://cdnjs.cloudflare.com/ajax/libs/countup.js/2.8.0/countUp.min.js';
        window.countUp = { CountUp };
    </script>
    <script src="js/main.js"></script>
    <script src="js/animations.js"></script>
    <script src="https://unpkg.com/three"></script>
    <script src="https://unpkg.com/globe.gl"></script>
    <script src="js/globe-init.js"></script>
</body>
</html>"""
    
    new_lines = lines[:index_to_cut]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
        f.write(correct_end)
