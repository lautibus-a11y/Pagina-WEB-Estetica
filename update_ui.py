import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Gallery separation and styling
# Replace masonry CSS rules
old_css = '''        /* Gallery Masonry */
        .masonry-grid {
            column-count: 2;
            column-gap: 0;
        }
        .masonry-item {
            break-inside: avoid;
            border-radius: 0;
            overflow: hidden;
            position: relative;
            cursor: pointer;
        }'''
new_css = '''        /* Gallery Masonry */
        .masonry-grid {
            column-count: 2;
            column-gap: 1.5rem;
            padding: 0 1.5rem;
        }
        .masonry-item {
            break-inside: avoid;
            margin-bottom: 1.5rem;
            border-radius: 1.5rem;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            border: 4px solid rgba(255, 255, 255, 0.4);
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.08);
            transform: translateZ(0);
        }'''
content = content.replace(old_css, new_css)

old_media_css = '''        @media (min-width: 768px) {
            .masonry-grid {
                column-count: 3;
                column-gap: 0;
            }
        }
        @media (min-width: 1024px) {
            .masonry-grid {
                column-count: 4;
                column-gap: 0;
            }
        }'''
new_media_css = '''        @media (min-width: 768px) {
            .masonry-grid {
                column-count: 3;
                column-gap: 1.5rem;
            }
        }
        @media (min-width: 1024px) {
            .masonry-grid {
                column-count: 4;
                column-gap: 1.5rem;
            }
        }'''
content = content.replace(old_media_css, new_media_css)

# 2. CTA button "ver promociones" color
# Find: <a href="#promotions" class="inline-flex items-center justify-center gap-2 px-8 py-4 text-pink-100 border border-pink-300/40 backdrop-blur-md bg-pink-500/15 hover:bg-pink-500/25 hover:border-pink-300/60 font-semibold rounded-xl transition-all duration-300 hover:-translate-y-0.5 text-lg">
old_promo_btn = 'class="inline-flex items-center justify-center gap-2 px-8 py-4 text-pink-100 border border-pink-300/40 backdrop-blur-md bg-pink-500/15 hover:bg-pink-500/25 hover:border-pink-300/60 font-semibold rounded-xl transition-all duration-300 hover:-translate-y-0.5 text-lg"'
new_promo_btn = 'class="inline-flex items-center justify-center gap-2 px-8 py-4 font-semibold rounded-xl transition-all duration-300 hover:-translate-y-0.5 text-lg text-white border border-pink-500 bg-pink-500 hover:bg-pink-600 shadow-lg shadow-pink-500/30"'
if old_promo_btn in content:
    content = content.replace(old_promo_btn, new_promo_btn)

# 3. Sobre Nosotras Title re-ordering
# Current order is Carousel then Title inside grid lg:grid-cols-2.
# We will pull the Title OUT of the grid and place it at the top of the #about max-w-7xl div.
old_about_section = '''    <section class="py-20 sm:py-28 lg:py-32 bg-white" id="about">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-10">
            <div class="grid lg:grid-cols-2 gap-10 lg:gap-16 items-center">
                <div class="relative">'''

# The title text block:
title_block = '''                <div class="text-center lg:text-left">
                    <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-pink-50 border border-pink-100">
                        <span class="text-xs font-semibold tracking-widest uppercase text-pink-500">Sobre Nosotras</span>
                    </div>
                    <h2 class="headline-animated headline-dots font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-6 leading-tight">
                        Profesionalismo y confianza en cada toque
                    </h2>'''
new_title_block = '''                <div class="text-center lg:text-left">''' # The title is moved out

new_about_section = '''    <section class="py-20 sm:py-28 lg:py-32 bg-white" id="about">
        <div class="max-w-7xl mx-auto px-5 sm:px-8 lg:px-10">
            <div class="text-center lg:text-center mb-12 lg:mb-20">
                <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-pink-50 border border-pink-100">
                    <span class="text-xs font-semibold tracking-widest uppercase text-pink-500">Sobre Nosotras</span>
                </div>
                <h2 class="headline-animated headline-dots font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-6 leading-tight">
                        Profesionalismo y confianza en cada toque
                </h2>
            </div>
            <div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
                <div class="relative order-2 lg:order-1">'''

# First replace the old_about_section
if old_about_section in content and title_block in content:
    content = content.replace(old_about_section, new_about_section)
    content = content.replace(title_block, new_title_block)
    # the old text-center lg:text-left needs order-1 lg:order-2
    content = content.replace('<div class="text-center lg:text-left">', '<div class="text-center lg:text-left order-1 lg:order-2">')

# 4. Services SVGs Replacement
svg1 = '''<svg class="w-7 h-7 text-pink-600" viewBox="0 0 48 48" fill="none">
                                <path d="M24 6C16 6 10 14 10 22C10 30 14 34 18 36C18 32 20 30 24 30C28 30 30 32 30 36C34 34 38 30 38 22C38 14 32 6 24 6Z" fill="currentColor" opacity="0.2"/>
                                <path d="M24 6C16 6 10 14 10 22C10 30 14 34 18 36C18 32 20 30 24 30C28 30 30 32 30 36C34 34 38 30 38 22C38 14 32 6 24 6Z" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <circle cx="18" cy="20" r="2" fill="currentColor"/>
                                <circle cx="30" cy="20" r="2" fill="currentColor"/>
                            </svg>'''
new_svg1 = '''<svg class="w-8 h-8 text-pink-500 transform transition-transform duration-500 hover:scale-110 hover:rotate-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z" />
</svg>'''

svg2 = '''<svg class="w-7 h-7 text-pink-600" viewBox="0 0 48 48" fill="none">
                                <path d="M8 20C8 20 12 14 24 14C36 14 40 20 40 20" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M8 26C8 26 12 32 24 32C36 32 40 26 40 26" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <circle cx="16" cy="18" r="3" stroke="currentColor" stroke-width="2"/>
                                <circle cx="32" cy="18" r="3" stroke="currentColor" stroke-width="2"/>
                                <path d="M16 28L18 34" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                                <path d="M24 28V36" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                                <path d="M32 28L30 34" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                            </svg>'''
new_svg2 = '''<svg class="w-8 h-8 text-pink-500 transform transition-transform duration-500 hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
</svg>'''

svg3 = '''<svg class="w-7 h-7 text-pink-600" viewBox="0 0 48 48" fill="none">
                                <path d="M24 8L28 16L36 18L30 26L32 36L24 32L16 36L18 26L12 18L20 16L24 8Z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>
                                <path d="M18 40L20 44" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M30 40L28 44" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <circle cx="24" cy="22" r="4" stroke="currentColor" stroke-width="2"/>
                            </svg>'''
new_svg3 = '''<svg class="w-8 h-8 text-pink-500 transform transition-transform duration-500 hover:scale-110" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M7 11.5V14m0-2.5v-6a1.5 1.5 0 113 0m-3 6a1.5 1.5 0 00-3 0v2a7.5 7.5 0 0015 0v-5a1.5 1.5 0 00-3 0m-6-3V11m0-5.5v-1a1.5 1.5 0 013 0v1m0 0V11m0-5.5a1.5 1.5 0 013 0v3m0 0V11" />
</svg>'''

svg4 = '''<svg class="w-7 h-7 text-pink-600" viewBox="0 0 48 48" fill="none">
                                <path d="M24 6C14 6 8 12 8 20C8 28 14 34 20 36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M24 6C34 6 40 12 40 20C40 28 34 34 28 36" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M8 20C8 28 14 34 20 36" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
                                <path d="M40 20C40 28 34 34 28 36" stroke="currentColor" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
                                <circle cx="24" cy="22" r="6" stroke="currentColor" stroke-width="2"/>
                                <path d="M24 18V26" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                                <path d="M20 22H28" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
                            </svg>'''
new_svg4 = '''<svg class="w-8 h-8 text-pink-500 transform transition-transform duration-500 hover:scale-110 hover:rotate-90" fill="none" viewBox="0 0 24 24" stroke="currentColor">
  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 3v2.25m6.364.386l-1.591 1.591M21 12h-2.25m-.386 6.364l-1.591-1.591M12 18.75V21m-4.773-4.227l-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z" />
</svg>'''

content = content.replace(svg1, new_svg1)
content = content.replace(svg2, new_svg2)
content = content.replace(svg3, new_svg3)
content = content.replace(svg4, new_svg4)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated HTML")
