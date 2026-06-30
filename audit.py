import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check for aria-labels on buttons without text (like hamburger menu or close gallery)
close_btn_match = re.search(r'<button onclick="closeGalleryModal\(\)".*?</button>', html, re.DOTALL)
if close_btn_match and 'aria-label' not in close_btn_match.group(0):
    html = html.replace('<button onclick="closeGalleryModal()" class="', '<button onclick="closeGalleryModal()" aria-label="Cerrar galería" class="')

# Same for mobile menu toggle if it exists
mobile_btn_match = re.search(r'<button[^>]+id="mobileMenuBtn"[^>]*>', html)
if mobile_btn_match and 'aria-label' not in mobile_btn_match.group(0):
    html = html.replace('id="mobileMenuBtn" class="', 'id="mobileMenuBtn" aria-label="Abrir menú" class="')

# Same for scroll-to-top or anything similar
# Let's save accessibility updates
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Accessibility improved.")
