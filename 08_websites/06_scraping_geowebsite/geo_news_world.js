// Example JavaScript for Geo News World page
// You can expand this with dynamic features as needed

document.addEventListener('DOMContentLoaded', function() {
    // Highlight the current nav item (example: World)
    const navLinks = document.querySelectorAll('.nav a');
    navLinks.forEach(link => {
        if (link.textContent.trim().toLowerCase() === 'world') {
            link.style.color = '#ffb300';
            link.style.fontWeight = 'bold';
        }
    });

    // Example: Add click event to news cards
    const newsCards = document.querySelectorAll('.news-card');
    newsCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 4px 16px rgba(0,0,0,0.15)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = '0 2px 8px rgba(0,0,0,0.07)';
        });
    });
});
