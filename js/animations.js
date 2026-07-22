/**
 * Animations and Third-Party Plugins Initialization
 */

document.addEventListener("DOMContentLoaded", () => {
  
  // 1. Initialize AOS (Animate On Scroll)
  if (typeof AOS !== 'undefined') {
    AOS.init({
      duration: 800,
      easing: 'ease-in-out',
      once: true,
      mirror: false,
      offset: 50
    });
  }

  // 2. Initialize Vanilla Tilt (for premium cards)
  if (typeof VanillaTilt !== 'undefined') {
    VanillaTilt.init(document.querySelectorAll(".tilt-card"), {
      max: 5,
      speed: 400,
      glare: true,
      "max-glare": 0.1,
      scale: 1.02
    });
  }

  // 3. Initialize CountUp
  const countElements = document.querySelectorAll('.counter-val');
  if (countElements.length > 0 && typeof countUp !== 'undefined') {
    const options = {
      duration: 2.5,
      separator: ','
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const target = entry.target;
          const endVal = parseInt(target.getAttribute('data-count'), 10);
          
          if (!target.classList.contains('counted')) {
            let numAnim = new countUp.CountUp(target, endVal, options);
            if (!numAnim.error) {
              numAnim.start();
            } else {
              console.error(numAnim.error);
            }
            target.classList.add('counted');
          }
        }
      });
    }, { threshold: 0.5 });

    countElements.forEach(el => observer.observe(el));
  }

  // 4. Initialize GSAP Reveal Animations
  if (typeof gsap !== 'undefined') {
    // Register ScrollTrigger if available
    if (typeof ScrollTrigger !== 'undefined') {
      gsap.registerPlugin(ScrollTrigger);
    }

    // Hero Stagger Animation
    const heroElements = document.querySelectorAll('.hero-anim');
    if (heroElements.length > 0) {
      gsap.fromTo(heroElements, 
        { y: 50, opacity: 0 }, 
        { y: 0, opacity: 1, duration: 1, stagger: 0.2, ease: "power3.out", delay: 0.5 }
      );
    }

    // Image Reveal wrapper
    const reveals = document.querySelectorAll('.reveal-wrapper');
    reveals.forEach(reveal => {
      let overlay = reveal.querySelector('.reveal-overlay');
      let img = reveal.querySelector('img');
      
      if(overlay && img && typeof ScrollTrigger !== 'undefined') {
        let tl = gsap.timeline({
          scrollTrigger: {
            trigger: reveal,
            start: "top 80%",
          }
        });
        
        tl.to(overlay, { duration: 1, scaleY: 0, transformOrigin: "top", ease: "power3.inOut" })
          .fromTo(img, { scale: 1.2 }, { scale: 1, duration: 1, ease: "power3.out" }, "-=0.5");
      }
    });
  }

  // 5. Initialize Swiper.js (Carousels)
  if (typeof Swiper !== 'undefined') {
    // Category Slider
    const categorySwiper = new Swiper('.category-swiper', {
      slidesPerView: 1,
      spaceBetween: 20,
      loop: true,
      autoplay: {
        delay: 3000,
        disableOnInteraction: false,
      },
      breakpoints: {
        576: { slidesPerView: 2 },
        768: { slidesPerView: 3 },
        992: { slidesPerView: 4 }
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      }
    });

    // Product Gallery Slider (Product Detail Page)
    const productThumbSwiper = new Swiper('.product-thumb-swiper', {
      spaceBetween: 10,
      slidesPerView: 4,
      freeMode: true,
      watchSlidesProgress: true,
    });
    const productMainSwiper = new Swiper('.product-main-swiper', {
      spaceBetween: 10,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      thumbs: {
        swiper: productThumbSwiper,
      },
    });
  }

  // 6. Initialize GLightbox
  if (typeof GLightbox !== 'undefined') {
    const lightbox = GLightbox({
      touchNavigation: true,
      loop: true,
      autoplayVideos: true
    });
  }

  // 7. Refresh ScrollTrigger when images load
  window.addEventListener('load', () => {
    if (typeof ScrollTrigger !== 'undefined') {
      ScrollTrigger.refresh();
    }
  });

});
