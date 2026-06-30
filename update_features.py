import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update opacity of masonry before
old_before = '''        .masonry-item::before {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.15);'''
new_before = '''        .masonry-item::before {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.35);'''
html = html.replace(old_before, new_before)

# 2. Add transition and fade-out to masonry-item
old_masonry = '''        .masonry-item {
            display: inline-block;
            margin-bottom: 0;
            width: 100%;
            overflow: hidden;
            position: relative;
            cursor: pointer;
        }'''
new_masonry = '''        .masonry-item {
            display: inline-block;
            margin-bottom: 0;
            width: 100%;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            transition: opacity 0.4s ease, transform 0.4s ease;
        }
        .masonry-item.fade-out {
            opacity: 0;
            transform: scale(0.9);
        }'''
if 'transition: opacity' not in html:
    html = html.replace(old_masonry, new_masonry)

# 3. Glassmorphism for gallery tabs
old_filters = '''        .gallery-filters {
            position: relative;
            display: inline-flex;
            background: #fdf2f8;
            padding: 0.35rem;
            border-radius: 9999px;
            border: 1px solid #fce7f3;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }'''
new_filters = '''        .gallery-filters {
            position: relative;
            display: inline-flex;
            background: rgba(253, 242, 248, 0.65);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 0.35rem;
            border-radius: 9999px;
            border: 1px solid rgba(252, 231, 243, 0.8);
            box-shadow: 0 10px 25px -5px rgba(219, 112, 147, 0.2), 0 8px 10px -6px rgba(219, 112, 147, 0.1);
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }'''
html = html.replace(old_filters, new_filters)

# 4. Modify Gallery Filtering JS to use setTimeout and fade-out
old_js = '''                document.querySelectorAll('.masonry-item').forEach(item => {
                    if (filter === 'all' || item.dataset.category === filter) {
                        item.classList.remove('hidden-gallery');
                    } else {
                        item.classList.add('hidden-gallery');
                    }
                });'''
new_js = '''                document.querySelectorAll('.masonry-item').forEach(item => {
                    if (filter === 'all' || item.dataset.category === filter) {
                        item.classList.remove('hidden-gallery');
                        setTimeout(() => item.classList.remove('fade-out'), 20);
                    } else {
                        item.classList.add('fade-out');
                        setTimeout(() => {
                            if (item.classList.contains('fade-out')) {
                                item.classList.add('hidden-gallery');
                            }
                        }, 400);
                    }
                });'''
html = html.replace(old_js, new_js)

# 5. Fix Hero Video to play sequentially
old_video = '''            <video class="w-full h-full object-cover hero-video" autoplay muted loop playsinline poster="public/img/galeria/hero.jpg">
                <source src="public/video/viodeo-hero-1.mp4" type="video/mp4">
                <source src="public/video/videohero-2.mp4" type="video/mp4">
            </video>'''
new_video = '''            <video id="heroVideo" class="w-full h-full object-cover hero-video" autoplay muted playsinline poster="public/img/galeria/hero.jpg">
                <source src="public/video/viodeo-hero-1.mp4" type="video/mp4">
            </video>'''
html = html.replace(old_video, new_video)

video_script = '''
    <script>
        const heroVideo = document.getElementById('heroVideo');
        if (heroVideo) {
            const sources = [
                'public/video/viodeo-hero-1.mp4',
                'public/video/videohero-2.mp4'
            ];
            let currentSourceIdx = 0;
            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.play();
            });
        }
    </script>
</body>'''
if 'id="heroVideo"' not in html:
    html = html.replace('</body>', video_script)

# Make sure CTA video has loop
# Already has `autoplay muted loop playsinline`. I'll verify via regex just in case.
# No need, I checked the grep output.

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied updates for video, animation, and glassmorphism.")
