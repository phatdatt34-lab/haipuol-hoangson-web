// Đảm bảo DOM đã được tải hoàn toàn trước khi chạy JS
document.addEventListener('DOMContentLoaded', function() {
    
    // ==========================================
    // 1. Chức năng Lightbox cho Thư Viện Hình Ảnh
    // ==========================================
    const galleryItems = document.querySelectorAll('.gallery-item img');
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const closeBtn = document.querySelector('.close-lightbox');

    // Mở Lightbox khi click vào ảnh
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            lightbox.style.display = 'flex'; // Hiển thị overlay mờ
            lightboxImg.src = this.src;      // Lấy link ảnh được click gán vào ảnh trong lightbox
            
            // Ngăn cuộn trang ở dưới khi mở lightbox
            document.body.style.overflow = 'hidden'; 
        });
    });

    // Đóng Lightbox khi click vào nút X
    closeBtn.addEventListener('click', function() {
        closeLightbox();
    });

    // Đóng Lightbox khi click ra ngoài vùng ảnh
    lightbox.addEventListener('click', function(e) {
        if (e.target !== lightboxImg) {
            closeLightbox();
        }
    });

    // Đóng Lightbox bằng nút ESC trên bàn phím
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.style.display === 'flex') {
            closeLightbox();
        }
    });

    // Hàm tiện ích để đóng lightbox
    function closeLightbox() {
        lightbox.style.display = 'none';
        document.body.style.overflow = 'auto'; // Cho phép cuộn trang lại
    }

    // ==========================================
    // 2. Chức năng Header trong suốt / Đổi màu khi cuộn
    // ==========================================
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            header.style.backgroundColor = 'rgba(18, 18, 18, 0.98)';
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.5)';
        } else {
            header.style.backgroundColor = 'rgba(18, 18, 18, 0.8)';
            header.style.boxShadow = 'none';
        }
    });
});
