import re

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Delete extra-services-old
content = re.sub(r'<!-- Giới Thiệu Dịch Vụ Bổ Sung -->.*?<section id="extra-services-old".*?</section>\s*', '', content, flags=re.DOTALL)

# 2. Change titles
content = content.replace('<h2 class="section-title">Dịch Vụ Khác</h2>', '<h2 class="section-title">Dịch Vụ</h2>')
content = content.replace('<h2 class="section-title">Danh Mục Quan Tài</h2>', '<h2 class="section-title">Quan Tài</h2>')

# 3. Fix paths
content = content.replace('./images/dich-vu/dich-vu-khac/', './images/dich-vu-khac/')
content = content.replace('./images/dich-vu/quan-tai/', './images/quan-tai/')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Success')
