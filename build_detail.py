import re
import os

base_dir = r'c:\Users\pc\HAIPUOIHOANGSON'
index_path = os.path.join(base_dir, 'index.html')
detail_path = os.path.join(base_dir, 'quan-tai-chi-tiet.html')

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# 1. Update index.html (wrap cards in section quan-tai with <a>)
# Find the quan-tai section
start_qt = index_content.find('<section id="quan-tai"')
end_qt = index_content.find('</section>', start_qt)

qt_content = index_content[start_qt:end_qt]

# We need to wrap <div class="package-card"...>...</div> in <a> tags
# Let's extract the image ID from the img src
# <img src="./images/quan-tai/hinh-anh-hom-go-xa-cu.jpg" alt="Hòm Gỗ Xà Cừ" class="package-img">
# -> id="hom-go-xa-cu"

def replacer(match):
    card_html = match.group(0)
    # Find image src
    img_match = re.search(r'src=".*?/hinh-anh-([a-zA-Z0-9\-]+)\.jpg"', card_html)
    if img_match:
        obj_id = img_match.group(1)
        return f'<a href="quan-tai-chi-tiet.html?id={obj_id}" style="text-decoration: none; color: inherit;">\n{card_html}\n</a>'
    return card_html

new_qt_content = re.sub(r'<div class="package-card" data-images=.*?(?:</div>\s*</div>|</div>\s*</div>)', 
                        lambda m: m.group(0) if 'h3' not in m.group(0) else replacer(m), 
                        qt_content, flags=re.DOTALL) # wait, regex might be tricky.

# Let's just find all cards individually.
# A card starts with `<div class="package-card"` and ends with `</div>` (actually it contains inner divs, so counting is better or regex with non-greedy)
# Since we know the structure exactly:
# <div class="package-card" data-images='...'>
#     <div class="package-decor"></div>
#     <img src="..." alt="..." class="...">
#     <h3>...</h3>
# </div>
# This is exactly 5 lines (or matching up to </h3>\s*</div>)

pattern = r'<div class="package-card" data-images.*?</h3>\s*</div>'
new_qt_content = re.sub(pattern, replacer, qt_content, flags=re.DOTALL)

new_index = index_content[:start_qt] + new_qt_content + index_content[end_qt:]
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(new_index)

# 2. Create quan-tai-chi-tiet.html
head_end = index_content.find('</header>') + 9
footer_start = index_content.find('<footer')

header_html = index_content[:head_end]
footer_html = index_content[footer_start:]

# Extract 4 cards for related products
cards = re.findall(pattern, qt_content, flags=re.DOTALL)
related_cards = '\n'.join([replacer(re.match(pattern, c, re.DOTALL)) for c in cards[:4]])

detail_main = f'''
    <main style="padding: 50px 0; background-color: #0a0a0a; color: #fff;">
        <div class="container" style="max-width: 1200px; margin: 0 auto; padding: 0 15px;">
            <div class="detail-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px;">
                
                <!-- CỘT TRÁI -->
                <div class="detail-left" style="text-align: center;">
                    <img id="detail-img" src="" alt="Quan Tài" style="width: 100%; border-radius: 8px; border: 2px solid #cfa85e;">
                    <h2 id="detail-title" style="text-transform: uppercase; margin-top: 15px; color: #cfa85e;">TÊN QUAN TÀI</h2>
                    
                    <div class="detail-actions" style="margin-top: 25px; display: flex; flex-direction: column; gap: 15px;">
                        <div style="display: flex; gap: 15px;">
                            <a href="tel:0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none;">Gọi: 0777995858</a>
                            <a href="https://zalo.me/0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none;">Zalo: 0777995858</a>
                        </div>
                        <button id="btn-open-modal" style="width: 100%; background-color: #cfa85e; color: #000; text-align: center; padding: 15px; border-radius: 5px; font-weight: bold; font-size: 1.1em; border: none; cursor: pointer; text-transform: uppercase;">Tư Vấn Ngay</button>
                    </div>
                </div>

                <!-- CỘT PHẢI -->
                <div class="detail-right" style="line-height: 1.6;">
                    <h3 style="color: #cfa85e; margin-bottom: 20px; font-size: 1.5em; text-transform: uppercase;">GIỚI THIỆU DANH MỤC QUAN TÀI TẠI HAI PUÔL HOÀNG SƠN</h3>
                    <p style="margin-bottom: 15px;">Việc lựa chọn một cỗ quan tài trang nghiêm, vững chãi không chỉ là sự chuẩn bị cho chuyến đi cuối cùng của người quá cố, mà còn là cách để gia quyến thể hiện tấm lòng hiếu kính và sự tôn trọng sâu sắc nhất. Hiểu được ý nghĩa thiêng liêng đó, Dịch vụ Mai táng Hai Puôl Hoàng Sơn tự hào mang đến các dòng sản phẩm quan tài cao cấp, đa dạng mẫu mã và chuẩn mực trong từng chi tiết.</p>
                    
                    <h3 style="color: #cfa85e; margin: 25px 0 15px;">Điểm Nổi Bật Của Sản Phẩm Tại Hai Puôl Hoàng Sơn:</h3>
                    <ul style="list-style-type: disc; margin-left: 20px; margin-bottom: 20px;">
                        <li style="margin-bottom: 10px;"><strong>Chất Liệu Gỗ Tự Nhiên Thượng Hạng:</strong> Chúng tôi tuyển chọn kỹ lưỡng các loại gỗ tự nhiên có độ bền bỉ cao, vân gỗ đẹp và mang giá trị tâm linh sâu sắc như: Gỗ Hương, Gỗ Căm Xe, Gỗ Trai, Gỗ Sao, Gỗ Xà Cừ... Đảm bảo sự trường tồn, chống mối mọt và vững chãi theo thời gian.</li>
                        <li style="margin-bottom: 10px;"><strong>Nghệ Thuật Chạm Khắc Tinh Xảo:</strong> Mỗi sản phẩm đều được các thợ mộc mộc lành nghề chế tác thủ công. Các họa tiết hoa văn truyền thống, tứ linh hay các biểu tượng tôn giáo đều được chạm trổ vô cùng sắc nét, mang đậm nét văn hóa và sự trang trọng tuyệt đối.</li>
                        <li style="margin-bottom: 10px;"><strong>Đa Dạng Phân Khúc & Tín Ngưỡng:</strong> Từ các mẫu hòm Đại Cối bề thế, uy nghi đến các mẫu hòm Công Ty tiêu chuẩn, hay hòm Công Giáo trang nhã... Chúng tôi cung cấp sự lựa chọn phong phú, đáp ứng trọn vẹn mọi nhu cầu, tín ngưỡng và điều kiện kinh tế của từng gia đình.</li>
                        <li style="margin-bottom: 10px;"><strong>Phụ Kiện Đồng Bộ, Chỉnh Chu:</strong> Đi kèm với quan tài là hệ thống phụ kiện trang trí nội ngoại thất (như nệm lót êm ái, tay nắm mạ vàng, nắp kính trong suốt...) được chuẩn bị đồng bộ, cao cấp và tỉ mỉ nhất.</li>
                    </ul>

                    <h3 style="color: #cfa85e; margin: 25px 0 15px;">Cam Kết Của Chúng Tôi</h3>
                    <p>Với tâm niệm "Tận tâm - Chu đáo - Trọn vẹn nghĩa tình", Hai Puôl Hoàng Sơn cam kết cung cấp những sản phẩm đúng chất lượng, đúng chuẩn loại gỗ đã tư vấn. Đội ngũ nhân viên của chúng tôi luôn túc trực để hỗ trợ, tư vấn minh bạch, giúp gia quyến chọn lựa được sản phẩm phù hợp nhất, vơi bớt đi phần nào những gánh nặng lo toan trong lúc tang gia bối rối.</p>
                </div>
            </div>
        </div>
    </main>

    <!-- SẢN PHẨM LIÊN QUAN -->
    <section class="section dark-section">
        <div class="container">
            <h2 class="section-title">SẢN PHẨM LIÊN QUAN</h2>
            <div class="packages-grid">
                {related_cards}
            </div>
        </div>
    </section>

    <!-- POPUP MODAL TƯ VẤN -->
    <div id="contact-modal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(10, 15, 25, 0.9); z-index: 9999; justify-content: center; align-items: center;">
        <div class="modal-content" style="background: #111; padding: 30px; border-radius: 8px; border: 1px solid #cfa85e; width: 90%; max-width: 500px; position: relative;">
            <span id="close-modal" style="position: absolute; top: 15px; right: 20px; color: #cfa85e; font-size: 24px; cursor: pointer;">&times;</span>
            <h3 style="color: #cfa85e; text-align: center; margin-bottom: 20px; text-transform: uppercase;">LIÊN HỆ TƯ VẤN SẢN PHẨM</h3>
            <form style="display: flex; flex-direction: column; gap: 15px;">
                <input type="text" id="modal-product" readonly style="padding: 10px; background: #222; border: 1px solid #444; color: #cfa85e; font-weight: bold;">
                <input type="text" placeholder="Họ tên (*)" required style="padding: 10px; background: #222; border: 1px solid #444; color: #fff;">
                <input type="tel" placeholder="Số điện thoại (*)" required style="padding: 10px; background: #222; border: 1px solid #444; color: #fff;">
                <input type="email" placeholder="Email" style="padding: 10px; background: #222; border: 1px solid #444; color: #fff;">
                <input type="text" placeholder="Địa chỉ" style="padding: 10px; background: #222; border: 1px solid #444; color: #fff;">
                <textarea placeholder="Ghi chú thêm" rows="3" style="padding: 10px; background: #222; border: 1px solid #444; color: #fff;"></textarea>
                <button type="submit" style="padding: 12px; background: #cfa85e; color: #000; border: none; font-weight: bold; font-size: 1.1em; cursor: pointer; border-radius: 5px;">GỬI YÊU CẦU</button>
            </form>
        </div>
    </div>
'''

# Adjust header: update menu links if needed, but since it's the exact header from index, 
# relative links like href="#quan-tai" should ideally be href="index.html#quan-tai", 
# but I will just replace `href="#` with `href="index.html#` inside the detail page header so it goes back to index.

detail_header = header_html.replace('href="#', 'href="index.html#')

full_detail_html = detail_header + detail_main + footer_html

with open(detail_path, 'w', encoding='utf-8') as f:
    f.write(full_detail_html)

print("Done")
