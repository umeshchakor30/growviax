/**
 * Main Javascript logic for Growviax
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Preloader
  const preloader = document.getElementById('preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      setTimeout(() => {
        preloader.style.opacity = '0';
        setTimeout(() => {
          preloader.style.display = 'none';
        }, 500);
      }, 500); // Small delay to ensure smooth transition
    });
  }

  // 2. Lenis Smooth Scrolling (Removed to fix mouse wheel scrolling issues)
  let lenis = null;

  // 3. Navbar Scroll Effect
  const navbar = document.querySelector('.navbar-custom');
  if (navbar) {
    const onScroll = () => {
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll);
    onScroll(); // Check on init
  }

  // 4. Back to Top Button
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('active');
      } else {
        backToTopBtn.classList.remove('active');
      }
    });

    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      if (lenis) {
        lenis.scrollTo(0);
      } else {
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      }
    });
  }

  // 5. Initialize active menu item based on current URL
  const currentLocation = location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentLocation) {
      link.classList.add('active');
    }
  });

});


// Initialize Hero Swiper
if (document.querySelector('.hero-swiper')) {
    const heroSwiper = new Swiper('.hero-swiper', {
        effect: 'cards',
        grabCursor: true,
        centeredSlides: true,
        slidesPerView: 'auto',
        loop: true,
        autoplay: {
            delay: 3500,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
}


// Custom Magnetic Cursor Logic
const cursor = document.querySelector('.custom-cursor');
const cursorFollower = document.querySelector('.custom-cursor-follower');

if (cursor && cursorFollower) {
    document.addEventListener('mousemove', (e) => {
        cursor.style.left = e.clientX + 'px';
        cursor.style.top = e.clientY + 'px';
        
        cursorFollower.style.left = e.clientX + 'px';
        cursorFollower.style.top = e.clientY + 'px';
    });

    const hoverElements = document.querySelectorAll('a, button, .swiper-slide');
    hoverElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            cursor.classList.add('hovering');
            cursorFollower.classList.add('hovering');
        });
        el.addEventListener('mouseleave', () => {
            cursor.classList.remove('hovering');
            cursorFollower.classList.remove('hovering');
        });
    });
}


// Product Quick View Offcanvas Logic
document.querySelectorAll('.quick-view-trigger').forEach(trigger => {
    trigger.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Find the closest product card
        const card = this.closest('.product-card') || this.closest('.card');
        if (!card) return;
        
        // Extract product data
        const titleEl = card.querySelector('.product-title, .card-title');
        const imgEl = card.querySelector('img');
        
        if (titleEl && imgEl) {
            const title = titleEl.innerText;
            const imgSrc = imgEl.src;
            
            // Populate offcanvas
            document.getElementById('qv-title').innerText = title;
            document.getElementById('qv-img').src = imgSrc;
        }
    });
});

// Product Filtering Logic
document.addEventListener("DOMContentLoaded", () => {
    const filterBtns = document.querySelectorAll('.filter-btn');
    if (filterBtns.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Update active state
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.getAttribute('data-filter');
                const items = document.querySelectorAll('.product-item');
                
                items.forEach(item => {
                    if (filterValue === 'all' || item.classList.contains(filterValue)) {
                        item.style.display = 'block';
                        // Re-trigger AOS animation
                        item.classList.remove('aos-animate');
                        setTimeout(() => item.classList.add('aos-animate'), 10);
                    } else {
                        item.style.display = 'none';
                        item.classList.remove('aos-animate');
                    }
                });
                
                // Refresh AOS offsets if elements moved
                if (typeof AOS !== 'undefined') {
                    setTimeout(() => AOS.refresh(), 100);
                }
            });
        });
    }
});


// Image Full Size Modal Logic
document.addEventListener("DOMContentLoaded", () => {
    // We need to attach this using event delegation since the image src changes dynamically
    document.body.addEventListener('click', (e) => {
        if (e.target && e.target.id === 'qv-img') {
            const imgSrc = e.target.src;
            if (imgSrc) {
                const fullSizeImg = document.getElementById('fullSizeImg');
                if (fullSizeImg) {
                    fullSizeImg.src = imgSrc;
                    // Close offcanvas first to prevent overlay z-index issues
                    const qvOffcanvas = document.getElementById('productQuickView');
                    const bsOffcanvas = bootstrap.Offcanvas.getInstance(qvOffcanvas);
                    if (bsOffcanvas) {
                        bsOffcanvas.hide();
                    }
                    
                    // Show modal after a tiny delay
                    setTimeout(() => {
                        const imageModalEl = document.getElementById('imageModal');
                        let bsModal = bootstrap.Modal.getInstance(imageModalEl);
                        if (!bsModal) {
                            bsModal = new bootstrap.Modal(imageModalEl);
                        }
                        bsModal.show();
                    }, 300);
                }
            }
        }
    });
    
    // Add pointer cursor to indicate it's clickable
    const style = document.createElement('style');
    style.innerHTML = '#qv-img { cursor: pointer; transition: transform 0.2s; } #qv-img:hover { transform: scale(1.02); }';
    document.head.appendChild(style);
});
