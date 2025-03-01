document.addEventListener("DOMContentLoaded", () => {
    // Typing Effect
    const roleText = ["Full Stack Developer", "Software Engineer", "Tech Enthusiast"];
    let index = 0;
    let charIndex = 0;
    const roleElement = document.querySelector(".role");

    function typeEffect() {
        if (charIndex < roleText[index].length) {
            roleElement.textContent += roleText[index].charAt(charIndex);
            charIndex++;
            setTimeout(typeEffect, 100);
        } else {
            setTimeout(eraseEffect, 2000);
        }
    }

    function eraseEffect() {
        if (charIndex > 0) {
            roleElement.textContent = roleText[index].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(eraseEffect, 50);
        } else {
            index = (index + 1) % roleText.length;
            setTimeout(typeEffect, 500);
        }
    }

    typeEffect();

    // Dark Mode Toggle
    const darkModeToggle = document.querySelector("#dark-mode");
    darkModeToggle.addEventListener("change", () => {
        document.body.classList.toggle("dark-mode");
    });

    // Ensure all .edu-card elements have the same height
    function equalizeCardHeights() {
        const cards = document.querySelectorAll(".edu-card");
        let maxHeight = 0;

        cards.forEach(card => {
            card.style.height = "auto"; // Reset height to get natural height
            maxHeight = Math.max(maxHeight, card.clientHeight);
        });

        cards.forEach(card => {
            card.style.height = maxHeight + "px"; // Apply max height
        });
    }

    // Run height adjustment after DOM loads
    equalizeCardHeights();

    // Run again on window resize to handle responsiveness
    window.addEventListener("resize", equalizeCardHeights);

    // Active Link Highlighting
    const navLinks = document.querySelectorAll("nav a");
    navLinks.forEach(link => {
        link.addEventListener("click", function () {
            navLinks.forEach(nav => nav.classList.remove("active"));
            this.classList.add("active");
        });
    });

    // Scroll Reveal Animation
    function revealElements() {
        const revealItems = document.querySelectorAll(".reveal");

        revealItems.forEach(item => {
            const windowHeight = window.innerHeight;
            const elementTop = item.getBoundingClientRect().top;
            const revealPoint = 100; // Adjust as needed

            if (elementTop < windowHeight - revealPoint) {
                item.classList.add("active");
            } else {
                item.classList.remove("active");
            }
        });
    }

    window.addEventListener("scroll", revealElements);
    revealElements(); // Trigger on load
});
