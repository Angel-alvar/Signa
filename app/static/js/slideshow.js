document.addEventListener('DOMContentLoaded', function() {
            const slides = document.querySelectorAll('.slide');
            const dots = document.querySelectorAll('.slide-dot');
            const prevBtn = document.querySelector('.prev-slide');
            const nextBtn = document.querySelector('.next-slide');
            let currentSlide = 0;
            let slideInterval;

            // Función para cambiar de slide
            function goToSlide(n) {
                slides[currentSlide].classList.remove('active');
                dots[currentSlide].classList.remove('active');
                currentSlide = (n + slides.length) % slides.length;
                slides[currentSlide].classList.add('active');
                dots[currentSlide].classList.add('active');
                
                // Reiniciar animaciones
                const content = slides[currentSlide].querySelector('.slide-content');
                content.classList.remove('animate__animated', 'animate__fadeInDown', 'animate__fadeInUp');
                void content.offsetWidth; // Trigger reflow
                content.querySelector('h2').classList.add('animate__animated', 'animate__fadeInDown');
                content.querySelector('p').classList.add('animate__animated', 'animate__fadeInUp', 'animate__delay-1s');
                content.querySelector('.slide-btn').classList.add('animate__animated', 'animate__fadeInUp', 'animate__delay-2s');
            }

            // Función para siguiente slide
            function nextSlide() {
                goToSlide(currentSlide + 1);
            }

            // Función para slide anterior
            function prevSlide() {
                goToSlide(currentSlide - 1);
            }

            // Event listeners para botones
            nextBtn.addEventListener('click', nextSlide);
            prevBtn.addEventListener('click', prevSlide);

            // Event listeners para dots
            dots.forEach(dot => {
                dot.addEventListener('click', function() {
                    goToSlide(parseInt(this.dataset.slide));
                });
            });

            // Autoplay
            function startSlideShow() {
                slideInterval = setInterval(nextSlide, 5000);
            }

            function pauseSlideShow() {
                clearInterval(slideInterval);
            }

            // Pausar al interactuar
            document.querySelector('.hero-slideshow').addEventListener('mouseenter', pauseSlideShow);
            document.querySelector('.hero-slideshow').addEventListener('mouseleave', startSlideShow);

            // Iniciar slideshow
            startSlideShow();

            // Keyboard navigation
            document.addEventListener('keydown', function(e) {
                if (e.key === 'ArrowLeft') {
                    prevSlide();
                } else if (e.key === 'ArrowRight') {
                    nextSlide();
                }
            });
        });