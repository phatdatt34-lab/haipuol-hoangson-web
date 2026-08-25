import sys
filepath = r'c:\Users\pc\HAIPUOIHOANGSON\quan-tai-chi-tiet.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<section class="section dark-section">', '<section class="section" style="background-color: #fdf7e3; padding-top: 0;">')
content = content.replace('<h2 class="section-title">SẢN PHẨM LIÊN QUAN</h2>', '<h2 class="section-title" style="color: #333;">SẢN PHẨM LIÊN QUAN</h2>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
