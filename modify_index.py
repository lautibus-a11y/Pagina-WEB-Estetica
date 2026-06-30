import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Change Hero Button
old_btn = 'class="w-full sm:w-auto px-8 py-4 rounded-xl font-medium text-base text-pink-100 border border-pink-300/40 backdrop-blur-md bg-pink-500/15 hover:bg-pink-500/25 hover:border-pink-300/60 transition-all flex items-center justify-center gap-2"'
new_btn = 'class="w-full sm:w-auto px-8 py-4 rounded-xl font-medium text-base text-white border border-pink-500 bg-pink-500 hover:bg-pink-600 shadow-lg shadow-pink-500/30 transition-all flex items-center justify-center gap-2"'
content = content.replace(old_btn, new_btn)

# 2. Move Promotions Section
# Find <section id="promotions"> ... </section>
# The section ends at the next section or footer, we can extract it precisely
match = re.search(r'(    <!-- Promotions Section - Full-width Slider -->\s*<section class=".*?id="promotions">.*?)(    <!-- Team Section with Carousel -->)', content, re.DOTALL)
if match:
    promo_block = match.group(1)
    # Remove from original place
    content = content.replace(promo_block, '')
    # Insert after services section
    # Find the end of services section
    services_match = re.search(r'(    <!-- Services Section -->.*?    </section>\n)', content, re.DOTALL)
    if services_match:
        services_block = services_match.group(1)
        content = content.replace(services_block, services_block + '\n' + promo_block)

# 3. Update Gallery Filter CSS
old_css = '''        /* Gallery Filter Tabs */
        .gallery-filters {
            display: flex;
            flex-wrap: nowrap;
            gap: 0.5rem;
            justify-content: center;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .gallery-filters::-webkit-scrollbar {
            display: none;
        }
        .gallery-filter-btn {
            flex-shrink: 0;
            padding: 0.625rem 1.5rem;
            border-radius: 9999px;
            font-size: 0.9rem;
            font-weight: 600;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 183, 197, 0.2);
            color: rgba(159, 94, 112, 0.7);
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .gallery-filter-btn:hover {
            background: rgba(255, 183, 197, 0.15);
            border-color: rgba(255, 183, 197, 0.4);
            color: #9E5E70;
        }
        .gallery-filter-btn.active {
            background: rgba(219, 112, 147, 0.25);
            border-color: rgba(219, 112, 147, 0.5);
            color: #B8607A;
            box-shadow: 0 0 20px rgba(219, 112, 147, 0.15);
        }'''

new_css = '''        /* Gallery Filter Tabs */
        .gallery-filters-container {
            display: flex;
            justify-content: center;
            margin-top: 2rem;
            padding: 0 1.25rem;
        }
        .gallery-filters {
            position: relative;
            display: inline-flex;
            background: #fdf2f8;
            padding: 0.35rem;
            border-radius: 9999px;
            border: 1px solid #fce7f3;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .gallery-filters::-webkit-scrollbar {
            display: none;
        }
        .gallery-filter-btn {
            position: relative;
            z-index: 10;
            flex-shrink: 0;
            padding: 0.625rem 1.5rem;
            border-radius: 9999px;
            font-size: 0.95rem;
            font-weight: 600;
            color: #9d174d;
            cursor: pointer;
            background: transparent;
            border: none;
            transition: color 0.3s ease;
        }
        .gallery-filter-btn.active {
            color: white;
        }
        .gallery-filter-indicator {
            position: absolute;
            top: 0.35rem;
            bottom: 0.35rem;
            left: 0;
            border-radius: 9999px;
            background: #db7093;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 1;
            box-shadow: 0 4px 6px -1px rgba(219, 112, 147, 0.2);
            pointer-events: none;
        }'''

content = content.replace(old_css, new_css)

# 4. Update Gallery Filter HTML
old_html = '''            <div class="gallery-filters mt-8 px-5 sm:px-8 lg:px-10">
                <button class="gallery-filter-btn active" data-filter="all">Todas</button>
                <button class="gallery-filter-btn" data-filter="estetica">Estetica</button>
                <button class="gallery-filter-btn" data-filter="trabajos">Trabajos</button>
            </div>'''
new_html = '''            <div class="gallery-filters-container">
                <div class="gallery-filters" id="galleryFilters">
                    <div class="gallery-filter-indicator"></div>
                    <button class="gallery-filter-btn active" data-filter="all">Todas</button>
                    <button class="gallery-filter-btn" data-filter="estetica">Estetica</button>
                    <button class="gallery-filter-btn" data-filter="trabajos">Trabajos</button>
                </div>
            </div>'''
content = content.replace(old_html, new_html)

# 5. Update Gallery Filter JS
old_js = '''        document.querySelectorAll('.gallery-filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.gallery-filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                const filter = btn.dataset.filter;'''
new_js = '''        function updateGalleryIndicator(activeBtn) {
            const indicator = document.querySelector('.gallery-filter-indicator');
            const container = document.querySelector('#galleryFilters');
            if (!indicator || !activeBtn || !container) return;
            const containerRect = container.getBoundingClientRect();
            const btnRect = activeBtn.getBoundingClientRect();
            indicator.style.width = `${btnRect.width}px`;
            indicator.style.left = `${btnRect.left - containerRect.left + container.scrollLeft}px`;
        }
        window.addEventListener('load', () => {
            const activeBtn = document.querySelector('.gallery-filter-btn.active');
            updateGalleryIndicator(activeBtn);
        });
        
        document.querySelectorAll('.gallery-filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.gallery-filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                updateGalleryIndicator(btn);
                const filter = btn.dataset.filter;'''
content = content.replace(old_js, new_js)

# 6. Spacing and UI/UX padding
# Increase py-16 sm:py-20 to py-20 sm:py-28 for better spacing
content = content.replace('py-16 sm:py-20', 'py-20 sm:py-28 lg:py-32')
content = content.replace('pt-16 sm:pt-20', 'pt-20 sm:pt-28 lg:pt-32')
content = content.replace('pb-16 sm:pb-20', 'pb-20 sm:pb-28 lg:pb-32')

# 7. Typography
# We will make headings have tighter tracking and subtitles have better opacity and sizing
content = content.replace('text-3xl sm:text-4xl lg:text-5xl text-pink-800', 'text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900')
content = content.replace('text-pink-700/70 text-sm sm:text-base', 'text-pink-800/80 text-base sm:text-lg')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
