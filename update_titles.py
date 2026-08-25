import sys
import re

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Gói Phổ Thông -> Gói An Táng Phổ Thông
old_pho_thong = '''                <!-- Gói Phổ Thông -->
                <div class="package-card" data-images='["./images/dich-vu/goi-pho-thong/hinh-anh-goi-pho-thong-1.jpg", "./images/dich-vu/goi-pho-thong/hinh-anh-goi-pho-thong-2.jpg", "./images/dich-vu/goi-pho-thong/hinh-anh-goi-pho-thong-3.jpg", "./images/dich-vu/goi-pho-thong/hinh-anh-goi-pho-thong-4.jpg"]'>
                    <div class="package-decor"></div>
                    <!-- Ảnh số 1 làm ảnh đại diện -->
                    <img src="./images/dich-vu/goi-pho-thong/hinh-anh-goi-pho-thong-1.jpg" alt="Gói Phổ Thông" class="package-img">
                    <h3>Gói Phổ Thông</h3>'''

# Try regex replacement since `<!-- Ảnh số 1...` or `<div class="package-decor">` might be absent
pt_pattern = re.compile(
    r'<!-- Gói Phổ Thông -->\s*<div class="package-card" data-images=\'\[.*?\]\'>.*?<img src=".*?" alt="Gói Phổ Thông" class="package-img">\s*<h3>Gói Phổ Thông</h3>',
    re.DOTALL
)

pt_replacement = '''<!-- Gói Phổ Thông -->
                <div class="package-card" data-images='["./images/dich-vu/goi-an-tang-pho-thong/hinh-anh-goi-an-tang-pho-thong-1.jpg", "./images/dich-vu/goi-an-tang-pho-thong/hinh-anh-goi-an-tang-pho-thong-2.jpg", "./images/dich-vu/goi-an-tang-pho-thong/hinh-anh-goi-an-tang-pho-thong-3.jpg", "./images/dich-vu/goi-an-tang-pho-thong/hinh-anh-goi-an-tang-pho-thong-4.jpg"]'>
                    <img src="./images/dich-vu/goi-an-tang-pho-thong/hinh-anh-goi-an-tang-pho-thong-1.jpg" alt="Gói An Táng Phổ Thông" class="package-img">
                    <h3>Gói An Táng Phổ Thông</h3>'''
content = pt_pattern.sub(pt_replacement, content, count=1)


# 2. Gói Cao Cấp -> Gói An Táng Cao Cấp
cc_pattern = re.compile(
    r'<!-- Gói Cao Cấp -->\s*<div class="package-card featured" data-images=\'\[.*?\]\'>.*?<img src=".*?" alt="Gói Cao Cấp" class="package-img">\s*<h3>Gói Cao Cấp</h3>',
    re.DOTALL
)

cc_images = '", "'.join([f"./images/dich-vu/goi-an-tang-cao-cap/hinh-anh-goi-an-tang-cao-cap-{i}.jpg" for i in range(1, 8)])
cc_replacement = f'''<!-- Gói Cao Cấp -->
                <div class="package-card featured" data-images='["{cc_images}"]'>
                    <img src="./images/dich-vu/goi-an-tang-cao-cap/hinh-anh-goi-an-tang-cao-cap-1.jpg" alt="Gói An Táng Cao Cấp" class="package-img">
                    <h3>Gói An Táng Cao Cấp</h3>'''
content = cc_pattern.sub(cc_replacement, content, count=1)


# 3. Gói Hỏa Táng Cao Cấp
ht_pattern = re.compile(
    r'<!-- Gói Hỏa Táng Cao Cấp -->\s*<div class="package-card" data-images=\'\[.*?\]\'>.*?<img src=".*?" alt="Gói Hỏa Táng Cao Cấp" class="package-img">\s*<h3>Gói Hỏa Táng Cao Cấp</h3>',
    re.DOTALL
)

ht_images = '", "'.join([f"./images/dich-vu/goi-hoa-tang-cao-cap/hinh-anh-goi-hoa-tang-cao-cap-{i}.jpg" for i in range(1, 6)])
ht_replacement = f'''<!-- Gói Hỏa Táng Cao Cấp -->
                <div class="package-card" data-images='["{ht_images}"]'>
                    <img src="./images/dich-vu/goi-hoa-tang-cao-cap/hinh-anh-goi-hoa-tang-cao-cap-1.jpg" alt="Gói Hỏa Táng Cao Cấp" class="package-img">
                    <h3>Gói Hỏa Táng Cao Cấp</h3>'''
content = ht_pattern.sub(ht_replacement, content, count=1)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Replaced successfully")
