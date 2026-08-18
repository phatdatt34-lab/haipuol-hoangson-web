document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // JS CHO LIGHTBOX MODAL MỚI (Hình chính & Thumbnails)
    // ==========================================
    const packageCards = document.querySelectorAll('.package-card');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const thumbnailContainer = document.getElementById('lightbox-thumbnails');
    const closeBtn = document.querySelector('.close-lightbox');

    // Thư viện ảnh cũ (nếu có click thì mở ảnh đơn giản)
    const galleryItems = document.querySelectorAll('.gallery-item img');
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            openLightbox([this.src]);
        });
    });

    // Bắt sự kiện click vào Card Gói Dịch Vụ
    packageCards.forEach(card => {
        card.addEventListener('click', function(e) {
            // Không ăn click nếu bấm vào thẻ a hay nút linh tinh bên trong, 
            // nhưng ở đây ta bắt click toàn card.
            const imagesData = this.getAttribute('data-images');
            
            if (imagesData) {
                try {
                    const imagesArray = JSON.parse(imagesData);
                    if (imagesArray.length > 0) {
                        openLightbox(imagesArray);
                    }
                } catch (err) {
                    console.error("Lỗi đọc đường dẫn ảnh gói dịch vụ:", err);
                }
            }
        });
    });

    // Hàm mở Lightbox và khởi tạo Thumbnail
    function openLightbox(images) {
        // Reset container thumbnails
        thumbnailContainer.innerHTML = '';
        
        // Render ảnh chính (mặc định lấy ảnh đầu tiên)
        showMainImage(images[0], 0);
        
        // Render danh sách ảnh thu nhỏ
        images.forEach((src, index) => {
            const thumb = document.createElement('img');
            thumb.src = src;
            thumb.alt = `Thumbnail ${index + 1}`;
            
            // Xử lý lỗi load ảnh
            thumb.onerror = function() {
                this.src = 'https://via.placeholder.com/150?text=Loi+Anh';
            };
            
            // Nếu là ảnh đang chọn thì thêm viền sáng
            if (index === 0) {
                thumb.classList.add('active');
            }
            
            // Lắng nghe sự kiện click trên từng thumbnail
            thumb.addEventListener('click', (e) => {
                e.stopPropagation(); // Ngăn sự kiện đóng lightbox
                showMainImage(src, index);
            });
            
            thumbnailContainer.appendChild(thumb);
        });

        // Hiển thị modal
        lightbox.style.display = 'flex';
        document.body.style.overflow = 'hidden'; // Khóa scroll nền
    }

    // Hàm hiển thị ảnh chính khi click Thumbnail
    function showMainImage(src, activeIndex) {
        // Đổi ảnh với hiệu ứng mờ nhẹ
        lightboxImg.style.opacity = '0.5';
        setTimeout(() => {
            lightboxImg.src = src;
            lightboxImg.style.opacity = '1';
        }, 150);

        // Fallback ảnh lỗi
        lightboxImg.onerror = function() {
            this.src = 'https://via.placeholder.com/800x600?text=Hinh+Anh+Dang+Duoc+Cap+Nhat';
        };

        // Đổi trạng thái viền sáng (active) của các thumbnails
        const thumbs = thumbnailContainer.querySelectorAll('img');
        thumbs.forEach((thumb, idx) => {
            if (idx === activeIndex) {
                thumb.classList.add('active');
                // Tự động cuộn thumbnail đó vào giữa màn hình nếu danh sách quá dài
                thumb.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
            } else {
                thumb.classList.remove('active');
            }
        });
    }

    // Hàm đóng Lightbox
    function closeLightbox() {
        lightbox.style.display = 'none';
        document.body.style.overflow = 'auto'; // Cho cuộn trang lại
    }

    // Nút đóng X
    if (closeBtn) {
        closeBtn.addEventListener('click', closeLightbox);
    }

    // Bấm ra ngoài vùng tối sẽ đóng modal
    if (lightbox) {
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox || e.target.classList.contains('lightbox-img-wrapper')) {
                closeLightbox();
            }
        });
    }

    // Nút ESC trên bàn phím
    document.addEventListener('keydown', function(e) {
        if (lightbox && lightbox.style.display === 'flex' && e.key === 'Escape') {
            closeLightbox();
        }
    });

    // ==========================================
    // 2. Chức năng Đổi màu Header trong suốt khi cuộn trang
    // ==========================================
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.9)';
            header.style.boxShadow = 'none';
        }
    });

    // ==========================================
    // 3. Hamburger Menu cho Mobile
    // ==========================================
    const mobileMenuBtn = document.getElementById('mobile-menu');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', function(e) {
            navMenu.classList.toggle('active');
            e.stopPropagation();
        });

        // Đóng menu khi click ra ngoài
        document.addEventListener('click', function(e) {
            if (!navMenu.contains(e.target) && e.target !== mobileMenuBtn && !mobileMenuBtn.contains(e.target)) {
                navMenu.classList.remove('active');
            }
        });

        // Đóng menu khi bấm vào bất kỳ link nào bên trong
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
            });
        });
    }
});
