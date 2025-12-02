// LLMNetOps - Animations JavaScript

// Fade in on scroll animation
function initScrollReveal() {
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        revealElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('revealed');
            }
        });
    };
    
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll(); // Check on initial load
}

// Staggered animation for card grids
function initStaggerAnimation() {
    const grids = document.querySelectorAll('.card-grid, .features-grid');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const cards = entry.target.querySelectorAll('.card, .feature-card');
                cards.forEach((card, index) => {
                    card.style.animationDelay = `${index * 0.1}s`;
                    card.classList.add('animate-in');
                });
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    grids.forEach(grid => observer.observe(grid));
}

// Parallax effect for hero section
function initParallax() {
    const hero = document.querySelector('.hero');
    
    if (!hero) return;
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        hero.style.backgroundPositionY = `${scrolled * 0.5}px`;
    });
}

// Typing effect for hero text
function typeWriter(element, text, speed = 50) {
    let i = 0;
    element.textContent = '';
    
    function type() {
        if (i < text.length) {
            element.textContent += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Number counting animation
function countUp(element, target, duration = 2000) {
    const start = 0;
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function
        const easeOutQuad = progress * (2 - progress);
        
        const current = Math.floor(easeOutQuad * target);
        element.textContent = current.toLocaleString();
        
        if (progress < 1) {
            requestAnimationFrame(update);
        } else {
            element.textContent = target.toLocaleString();
        }
    }
    
    requestAnimationFrame(update);
}

// Initialize stats counter when visible
function initStatsCounter() {
    const statNumbers = document.querySelectorAll('.stat-number[data-target]');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.dataset.target);
                countUp(entry.target, target);
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    statNumbers.forEach(stat => observer.observe(stat));
}

// Progress bar animation
function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const targetWidth = entry.target.dataset.progress || '0';
                entry.target.style.width = targetWidth + '%';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    progressBars.forEach(bar => {
        bar.style.width = '0%';
        observer.observe(bar);
    });
}

// Accordion animation
function initAccordion() {
    const accordionItems = document.querySelectorAll('.deliverable-card, .faq-item');
    
    accordionItems.forEach(item => {
        const header = item.querySelector('.deliverable-header, .faq-question');
        const content = item.querySelector('.deliverable-content, .faq-answer');
        
        if (header && content) {
            header.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                
                // Close all other items
                accordionItems.forEach(otherItem => {
                    if (otherItem !== item) {
                        otherItem.classList.remove('active');
                        const otherContent = otherItem.querySelector('.deliverable-content, .faq-answer');
                        if (otherContent) {
                            otherContent.style.maxHeight = null;
                        }
                    }
                });
                
                // Toggle current item
                item.classList.toggle('active');
                
                if (!isActive) {
                    content.style.maxHeight = content.scrollHeight + 'px';
                } else {
                    content.style.maxHeight = null;
                }
            });
        }
    });
}

// Smooth scroll with offset for fixed header
function smoothScrollTo(targetId) {
    const target = document.querySelector(targetId);
    if (target) {
        const navHeight = document.querySelector('nav').offsetHeight;
        const targetPosition = target.offsetTop - navHeight - 20;
        
        window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
        });
    }
}

// Initialize all animations
function initAnimations() {
    initScrollReveal();
    initStaggerAnimation();
    initStatsCounter();
    animateProgressBars();
    initAccordion();
}

// Run when DOM is loaded
document.addEventListener('DOMContentLoaded', initAnimations);

// Export for module use
window.Animations = {
    typeWriter,
    countUp,
    smoothScrollTo,
    initAccordion
};
