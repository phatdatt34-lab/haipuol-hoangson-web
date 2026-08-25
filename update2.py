import re

filepath = r'c:\Users\pc\HAIPUOIHOANGSON\quan-tai-chi-tiet.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <main> styling
content = content.replace('<main style="padding: 50px 0; background-color: #0a0a0a; color: #fff;">', '<main style="padding: 120px 0 50px 0; background-color: #fdf7e3; color: #333;">')
# Also the related product section was dark-section, let's keep it or change it? 
# "Đổi màu nền (Beige): Set background-color của toàn bộ trang chi tiết (body hoặc vùng main) thành màu be sáng"
# Right column has color #333 now due to inheritance.

# Update buttons
old_btn1 = '<a href="tel:0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none;">Gọi: 0777995858</a>'
new_btn1 = '<a href="tel:0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;"><img src="./images/chung/phone.jpg" alt="Gọi điện" style="width: 24px; height: 24px; border-radius: 50%; object-fit: cover;"> 0777995858</a>'
content = content.replace(old_btn1, new_btn1)

old_btn2 = '<a href="https://zalo.me/0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none;">Zalo: 0777995858</a>'
new_btn2 = '<a href="https://zalo.me/0777995858" class="btn" style="flex: 1; background-color: #cfa85e; color: #000; text-align: center; padding: 12px; border-radius: 5px; font-weight: bold; text-decoration: none; display: flex; align-items: center; justify-content: center; gap: 8px;"><img src="./images/chung/zalo.jpg" alt="Zalo" style="width: 24px; height: 24px; border-radius: 50%; object-fit: cover;"> 0777995858</a>'
content = content.replace(old_btn2, new_btn2)

# Slider
# Locate SẢN PHẨM LIÊN QUAN
start_slider = content.find('<div class="packages-grid">', content.find('SẢN PHẨM LIÊN QUAN'))
if start_slider != -1:
    end_slider = content.find('</div>', start_slider) # this will just find the first div close, wait.
    # A package-grid contains multiple package-cards. Let's find the closing div of packages-grid.
    # It's followed by </div>\n    </section>
    end_slider = content.find('</section>', start_slider)
    if end_slider != -1:
        # Extract the cards
        grid_html = content[start_slider:end_slider]
        # Remove the <div class="packages-grid"> and the last two </div>
        cards_html = grid_html.replace('<div class="packages-grid">', '')
        cards_html = cards_html.rsplit('</div>', 2)[0]

        slider_html = f'''<div class="related-slider-wrapper">
                <button class="slider-btn prev">&#10094;</button>
                <div class="related-slider-track">
{cards_html}                </div>
                <button class="slider-btn next">&#10095;</button>
            </div>
        </div>
'''
        content = content[:start_slider] + slider_html + content[end_slider:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated quan-tai-chi-tiet.html')

# Add CSS to style.css
css_filepath = r'c:\Users\pc\HAIPUOIHOANGSON\style.css'
with open(css_filepath, 'a', encoding='utf-8') as f:
    f.write('''
/* SLIDER SẢN PHẨM LIÊN QUAN */
.related-slider-wrapper { position: relative; overflow: hidden; padding: 10px 40px; }
.related-slider-track { display: flex; gap: 20px; overflow-x: auto; scroll-behavior: smooth; -ms-overflow-style: none; scrollbar-width: none; }
.related-slider-track::-webkit-scrollbar { display: none; }
.related-slider-track .package-card { min-width: 250px; flex-shrink: 0; }
.slider-btn { position: absolute; top: 50%; transform: translateY(-50%); background: #fff; color: #cfa85e; border: none; border-radius: 50%; width: 40px; height: 40px; font-size: 20px; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 5px rgba(0,0,0,0.3); z-index: 10; transition: 0.3s; }
.slider-btn:hover { background: #cfa85e; color: #fff; }
.slider-btn.prev { left: 0; }
.slider-btn.next { right: 0; }
''')
print('Updated style.css')

# Add JS to script.js
js_filepath = r'c:\Users\pc\HAIPUOIHOANGSON\script.js'
with open(js_filepath, 'r', encoding='utf-8') as f:
    js_content = f.read()

slider_js = '''
    // Slider Sản Phẩm Liên Quan
    const sliderTrack = document.querySelector('.related-slider-track');
    const btnPrev = document.querySelector('.slider-btn.prev');
    const btnNext = document.querySelector('.slider-btn.next');

    if (sliderTrack && btnPrev && btnNext) {
        btnNext.addEventListener('click', () => {
            const cardWidth = sliderTrack.querySelector('.package-card').clientWidth + 20;
            sliderTrack.scrollBy({ left: cardWidth, behavior: 'smooth' });
        });
        btnPrev.addEventListener('click', () => {
            const cardWidth = sliderTrack.querySelector('.package-card').clientWidth + 20;
            sliderTrack.scrollBy({ left: -cardWidth, behavior: 'smooth' });
        });
    }
'''

last_brace = js_content.rfind('});')
if last_brace != -1:
    js_content = js_content[:last_brace] + slider_js + '\n});\n'
    with open(js_filepath, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print('Updated script.js')
