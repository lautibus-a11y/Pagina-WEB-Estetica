import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the Masonry Grid with exactly 10 photos
old_masonry_block = re.search(r'<div class="masonry-grid">.*?</div>\n    </section>', html, flags=re.DOTALL)
if old_masonry_block:
    new_masonry_block = '''<div class="masonry-grid">
            <!-- 5 trabajos -->
            <div class="masonry-item gallery-reveal" data-category="trabajos" style="--delay: 0s;">
                <img src="public/img/galeria/gallery-1.jpg" alt="Tratamiento facial" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?w=800&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="trabajos" style="--delay: 0.1s;">
                <img src="public/img/galeria/gallery-2.jpg" alt="Ambiente spa" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1540555700478-4be289fbecef?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="trabajos" style="--delay: 0.2s;">
                <img src="public/img/galeria/gallery-3.jpg" alt="Productos orgánicos" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1515377905703-c4788e51af15?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="trabajos" style="--delay: 0.3s;">
                <img src="public/img/galeria/gallery-4.jpg" alt="Masaje relajante" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=800&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="trabajos" style="--delay: 0.35s;">
                <img src="public/img/nostras/about.jpg" alt="Equipo profesional" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1556760544-74068565f05c?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <!-- 5 estetica -->
            <div class="masonry-item gallery-reveal" data-category="estetica" style="--delay: 0.05s;">
                <img src="public/img/ofertas/oferta-1.jpg" alt="Limpieza facial" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1556228578-0d85b1a4d571?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="estetica" style="--delay: 0.1s;">
                <img src="public/img/ofertas/oferta-2.jpg" alt="Spa day" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1515377905703-c4788e51af15?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="estetica" style="--delay: 0.15s;">
                <img src="public/img/ofertas/oferta-3.jpg" alt="Tratamiento corporal" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1560750588-73207b1ef5b8?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="estetica" style="--delay: 0.2s;">
                <img src="public/img/servicios/placeholder-1.jpg" alt="Aromaterapia" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1600612253971-422e7f7faeb6?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
            <div class="masonry-item gallery-reveal" data-category="estetica" style="--delay: 0.25s;">
                <img src="public/img/servicios/placeholder-2.jpg" alt="Velas spa" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1602872030214-6f8a6b7f1c7e?w=600&q=80'" onclick="openGalleryModal(this.src)">
            </div>
        </div>
    </section>'''
    html = html.replace(old_masonry_block.group(0), new_masonry_block)

# 2. Add Scroll Reveal CSS
scroll_reveal_css = '''
        /* Scroll Reveal Animations */
        .sr-item {
            opacity: 0;
            transition: all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .sr-fade-up {
            transform: translateY(40px);
        }
        .sr-scale {
            transform: scale(0.92);
        }
        .sr-slide-left {
            transform: translateX(-40px);
        }
        .sr-slide-right {
            transform: translateX(40px);
        }
        .sr-item.sr-visible {
            opacity: 1;
            transform: translate(0) scale(1);
        }
    </style>'''
if '.sr-item {' not in html:
    html = html.replace('</style>', scroll_reveal_css)

# 3. Add Scroll Reveal JS
scroll_reveal_js = '''
    <script>
        // IntersectionObserver for Scroll Reveal
        const srObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const delay = entry.target.dataset.delay || 0;
                    setTimeout(() => {
                        entry.target.classList.add('sr-visible');
                    }, delay);
                    observer.unobserve(entry.target);
                }
            });
        }, {
            root: null,
            threshold: 0.15,
            rootMargin: '0px 0px -50px 0px'
        });
        
        document.querySelectorAll('.sr-item').forEach(el => srObserver.observe(el));
    </script>
</body>'''
if 'srObserver' not in html:
    html = html.replace('</body>', scroll_reveal_js)

# 4. Tag elements with sr-item and animation classes
# Hero
html = html.replace('<h1 class="font-serif', '<h1 class="font-serif sr-item sr-fade-up"')
html = html.replace('<p class="text-pink-100', '<p class="text-pink-100 sr-item sr-fade-up" data-delay="100"')
html = html.replace('<div class="flex flex-col sm:flex-row items-center justify-center gap-4">', '<div class="flex flex-col sm:flex-row items-center justify-center gap-4 sr-item sr-fade-up" data-delay="200">')

# Services
html = html.replace('class="headline-animated headline-gradient font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4"', 'class="headline-animated headline-gradient font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4 sr-item sr-fade-up"')
html = html.replace('class="text-pink-800/80 text-base sm:text-lg max-w-2xl mx-auto mb-6 sm:mb-8"', 'class="text-pink-800/80 text-base sm:text-lg max-w-2xl mx-auto mb-6 sm:mb-8 sr-item sr-fade-up" data-delay="100"')

# Bento Items (stagger delays)
def bento_stagger(match):
    idx = match.start() % 4
    delay = idx * 100
    return f'<div class="bento-item sr-item sr-scale" data-delay="{delay}"'
html = re.sub(r'<div class="bento-item"', bento_stagger, html)

# Ofertas
html = html.replace('class="headline-animated headline-dots font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-2"', 'class="headline-animated headline-dots font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-2 sr-item sr-fade-up"')
html = html.replace('<div class="promo-slider max-w-7xl mx-auto">', '<div class="promo-slider max-w-7xl mx-auto sr-item sr-fade-up" data-delay="150">')

# Galeria title
html = html.replace('class="headline-animated headline-gradient font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-3"', 'class="headline-animated headline-gradient font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-3 sr-item sr-fade-up"')

# About
html = html.replace('class="relative h-[400px] sm:h-[500px] lg:h-full rounded-2xl sm:rounded-3xl overflow-hidden shadow-2xl"', 'class="relative h-[400px] sm:h-[500px] lg:h-full rounded-2xl sm:rounded-3xl overflow-hidden shadow-2xl sr-item sr-slide-left"')
html = html.replace('class="lg:py-8"', 'class="lg:py-8 sr-item sr-slide-right"')

# Team
html = html.replace('class="headline-animated font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4"', 'class="headline-animated font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4 sr-item sr-fade-up"')
def team_stagger(match):
    idx = match.start() % 3
    delay = idx * 150
    return f'<div class="team-member sr-item sr-scale" data-delay="{delay}"'
html = re.sub(r'<div class="team-member"', team_stagger, html)

# CTA
html = html.replace('<div class="relative z-10 max-w-4xl mx-auto text-center">', '<div class="relative z-10 max-w-4xl mx-auto text-center sr-item sr-scale">')

# Contact
html = html.replace('class="headline-animated headline-gradient font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4"', 'class="headline-animated headline-gradient font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-4 sr-item sr-fade-up"')
html = html.replace('<div class="bg-white/60 backdrop-blur-md p-6 sm:p-8 rounded-2xl shadow-xl border border-pink-100">', '<div class="bg-white/60 backdrop-blur-md p-6 sm:p-8 rounded-2xl shadow-xl border border-pink-100 sr-item sr-slide-left">')
html = html.replace('<form class="bg-white p-6 sm:p-8 rounded-2xl shadow-xl border border-pink-100 h-full">', '<form class="bg-white p-6 sm:p-8 rounded-2xl shadow-xl border border-pink-100 h-full sr-item sr-slide-right">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied animations and gallery fixes.")
