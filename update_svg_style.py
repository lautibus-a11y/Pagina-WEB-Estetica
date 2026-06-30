import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update .bento-icon CSS
old_bento_icon = '''        .bento-icon {
            width: 3.5rem;
            height: 3.5rem;
            border-radius: 1rem;
            background: linear-gradient(135deg, rgba(255, 183, 197, 0.4), rgba(255, 133, 161, 0.2));
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            margin-bottom: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.4);
            transition: all 0.3s ease;
        }'''
new_bento_icon = '''        .bento-icon {
            width: 5rem;
            height: 5rem;
            border-radius: 1.5rem;
            background: #ffffff;
            box-shadow: 0 4px 15px rgba(255, 183, 197, 0.4);
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            margin-bottom: 1rem;
            border: 1px solid rgba(255, 255, 255, 0.8);
            transition: all 0.3s ease;
        }'''
content = content.replace(old_bento_icon, new_bento_icon)

old_bento_hover = '''        .bento-glass:hover .bento-icon {
            transform: scale(1.1);
            background: linear-gradient(135deg, rgba(255, 183, 197, 0.6), rgba(255, 133, 161, 0.3));
        }'''
new_bento_hover = '''        .bento-glass:hover .bento-icon {
            transform: scale(1.1);
            box-shadow: 0 8px 25px rgba(255, 183, 197, 0.6);
            background: #ffffff;
        }'''
content = content.replace(old_bento_hover, new_bento_hover)

# 2. Update img tags to remove blend mode and increase size
content = content.replace('class="w-10 h-10 object-contain mix-blend-multiply opacity-80 filter contrast-125"', 'class="w-14 h-14 object-contain transition-transform duration-500"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated SVG styles to solid white background and larger size")
