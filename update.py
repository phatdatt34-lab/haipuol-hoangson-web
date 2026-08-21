import os

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_sections = '''
    <!-- DỊCH VỤ KHÁC -->
    <section id="dich-vu" class="section light-section">
        <div class="container">
            <h2 class="section-title">Dịch Vụ Khác</h2>
            <div class="packages-grid">
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-thay.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-thay.jpg" alt="Thầy" class="package-img">
                    <h3>Thầy</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-tan-liem.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-tan-liem.jpg" alt="Nhân viên tẩn liệm" class="package-img">
                    <h3>Nhân viên tẩn liệm</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-dao-ty.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-dao-ty.jpg" alt="Đạo tỳ" class="package-img">
                    <h3>Đạo tỳ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-nhac-le.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-nhac-le.jpg" alt="Nhạc lễ" class="package-img">
                    <h3>Nhạc lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-ken-tay.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-ken-tay.jpg" alt="Kèn tây" class="package-img">
                    <h3>Kèn tây</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg" alt="Quay phim chụp hình" class="package-img">
                    <h3>Quay phim chụp hình</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-xe-tang-le.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-xe-tang-le.jpg" alt="Xe tang lễ" class="package-img">
                    <h3>Xe tang lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-ban-ghe-nha-khach.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-ban-ghe-nha-khach.jpg" alt="Bàn ghế nhà khách" class="package-img">
                    <h3>Bàn ghế nhà khách</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-trang-tri-tang-le.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-trang-tri-tang-le.jpg" alt="Trang trí tang lễ" class="package-img">
                    <h3>Trang trí tang lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-rai-bong.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-rai-bong.jpg" alt="Nhân viên rãi bông" class="package-img">
                    <h3>Nhân viên rãi bông</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- DANH MỤC QUAN TÀI -->
    <section id="quan-tai" class="section dark-section">
        <div class="container">
            <h2 class="section-title">Danh Mục Quan Tài</h2>
            <div class="packages-grid">
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-go-xa-cu.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-go-xa-cu.jpg" alt="Hòm Gỗ Xà Cừ" class="package-img">
                    <h3>Hòm Gỗ Xà Cừ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-go-sao.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-go-sao.jpg" alt="Hòm Gỗ Sao" class="package-img">
                    <h3>Hòm Gỗ Sao</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-go-trai.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-go-trai.jpg" alt="Hòm Gỗ Trai" class="package-img">
                    <h3>Hòm Gỗ Trai</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-go-cam-xe.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-go-cam-xe.jpg" alt="Hòm Gỗ Căm Xe" class="package-img">
                    <h3>Hòm Gỗ Căm Xe</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-go-huong.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-go-huong.jpg" alt="Hòm Gỗ Hương" class="package-img">
                    <h3>Hòm Gỗ Hương</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-dai-coi.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-dai-coi.jpg" alt="Hòm Đại Cối" class="package-img">
                    <h3>Hòm Đại Cối</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-cong-ty.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-cong-ty.jpg" alt="Hòm Công Ty" class="package-img">
                    <h3>Hòm Công Ty</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu/quan-tai/hinh-anh-hom-cong-giao.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu/quan-tai/hinh-anh-hom-cong-giao.jpg" alt="Hòm Công Giáo" class="package-img">
                    <h3>Hòm Công Giáo</h3>
                </div>
            </div>
        </div>
    </section>
'''

start_extra = 0
end_extra = 0
start_pkg = 0
end_pkg = 0

for i, line in enumerate(lines):
    if 'id="extra-services"' in line:
        start_extra = i - 1
    if 'id="packages"' in line:
        start_pkg = i - 1

for i in range(start_extra + 2, len(lines)):
    if '</section>' in lines[i]:
        end_extra = i
        break
for i in range(start_pkg + 2, len(lines)):
    if '</section>' in lines[i]:
        end_pkg = i
        break

extra_html = lines[start_extra:end_extra+1]
pkg_html = lines[start_pkg:end_pkg+1]

# Modify extra ID
extra_html = [line.replace('id="extra-services"', 'id="extra-services-old"') for line in extra_html]

# Swap
out = lines[:start_extra] + pkg_html + extra_html + [new_sections + '\n'] + lines[end_pkg+1:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(''.join(out))

print("Successfully written sections!")
