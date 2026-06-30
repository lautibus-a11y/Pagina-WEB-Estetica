import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Hero Title
old_hero_title = '<h1 class="font-serif sr-item sr-fade-up" text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-white leading-tight mb-8">'
new_hero_title = '<h1 class="headline-animated font-serif sr-item sr-fade-up text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-white leading-tight mb-8">'
html = html.replace(old_hero_title, new_hero_title)

# If it was already replaced partially in another way, let's use regex
html = re.sub(r'<h1 class="font-serif sr-item sr-fade-up"\s+text-3xl', '<h1 class="headline-animated font-serif sr-item sr-fade-up text-3xl', html)

# 2. Fix Gallery Tab overflow issue
old_filters_css = '''        .gallery-filters {
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
        }
        .gallery-filters::-webkit-scrollbar {
            display: none;
        }'''
new_filters_css = '''        .gallery-filters {
            position: relative;
            display: inline-flex;
            background: rgba(253, 242, 248, 0.65);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            padding: 0.35rem;
            border-radius: 9999px;
            border: 1px solid rgba(252, 231, 243, 0.8);
            box-shadow: 0 10px 25px -5px rgba(219, 112, 147, 0.2), 0 8px 10px -6px rgba(219, 112, 147, 0.1);
        }'''
html = html.replace(old_filters_css, new_filters_css)

# 3. Fix Gallery JS Animation Loop
old_gallery_js = '''                document.querySelectorAll('.masonry-item').forEach(item => {
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
new_gallery_js = '''                document.querySelectorAll('.masonry-item').forEach(item => {
                    item.classList.add('fade-out');
                });
                
                setTimeout(() => {
                    document.querySelectorAll('.masonry-item').forEach(item => {
                        if (filter === 'all' || item.dataset.category === filter) {
                            item.classList.remove('hidden-gallery');
                            setTimeout(() => item.classList.remove('fade-out'), 50);
                        } else {
                            if (item.classList.contains('fade-out')) {
                                item.classList.add('hidden-gallery');
                            }
                        }
                    });
                }, 300);'''
html = html.replace(old_gallery_js, new_gallery_js)

# 4. Fix Hero Video JS Looping
old_video_js = '''            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.play();
            });'''
new_video_js = '''            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.load();
                heroVideo.play();
            });'''
html = html.replace(old_video_js, new_video_js)


with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixes applied.")
