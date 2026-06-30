import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Favicon
favicon_tag = '    <link rel="icon" type="image/webp" href="public/img/Favicon.webp">\n'
if 'Favicon.webp' not in html:
    html = html.replace('<title>', favicon_tag + '    <title>')

# 2. Add Preloader HTML after <body>
preloader_html = '''    <!-- Preloader -->
    <div id="cinematic-preloader" class="fixed inset-0 z-[9999] flex items-center justify-center bg-gradient-to-br from-white to-pink-100 transition-opacity duration-1000 ease-in-out">
        <div class="relative overflow-hidden w-40 h-40 sm:w-56 sm:h-56 shadow-2xl shadow-pink-200/50 rounded-full border-4 border-white">
            <img src="public/img/Favicon.webp" alt="GS Estetica Integral" class="w-full h-full object-cover animate-ken-burns">
        </div>
    </div>\n\n'''
if 'cinematic-preloader' not in html:
    html = html.replace('<body>', '<body>\n' + preloader_html)

# 3. Add Preloader CSS
preloader_css = '''
        /* Preloader Ken Burns */
        @keyframes kenBurnsPreloader {
            0% {
                transform: scale(1);
                filter: brightness(0.9);
            }
            100% {
                transform: scale(1.15);
                filter: brightness(1.05);
            }
        }
        .animate-ken-burns {
            animation: kenBurnsPreloader 3s ease-out forwards;
        }
    </style>'''
if 'kenBurnsPreloader' not in html:
    html = html.replace('</style>', preloader_css)

# 4. Add Preloader JS
preloader_js = '''
    <script>
        // Preloader Logic
        window.addEventListener('load', () => {
            const preloader = document.getElementById('cinematic-preloader');
            if (preloader) {
                setTimeout(() => {
                    preloader.style.opacity = '0';
                    setTimeout(() => {
                        preloader.style.display = 'none';
                    }, 1000);
                }, 1800);
            }
        });
    </script>
</body>'''
if 'cinematic-preloader' not in html[html.rfind('<script'):]:
    html = html.replace('</body>', preloader_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Favicon and preloader added successfully.")
