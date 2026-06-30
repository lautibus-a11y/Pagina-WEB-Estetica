import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find all <div class="bento-icon">...</div> and replace them one by one.
# Since we know the exact order (Cosmetología, Cejas, Manos, Bienestar), we can just replace them in order.

images = [
    '<img src="public/img/SVG/SVG-Cosmetologia.webp" alt="Cosmetología" class="w-10 h-10 object-contain mix-blend-multiply opacity-80 filter contrast-125" />',
    '<img src="public/img/SVG/SVG-Pestanias-Cejas.webp" alt="Cejas y Pestañas" class="w-10 h-10 object-contain mix-blend-multiply opacity-80 filter contrast-125" />',
    '<img src="public/img/SVG/SVG-Manicuria-Pedicuria.webp" alt="Manos y Pies" class="w-10 h-10 object-contain mix-blend-multiply opacity-80 filter contrast-125" />',
    '<img src="public/img/SVG/SVG-Bienestar-integral.webp" alt="Bienestar Integral" class="w-10 h-10 object-contain mix-blend-multiply opacity-80 filter contrast-125" />'
]

# Find all blocks of <div class="bento-icon"> ... </div>
blocks = re.finditer(r'<div class="bento-icon">.*?</div>', content, re.DOTALL)
new_content = content
for i, match in enumerate(blocks):
    if i < 4:
        original = match.group(0)
        replacement = f'<div class="bento-icon">\n                            {images[i]}\n                        </div>'
        new_content = new_content.replace(original, replacement, 1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Updated SVGs to WEBP images")
