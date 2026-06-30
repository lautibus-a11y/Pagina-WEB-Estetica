import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove blur from masonry-item img
old_masonry = '''        .masonry-item img {
            width: 100%;
            display: block;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94), filter 0.5s ease;
            filter: blur(1px);
        }
        .masonry-item:hover {
            z-index: 10;
        }
        .masonry-item:hover img {
            transform: scale(1.15);
            filter: blur(0);
        }'''
new_masonry = '''        .masonry-item img {
            width: 100%;
            display: block;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }
        .masonry-item:hover {
            z-index: 10;
        }
        .masonry-item:hover img {
            transform: scale(1.15);
        }'''
html = html.replace(old_masonry, new_masonry)

# 2. Fix the broken double <a> tag for the first 3 offers
bad_btn_pattern = r'<a href="#booking"[^>]*>\s*<a href="https://wa.me/[^>]*>\s*Adquirir Oferta\s*<svg.*?</svg>\s*</a>'
clean_btn = '''<a href="https://wa.me/5491144445555?text=Hola%20GS%20Estetica%20Integral%2C%20quiero%20adquirir%20una%20oferta" target="_blank" class="inline-flex items-center justify-center gap-2 px-6 py-3 rounded-lg font-bold text-sm text-white bg-pink-500 hover:bg-pink-600 shadow-lg shadow-pink-500/30 transition-all w-full sm:w-auto">
                                Adquirir Oferta
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                                </svg>
                            </a>'''
html = re.sub(bad_btn_pattern, clean_btn, html, flags=re.DOTALL)

# 3. Fix the last offer missing button (has href="#contact")
bad_btn_pattern_4 = r'<a href="#contact"[^>]*>\s*Adquirir\s*<svg.*?</svg>\s*</a>'
html = re.sub(bad_btn_pattern_4, clean_btn, html, flags=re.DOTALL)

# 4. Service modal button solid pink
old_service_btn = '''        .service-whatsapp-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: 1px solid rgba(255, 255, 255, 0.35);
            border-radius: 0.625rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            margin-top: 0.5rem;
        }
        .service-whatsapp-btn:hover {
            background: rgba(255, 255, 255, 0.25);
            border-color: rgba(255, 255, 255, 0.5);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
            transform: translateY(-1px);
        }'''
new_service_btn = '''        .service-whatsapp-btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            background: #ec4899; /* pink-500 */
            color: white;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border-radius: 0.625rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
            margin-top: 0.5rem;
        }
        .service-whatsapp-btn:hover {
            background: #db2777; /* pink-600 */
            box-shadow: 0 8px 24px rgba(236, 72, 153, 0.3);
            transform: translateY(-1px);
        }'''
html = html.replace(old_service_btn, new_service_btn)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bug fixes applied")
