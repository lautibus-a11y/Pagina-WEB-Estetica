import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Fix Masonry White Space (convert to Flex Grid)
old_masonry_css = '''        /* Gallery Masonry */
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
        }
        .masonry-item img {
            width: 100%;
            display: block;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }'''
new_masonry_css = '''        /* Gallery Flex Grid */
        .masonry-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 0;
        }
        .masonry-item {
            flex: 1 1 50%;
            height: 250px;
            border-radius: 0;
            overflow: hidden;
            position: relative;
            cursor: pointer;
            transition: opacity 0.4s ease, transform 0.4s ease;
        }
        .masonry-item.fade-out {
            opacity: 0;
            transform: scale(0.9);
        }
        .masonry-item img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            display: block;
            transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }'''
html = html.replace(old_masonry_css, new_masonry_css)

old_media_masonry = '''        @media (min-width: 768px) {
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
new_media_masonry = '''        @media (min-width: 768px) {
            .masonry-item {
                flex: 1 1 33.333%;
                height: 300px;
            }
        }
        @media (min-width: 1024px) {
            .masonry-item {
                flex: 1 1 20%;
                height: 350px;
            }
        }'''
html = html.replace(old_media_masonry, new_media_masonry)

# 2. Fix Hero Video Looping HTML
old_video_html = '''            <video id="heroVideo" class="w-full h-full object-cover hero-video" autoplay muted playsinline poster="public/img/galeria/hero.jpg">
                <source src="public/video/viodeo-hero-1.mp4" type="video/mp4">
            </video>'''
new_video_html = '''            <video id="heroVideo" src="public/video/viodeo-hero-1.mp4" class="w-full h-full object-cover hero-video" autoplay muted playsinline poster="public/img/galeria/hero.jpg"></video>'''
html = html.replace(old_video_html, new_video_html)

# 3. Add explicit load and play handling for the video JS
old_video_js = '''            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.load();
                heroVideo.play();
            });'''
new_video_js = '''            heroVideo.addEventListener('ended', () => {
                currentSourceIdx = (currentSourceIdx + 1) % sources.length;
                heroVideo.src = sources[currentSourceIdx];
                heroVideo.load();
                const playPromise = heroVideo.play();
                if (playPromise !== undefined) {
                    playPromise.catch(error => console.log("Video playback failed:", error));
                }
            });'''
html = html.replace(old_video_js, new_video_js)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Finished final fixes.")
