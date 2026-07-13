document.addEventListener('DOMContentLoaded', () => {
    
    // --- Scroll Reveal Animations ---
    const revealElements = document.querySelectorAll('.reveal-up, .reveal-left, .reveal-right');
    
    const revealOptions = {
        threshold: 0.15,
        rootMargin: "0px 0px -50px 0px"
    };
    
    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);
    
    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });

    // --- Header Scroll Effect ---
    const navPill = document.querySelector('.nav-pill');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navPill.classList.add('scrolled');
        } else {
            navPill.classList.remove('scrolled');
        }
    });

    // --- Parallax Effect on Hero Cards ---
    const parallaxElements = document.querySelectorAll('.parallax-el');
    
    window.addEventListener('mousemove', (e) => {
        const x = (window.innerWidth - e.pageX * 2) / 100;
        const y = (window.innerHeight - e.pageY * 2) / 100;

        parallaxElements.forEach(el => {
            const speed = el.getAttribute('data-speed') || 1;
            el.style.transform = `translate(${x * speed}px, ${y * speed}px)`;
        });
    });
});
