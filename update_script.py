filepath = r'c:\Users\pc\HAIPUOIHOANGSON\script.js'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_logic = '''
    // ==========================================
    // 4. TRANG CHI TIẾT QUAN TÀI VÀ MODAL TƯ VẤN
    // ==========================================
    const urlParams = new URLSearchParams(window.location.search);
    const productId = urlParams.get('id');

    if (productId && document.getElementById('detail-img')) {
        const productMap = {
            'hom-go-xa-cu': 'HÒM GỖ XÀ CỪ',
            'go-sao': 'HÒM GỖ SAO',
            'hom-go-trai': 'HÒM GỖ TRAI',
            'hom-go-cam-xe': 'HÒM GỖ CĂM XE',
            'hom-go-huong': 'HÒM GỖ HƯƠNG',
            'hom-dai-coi': 'HÒM ĐẠI CỐI',
            'hom-cong-ty': 'HÒM CÔNG TY',
            'hom-cong-giao': 'HÒM CÔNG GIÁO'
        };

        const titleElement = document.getElementById('detail-title');
        const imgElement = document.getElementById('detail-img');
        const modalProductInput = document.getElementById('modal-product');

        if (productMap[productId]) {
            const productName = productMap[productId];
            titleElement.innerText = productName;
            imgElement.src = `./images/quan-tai/hinh-anh-${productId}.jpg`;
            if (modalProductInput) {
                modalProductInput.value = "Tư vấn: " + productName;
            }
        }
    }

    // Modal Tư Vấn Logic
    const btnOpenModal = document.getElementById('btn-open-modal');
    const contactModal = document.getElementById('contact-modal');
    const closeContactModal = document.getElementById('close-modal');

    if (btnOpenModal && contactModal) {
        btnOpenModal.addEventListener('click', function(e) {
            e.preventDefault();
            contactModal.style.display = 'flex';
        });
    }

    if (closeContactModal && contactModal) {
        closeContactModal.addEventListener('click', function() {
            contactModal.style.display = 'none';
        });
    }

    if (contactModal) {
        contactModal.addEventListener('click', function(e) {
            if (e.target === contactModal) {
                contactModal.style.display = 'none';
            }
        });
    }
'''

# Insert before the last `});`
last_brace = content.rfind('});')
if last_brace != -1:
    new_content = content[:last_brace] + new_logic + '\n});\n'
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Success script.js")
else:
    print("Failed to find end of file")
