import sys
import re

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\quan-tai-chi-tiet.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

index_path = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Get the 8 cards from index.html section quan-tai
start_qt = index_content.find('<section id="quan-tai"')
end_qt = index_content.find('</section>', start_qt)
qt_content = index_content[start_qt:end_qt]

# Find all <a> tags inside <div class="packages-grid">...
grid_start = qt_content.find('<div class="packages-grid">')
grid_end = qt_content.find('</div>\n        </div>', grid_start)
cards_html = qt_content[grid_start + len('<div class="packages-grid">'):grid_end].strip()

# 2. Replace the content inside <div class="related-slider-track">
start_track = content.find('<div class="related-slider-track">')
end_track = content.find('</div>', start_track)

if start_track != -1 and end_track != -1:
    new_content = content[:start_track + len('<div class="related-slider-track">')] + '\n' + cards_html + '\n                ' + content[end_track:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated HTML")

# 3. Update style.css
css_filepath = r'c:\Users\pc\HAIPUOIHOANGSON\style.css'
with open(css_filepath, 'r', encoding='utf-8') as f:
    css_content = f.read()

css_content = css_content.replace('.related-slider-track .package-card { min-width: 250px; flex-shrink: 0; }', 
                                  '.related-slider-track a { flex-shrink: 0; text-decoration: none; }\n.related-slider-track .package-card { min-width: 250px; flex-shrink: 0; }')

with open(css_filepath, 'w', encoding='utf-8') as f:
    f.write(css_content)
print("Updated CSS")

# 4. Check JS
js_filepath = r'c:\Users\pc\HAIPUOIHOANGSON\script.js'
with open(js_filepath, 'r', encoding='utf-8') as f:
    js_content = f.read()

# The JS already calculates clientWidth of .package-card:
# const cardWidth = sliderTrack.querySelector('.package-card').clientWidth + 20;
# This works fine even if wrapped in <a>.
print("Checked JS")
