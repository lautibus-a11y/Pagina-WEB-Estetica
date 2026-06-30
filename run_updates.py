import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Center Hero
html = html.replace('class="max-w-2xl lg:max-w-3xl text-center lg:text-left"', 'class="max-w-2xl lg:max-w-4xl mx-auto text-center"')
html = html.replace('class="flex flex-col sm:flex-row items-center justify-center lg:justify-start gap-3"', 'class="flex flex-col sm:flex-row items-center justify-center gap-4"')

# 2. Update Gallery Text
old_gallery_title = '''<h2 class="headline-animated headline-gradient font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-3">
                Nuestro Espacio
            </h2>
            <p class="text-pink-800/80 text-base sm:text-lg max-w-lg mx-auto">
                Un oasis de paz diseñado para tu comodidad
            </p>'''
new_gallery_title = '''<h2 class="headline-animated headline-gradient font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-3">
                Nuestra Galería
            </h2>
            <p class="text-pink-800/80 text-base sm:text-lg max-w-2xl mx-auto">
                Descubrí nuestros trabajos, resultados y cada rincón de nuestra estética a través de imágenes que reflejan la calidad, el profesionalismo y la experiencia que ofrecemos a cada cliente.
            </p>'''
html = html.replace(old_gallery_title, new_gallery_title)

# 3. Fix Ofertas layout
old_promo_div = '''        .promo-slide-full > div {
            display: flex;
            flex-direction: column;
        }'''
new_promo_div = '''        .promo-slide-full > div {
            display: flex;
            flex-direction: column;
            height: 100%;
        }'''
html = html.replace(old_promo_div, new_promo_div)

old_promo_content_css = '''        .promo-slide-content {
            width: 100%;
            padding: 2rem 2rem 2.5rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }'''
new_promo_content_css = '''        .promo-slide-content {
            width: 100%;
            padding: 2rem 2rem 2.5rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            flex: 1;
        }'''
html = html.replace(old_promo_content_css, new_promo_content_css)

# 4. Adquirir Oferta button
def replace_promo_btn(match):
    before_btn = match.group(1)
    after_btn = match.group(2)
    new_btn = f'{before_btn}<a href="https://wa.me/5491144445555?text=Hola%20GS%20Estetica%20Integral%2C%20quiero%20adquirir%20una%20oferta" target="_blank" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg font-bold text-sm text-white border border-pink-500 bg-pink-500 hover:bg-pink-600 shadow-lg shadow-pink-500/30 transition-all w-full sm:w-auto">\n                                Adquirir Oferta\n                                {after_btn}'
    return new_btn

html = re.sub(r'(<div class="promo-slide-content[^>]*>.*?<a href="#booking" class="[^"]*">)\s*(?:Obtener oferta|Reservar ahora|Consultar|Adquirir)\s*(<svg.*?</a>)', replace_promo_btn, html, flags=re.DOTALL)

# 5. Header buttons visibility
html = html.replace('text-xs font-medium text-pink-800', 'text-xs font-bold text-pink-900')
html = html.replace('text-sm font-medium text-pink-800', 'text-sm font-bold text-pink-900')

# 6. Gallery Modal
gallery_modal_html = '''
    <!-- Gallery Modal -->
    <div id="galleryModal" class="fixed inset-0 z-[100] hidden flex items-center justify-center p-4">
        <!-- Backdrop -->
        <div class="absolute inset-0 bg-black/60 backdrop-blur-md transition-opacity cursor-pointer" onclick="closeGalleryModal()"></div>
        <!-- Content -->
        <div class="relative z-10 max-w-5xl w-full max-h-[90vh] flex flex-col items-center justify-center">
            <button onclick="closeGalleryModal()" class="absolute -top-12 right-0 sm:-right-12 w-10 h-10 flex items-center justify-center text-white bg-white/20 hover:bg-white/40 backdrop-blur-sm rounded-full transition-all cursor-pointer">
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
            <img id="galleryModalImg" src="" class="max-w-full max-h-[85vh] object-contain rounded-lg shadow-2xl transform scale-95 opacity-0 transition-all duration-300" alt="Gallery Image">
        </div>
    </div>

    <script>
        function openGalleryModal(imgSrc) {
            const modal = document.getElementById('galleryModal');
            const modalImg = document.getElementById('galleryModalImg');
            modalImg.src = imgSrc;
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
            setTimeout(() => {
                modalImg.classList.remove('scale-95', 'opacity-0');
                modalImg.classList.add('scale-100', 'opacity-100');
            }, 10);
        }
        function closeGalleryModal() {
            const modal = document.getElementById('galleryModal');
            const modalImg = document.getElementById('galleryModalImg');
            modalImg.classList.remove('scale-100', 'opacity-100');
            modalImg.classList.add('scale-95', 'opacity-0');
            setTimeout(() => {
                modal.classList.add('hidden');
                document.body.style.overflow = 'auto';
                modalImg.src = '';
            }, 300);
        }
    </script>
</body>'''
if 'id="galleryModal"' not in html:
    html = html.replace('</body>', gallery_modal_html)

# Add onclick to masonry items
# Original: <img src="public/img/galeria/gallery-1.jpg" alt="Tratamiento facial" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800&q=80'"/>
# I should just replace 'onerror="this.onerror=null' with 'onclick="openGalleryModal(this.src)" onerror="this.onerror=null' 
# However this would apply to all images in the HTML. I only want the ones in masonry-grid.
# Instead let's just add it to all images inside .masonry-item
html = re.sub(r'(<div class="masonry-item gallery-reveal".*?>\s*)<img ([^>]+)>', r'\1<img \2 onclick="openGalleryModal(this.src)">', html)

# 7. Gallery border color
old_gallery_border = '''        .masonry-item::after {
            content: '';
            position: absolute;
            inset: 0;
            border: 1px solid rgba(255, 183, 197, 0.1);'''
new_gallery_border = '''        .masonry-item::after {
            content: '';
            position: absolute;
            inset: 0;
            border: 2px solid rgba(255, 133, 161, 0.5);'''
html = html.replace(old_gallery_border, new_gallery_border)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updates applied successfully")
