import os, re
filepath = r'c:\Users\pc\HAIPUOIHOANGSON\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

extra_match = re.search(r'<!-- Gi?i Thi?u D?ch V? B? Sung -->.*?<section id=\"extra-services\".*?</section>', content, re.DOTALL)
pkg_match = re.search(r'<!-- CÁC GÓI D?CH V?.*?<section id=\"packages\".*?</section>', content, re.DOTALL)

if not extra_match or not pkg_match:
    print('Failed to match')
else:
    print('Matched! extra len:', len(extra_match.group(0)), 'pkg len:', len(pkg_match.group(0)))
    
    new_sections = '''
    <!-- D?CH V? KHÁC -->
    <section id=\"dich-vu\" class=\"section light-section\">
        <div class=\"container\">
            <h2 class=\"section-title\">D?ch V? Khác</h2>
            <div class=\"packages-grid\">
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-thay.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-thay.jpg\" alt=\"Th?y\" class=\"package-img\">
                    <h3>Th?y</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-tan-liem.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-tan-liem.jpg\" alt=\"Nhân viên t?n li?m\" class=\"package-img\">
                    <h3>Nhân viên t?n li?m</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-dao-ty.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-dao-ty.jpg\" alt=\"Ð?o t?\" class=\"package-img\">
                    <h3>Ð?o t?</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-nhac-le.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-nhac-le.jpg\" alt=\"Nh?c l?\" class=\"package-img\">
                    <h3>Nh?c l?</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-ken-tay.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-ken-tay.jpg\" alt=\"Kèn tây\" class=\"package-img\">
                    <h3>Kèn tây</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-quay-phim-chup-hinh.jpg\" alt=\"Quay phim ch?p hình\" class=\"package-img\">
                    <h3>Quay phim ch?p hình</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-xe-tang-le.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-xe-tang-le.jpg\" alt=\"Xe tang l?\" class=\"package-img\">
                    <h3>Xe tang l?</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-ban-ghe-nha-khach.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-ban-ghe-nha-khach.jpg\" alt=\"Bàn gh? nhà khách\" class=\"package-img\">
                    <h3>Bàn gh? nhà khách</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-trang-tri-tang-le.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-trang-tri-tang-le.jpg\" alt=\"Trang trí tang l?\" class=\"package-img\">
                    <h3>Trang trí tang l?</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-rai-bong.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/dich-vu-khac/hinh-anh-nhan-vien-rai-bong.jpg\" alt=\"Nhân viên rãi bông\" class=\"package-img\">
                    <h3>Nhân viên rãi bông</h3>
                </div>
            </div>
        </div>
    </section>

    <!-- DANH M?C QUAN TÀI -->
    <section id=\"quan-tai\" class=\"section dark-section\">
        <div class=\"container\">
            <h2 class=\"section-title\">Danh M?c Quan Tài</h2>
            <div class=\"packages-grid\">
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-go-xa-cu.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-go-xa-cu.jpg\" alt=\"Hòm G? Xà C?\" class=\"package-img\">
                    <h3>Hòm G? Xà C?</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-go-sao.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-go-sao.jpg\" alt=\"Hòm G? Sao\" class=\"package-img\">
                    <h3>Hòm G? Sao</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-go-trai.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-go-trai.jpg\" alt=\"Hòm G? Trai\" class=\"package-img\">
                    <h3>Hòm G? Trai</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-go-cam-xe.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-go-cam-xe.jpg\" alt=\"Hòm G? Cam Xe\" class=\"package-img\">
                    <h3>Hòm G? Cam Xe</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-go-huong.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-go-huong.jpg\" alt=\"Hòm G? Huong\" class=\"package-img\">
                    <h3>Hòm G? Huong</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-dai-coi.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-dai-coi.jpg\" alt=\"Hòm Ð?i C?i\" class=\"package-img\">
                    <h3>Hòm Ð?i C?i</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-cong-ty.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-cong-ty.jpg\" alt=\"Hòm Công Ty\" class=\"package-img\">
                    <h3>Hòm Công Ty</h3>
                </div>
                <div class=\"package-card\" data-images='[\"./images/dich-vu/quan-tai/hinh-anh-hom-cong-giao.jpg\"]'>
                    <div class=\"package-decor\"></div>
                    <img src=\"./images/dich-vu/quan-tai/hinh-anh-hom-cong-giao.jpg\" alt=\"Hòm Công Giáo\" class=\"package-img\">
                    <h3>Hòm Công Giáo</h3>
                </div>
            </div>
        </div>
    </section>
'''
    extra_html = extra_match.group(0)
    pkg_html = pkg_match.group(0)
    
    old_extra = extra_html.replace('id=\"extra-services\"', 'id=\"extra-services-old\"').replace('display: none;', '')

    new_block = pkg_html + '\n\n' + old_extra + '\n\n' + new_sections
    
    c2 = content.replace(extra_html, '<<INSERT>>')
    c2 = c2.replace(pkg_html, '')
    c2 = c2.replace('<<INSERT>>', new_block)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c2)
    print('Done writing')
