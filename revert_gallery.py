import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace masonry CSS rules
old_css = '''        /* Gallery Masonry */
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
new_css = '''        /* Gallery Masonry */
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
content = content.replace(old_css, new_css)

old_media_css = '''        @media (min-width: 768px) {
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
new_media_css = '''        @media (min-width: 768px) {
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
content = content.replace(old_media_css, new_media_css)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted gallery design")
