import re

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_block = '''            <div class="packages-grid">
                <div class="package-card" data-images='["./images/dich-vu-khac/thay/hinh-anh-thay-1.jpg", "./images/dich-vu-khac/thay/hinh-anh-thay-2.jpg", "./images/dich-vu-khac/thay/hinh-anh-thay-3.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/thay/hinh-anh-thay-1.jpg" alt="Thầy" class="package-img">
                    <h3>Thầy</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/nhan-vien-tan-liem/hinh-anh-nhan-vien-tan-liem-1.jpg", "./images/dich-vu-khac/nhan-vien-tan-liem/hinh-anh-nhan-vien-tan-liem-2.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/nhan-vien-tan-liem/hinh-anh-nhan-vien-tan-liem-1.jpg" alt="Nhân viên tẩn liệm" class="package-img">
                    <h3>Nhân Viên Tẩn Liệm</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/dao-ty/hinh-anh-dao-ty-1.jpg", "./images/dich-vu-khac/dao-ty/hinh-anh-dao-ty-2.jpg", "./images/dich-vu-khac/dao-ty/hinh-anh-dao-ty-3.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/dao-ty/hinh-anh-dao-ty-3.jpg" alt="Đạo tỳ" class="package-img">
                    <h3>Đạo Tỳ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/nhac-le/hinh-anh-nhac-le-1.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/nhac-le/hinh-anh-nhac-le-1.jpg" alt="Nhạc lễ" class="package-img">
                    <h3>Nhạc Lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/ken-tay/hinh-anh-ken-tay-1.jpg", "./images/dich-vu-khac/ken-tay/hinh-anh-ken-tay-2.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/ken-tay/hinh-anh-ken-tay-1.jpg" alt="Kèn tây" class="package-img">
                    <h3>Kèn Tây</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg" alt="Quay phim chụp hình" class="package-img">
                    <h3>Quay Phim Chụp Hình</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/xe-tang-le/hinh-anh-xe-tang-le-1.jpg", "./images/dich-vu-khac/xe-tang-le/hinh-anh-xe-tang-le-2.jpg", "./images/dich-vu-khac/xe-tang-le/hinh-anh-xe-tang-le-3.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/xe-tang-le/hinh-anh-xe-tang-le-1.jpg" alt="Xe tang lễ" class="package-img">
                    <h3>Xe Tang Lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/ban-ghe-nha-khach/hinh-anh-ban-ghe-nha-khach-1.jpg", "./images/dich-vu-khac/ban-ghe-nha-khach/hinh-anh-ban-ghe-nha-khach-2.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/ban-ghe-nha-khach/hinh-anh-ban-ghe-nha-khach-1.jpg" alt="Bàn ghế nhà khách" class="package-img">
                    <h3>Bàn Ghế Nhà Khách</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/trang-tri-tang-le/hinh-anh-trang-tri-tang-le-1.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/trang-tri-tang-le/hinh-anh-trang-tri-tang-le-1.jpg" alt="Trang trí tang lễ" class="package-img">
                    <h3>Trang Trí Tang Lễ</h3>
                </div>
                <div class="package-card" data-images='["./images/dich-vu-khac/nhan-vien-rai-bong/hinh-anh-nhan-vien-rai-bong-1.jpg", "./images/dich-vu-khac/nhan-vien-rai-bong/hinh-anh-nhan-vien-rai-bong-2.jpg"]'>
                    <div class="package-decor"></div>
                    <img src="./images/dich-vu-khac/nhan-vien-rai-bong/hinh-anh-nhan-vien-rai-bong-1.jpg" alt="Nhân viên rãi bông" class="package-img">
                    <h3>Nhân Viên Rải Bông</h3>
                </div>
            </div>'''

start_idx = content.find('            <div class="packages-grid">', content.find('<section id="dich-vu"'))
end_idx = content.find('            </div>', start_idx) + 18

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + new_block + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success")
else:
    print("Could not find block")
