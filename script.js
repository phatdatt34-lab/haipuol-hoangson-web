document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // 1. Chức năng Lightbox cho Dịch Vụ (Cập nhật dạng Array/Slider)
    // ==========================================
    const packageCards = document.querySelectorAll('.package-card');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.close-lightbox');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');
    const caption = document.getElementById('lightbox-caption');

    let currentImages = [];
    let currentIndex = 0;

    // Lắng nghe sự kiện click trên từng gói dịch vụ
    packageCards.forEach(card => {
        card.addEventListener('click', function() {
            // Lấy danh sách ảnh từ thuộc tính data-images
            const imagesData = this.getAttribute('data-images');
            
            if (imagesData) {
                try {
                    currentImages = JSON.parse(imagesData);
                    currentIndex = 0;
                    
                    if (currentImages.length > 0) {
                        showImage(currentIndex);
                        lightbox.style.display = 'flex';
                        document.body.style.overflow = 'hidden';
                    }
                } catch (e) {
                    console.error("Lỗi parse data-images", e);
                }
            }
        });
    });

    function showImage(index) {
        lightboxImg.src = currentImages[index];
        caption.textContent = `Hình ảnh ${index + 1} / ${currentImages.length}`;
    }

    function closeLightbox() {
        lightbox.style.display = 'none';
        document.body.style.overflow = 'auto';
    }

    // Nút điều hướng
    if (prevBtn) {
        prevBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (currentImages.length > 0) {
                currentIndex = (currentIndex > 0) ? currentIndex - 1 : currentImages.length - 1;
                showImage(currentIndex);
            }
        });
    }

    if (nextBtn) {
        nextBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            if (currentImages.length > 0) {
                currentIndex = (currentIndex < currentImages.length - 1) ? currentIndex + 1 : 0;
                showImage(currentIndex);
            }
        });
    }

    // Đóng Lightbox khi click vào nút X
    if (closeBtn) {
        closeBtn.addEventListener('click', closeLightbox);
    }

    // Đóng Lightbox khi click ra ngoài vùng ảnh
    if (lightbox) {
        lightbox.addEventListener('click', function(e) {
            if (e.target === lightbox || e.target.classList.contains('lightbox-img-wrapper')) {
                closeLightbox();
            }
        });
    }

    // Hỗ trợ phím mũi tên và ESC
    document.addEventListener('keydown', function(e) {
        if (lightbox && lightbox.style.display === 'flex') {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft' && prevBtn) prevBtn.click();
            if (e.key === 'ArrowRight' && nextBtn) nextBtn.click();
        }
    });

    // ==========================================
    // 2. Chức năng Header trong suốt / Đổi màu khi cuộn
    // ==========================================
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.98)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.backgroundColor = 'rgba(255, 255, 255, 0.8)';
            header.style.boxShadow = 'none';
        }
    });
});
