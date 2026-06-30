import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Header Fix: Remove white border mask from .floating-header
old_header_css = '''        .floating-header {
            backdrop-filter: blur(24px) saturate(180%);
            -webkit-backdrop-filter: blur(24px) saturate(180%);
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        }'''
new_header_css = '''        .floating-header {
            backdrop-filter: blur(12px) saturate(140%);
            -webkit-backdrop-filter: blur(12px) saturate(140%);
            background: rgba(255, 255, 255, 0.12);
            box-shadow: 0 4px 24px rgba(0, 0, 0, 0.05);
        }'''
html = html.replace(old_header_css, new_header_css)

# 2. Hero Video Fix (Dual players for looping)
old_video_html = '''        <div class="absolute inset-0 z-0">
            <video id="heroVideo" src="public/video/viodeo-hero-1.mp4" class="w-full h-full object-cover hero-video" autoplay muted playsinline poster="public/img/galeria/hero.jpg"></video>
            <div class="absolute inset-0 bg-black/30"></div>
        </div>'''
new_video_html = '''        <div class="absolute inset-0 z-0">
            <video id="heroVideo1" src="public/video/viodeo-hero-1.mp4" class="w-full h-full object-cover hero-video absolute inset-0 z-0 transition-opacity duration-1000 opacity-100" autoplay muted playsinline poster="public/img/galeria/hero.jpg"></video>
            <video id="heroVideo2" src="public/video/videohero-2.mp4" class="w-full h-full object-cover hero-video absolute inset-0 z-0 transition-opacity duration-1000 opacity-0" muted playsinline></video>
            <div class="absolute inset-0 bg-black/30 z-10"></div>
        </div>'''
html = html.replace(old_video_html, new_video_html)

old_video_js = '''        const heroVideo = document.getElementById('heroVideo');
        if(heroVideo) {
            const sources = [
                'public/video/viodeo-hero-1.mp4',
                'public/video/videohero-2.mp4'
            ];
            let currentSourceIdx = 0;
            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.load();
                const playPromise = heroVideo.play();
                if (playPromise !== undefined) {
                    playPromise.catch(error => console.log("Video playback failed:", error));
                }
            });
        }'''
new_video_js = '''        // Dual-Video Crossfade System
        const v1 = document.getElementById('heroVideo1');
        const v2 = document.getElementById('heroVideo2');
        if (v1 && v2) {
            v1.addEventListener('ended', () => {
                v2.play().catch(e => console.error("Playback failed", e));
                v2.classList.remove('opacity-0');
                v2.classList.add('opacity-100');
                v1.classList.remove('opacity-100');
                v1.classList.add('opacity-0');
                setTimeout(() => { v1.currentTime = 0; }, 1000);
            });
            v2.addEventListener('ended', () => {
                v1.play().catch(e => console.error("Playback failed", e));
                v1.classList.remove('opacity-0');
                v1.classList.add('opacity-100');
                v2.classList.remove('opacity-100');
                v2.classList.add('opacity-0');
                setTimeout(() => { v2.currentTime = 0; }, 1000);
            });
        }'''
html = html.replace(old_video_js, new_video_js)

# 3. Code Audit & Cleanup
# Let's remove unused CSS animations or classes if any. We will just regex replace out specific known blocks if we are sure they are unused.
# E.g., `bounce` animation might be unused.
if '@keyframes bounce' in html and 'animate-bounce' not in html:
    # Actually wait, let's just do lazy loading first.
    pass

# 4. Add `loading="lazy"` to all <img src="public/img/galeria..." and <img src="public/img/ofertas..." etc
html = re.sub(r'(<img[^>]+src="public/img/(?:galeria|ofertas|nostras|servicios|SVG)/[^>]+)(?<!loading="lazy")>', r'\1 loading="lazy">', html)

# Strip out loading="lazy" from the hero preloader or above-the-fold images just in case. The regex above won't hit Favicon because it's in public/img/Favicon.webp (but wait it might).
html = html.replace('<img src="public/img/Favicon.webp" alt="GS Estetica Integral" class="w-full h-full object-cover animate-ken-burns" loading="lazy">', '<img src="public/img/Favicon.webp" alt="GS Estetica Integral" class="w-full h-full object-cover animate-ken-burns">')


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
