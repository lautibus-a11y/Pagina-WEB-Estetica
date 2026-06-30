import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update `#about` section: add title and improve card
old_about = '''                <div class="text-center lg:text-left">
                    <h2 class="headline-animated headline-dots font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-5 leading-tight">
                        Profesionalismo y confianza en cada toque
                    </h2>'''
new_about = '''                <div class="text-center lg:text-left">
                    <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-pink-50 border border-pink-100">
                        <span class="text-xs font-semibold tracking-widest uppercase text-pink-500">Sobre Nosotras</span>
                    </div>
                    <h2 class="headline-animated headline-dots font-serif text-3xl sm:text-4xl lg:text-5xl tracking-tight text-pink-900 mb-6 leading-tight">
                        Profesionalismo y confianza en cada toque
                    </h2>'''
content = content.replace(old_about, new_about)

old_carousel = '<div class="about-carousel relative z-10 overflow-hidden rounded-2xl shadow-xl shadow-pink-100/30">'
new_carousel = '<div class="about-carousel relative z-10 overflow-hidden rounded-3xl shadow-2xl shadow-pink-200/50 border-[6px] border-white/80 backdrop-blur-sm">'
content = content.replace(old_carousel, new_carousel)


# 2. Update `#contact` section
# We'll use regex to find the section and replace its content
contact_regex = r'(    <section class="py-20 sm:py-28 lg:py-32 bg-white" id="contact">).*?(    <!-- Footer -->)'
new_contact = '''    <section class="py-20 sm:py-28 lg:py-32 bg-white" id="contact">
        <div class="max-w-6xl mx-auto px-5 sm:px-8 lg:px-10">
            <div class="text-center mb-10 lg:mb-16">
                <div class="inline-block mb-4 px-4 py-1.5 rounded-full bg-pink-50 border border-pink-100">
                    <span class="text-xs font-semibold tracking-widest uppercase text-pink-500">Comunicate con nosotras</span>
                </div>
                <h2 class="headline-animated headline-diamond font-serif text-4xl sm:text-5xl lg:text-6xl tracking-tight text-pink-900 mb-4">
                    Contacto
                </h2>
                <p class="text-pink-700/70 max-w-2xl mx-auto">Estamos para responder todas tus dudas. Escribinos o visitanos en nuestro centro integral.</p>
            </div>

            <div class="flex flex-col lg:flex-row bg-white rounded-3xl shadow-2xl shadow-pink-100/50 overflow-hidden border border-pink-50">
                <!-- Info Side -->
                <div class="w-full lg:w-5/12 p-8 sm:p-12 lg:p-16 flex flex-col justify-center bg-gradient-to-br from-pink-50/50 to-white relative">
                    <div class="space-y-8 relative z-10">
                        <div class="flex items-start gap-5">
                            <span class="w-12 h-12 rounded-2xl bg-white shadow-sm flex items-center justify-center flex-shrink-0 text-pink-500 border border-pink-50">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
                                </svg>
                            </span>
                            <div>
                                <h3 class="font-bold text-pink-900 text-lg mb-1">Visitanos</h3>
                                <p class="text-pink-600/80 leading-relaxed">Av. Libertador 1234<br>CABA, Argentina</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-5">
                            <span class="w-12 h-12 rounded-2xl bg-white shadow-sm flex items-center justify-center flex-shrink-0 text-pink-500 border border-pink-50">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
                                </svg>
                            </span>
                            <div>
                                <h3 class="font-bold text-pink-900 text-lg mb-1">Llamanos</h3>
                                <p class="text-pink-600/80 leading-relaxed">+54 11 4444 5555<br>Lun a Vie 9-20h, Sáb 9-14h</p>
                            </div>
                        </div>
                        <div class="flex items-start gap-5">
                            <span class="w-12 h-12 rounded-2xl bg-white shadow-sm flex items-center justify-center flex-shrink-0 text-pink-500 border border-pink-50">
                                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
                                </svg>
                            </span>
                            <div>
                                <h3 class="font-bold text-pink-900 text-lg mb-1">Escribinos</h3>
                                <p class="text-pink-600/80 leading-relaxed">info@gesteticaintegral.com<br>Te responderemos a la brevedad</p>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Map Side -->
                <div class="w-full lg:w-7/12 min-h-[350px] sm:min-h-[450px] lg:min-h-full relative bg-gray-100">
                    <img class="absolute inset-0 w-full h-full object-cover mix-blend-multiply opacity-90 transition-all duration-700 hover:scale-105 hover:opacity-100" src="public/img/nostras/map.jpg" alt="Ubicación" onerror="this.onerror=null;this.src='https://images.unsplash.com/photo-1524661135-423995f22d0b?w=1000&q=80'"/>
                </div>
            </div>
        </div>
    </section>

'''
# Replace the contact section text
content = re.sub(contact_regex, new_contact + r'\2', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated sections")
