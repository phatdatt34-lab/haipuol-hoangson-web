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

# 2. Fix quan-tai-chi-tiet.html
start_rel = content.find('<!-- SẢN PHẨM LIÊN QUAN -->')
end_rel = content.find('<!-- POPUP MODAL TƯ VẤN -->', start_rel)

new_rel_section = f'''<!-- SẢN PHẨM LIÊN QUAN -->
    <section class="section" style="background-color: #fdf7e3; padding-top: 0;">
        <div class="container">
            <h2 class="section-title" style="color: #333;">SẢN PHẨM LIÊN QUAN</h2>
            <div class="related-slider-wrapper">
                <button class="slider-btn prev">&#10094;</button>
                <div class="related-slider-track">
{cards_html}
                </div>
                <button class="slider-btn next">&#10095;</button>
            </div>
        </div>
    </section>

    '''

content = content[:start_rel] + new_rel_section + content[end_rel:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed HTML structure')
