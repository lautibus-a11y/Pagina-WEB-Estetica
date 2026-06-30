import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Masonry Transitions and Overlay
old_masonry_css = '''        .masonry-item {
            display: inline-block;
            margin-bottom: 0;
            width: 100%;
            overflow: hidden;
            position: relative;
            cursor: pointer;
        }'''
new_masonry_css = '''        .masonry-item {
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
        }
        .masonry-item::before {
            content: '';
            position: absolute;
            inset: 0;
            background: rgba(0, 0, 0, 0.2);
            z-index: 1;
            transition: opacity 0.4s ease;
            pointer-events: none;
        }
        .masonry-item:hover::before {
            opacity: 0;
        }'''
html = html.replace(old_masonry_css, new_masonry_css)

# Remove the old ::before (which we changed earlier to a pink border). Wait, we changed ::after to pink border, ::before might not exist or might be the old one.
# Let's check if ::before already exists.
# `grep_search` showed:
# 277:         .masonry-item::before {
# 278:             content: '';
# 279:             position: absolute;
# 280:             inset: 0;
# Let's search for old ::before and remove it so we don't duplicate.
# Wait, let me just replace the existing ::before block.
