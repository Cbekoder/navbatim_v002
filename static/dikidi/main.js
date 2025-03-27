// Main JavaScript file for DIKIDI booking platform

document.addEventListener('DOMContentLoaded', function() {
    // Handle favorite toggle
    const favoriteButtons = document.querySelectorAll('.favorite-toggle');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function() {
            this.classList.toggle('text-red-500');
            this.classList.toggle('text-gray-300');
        });
    });

    // Handle search functionality
    const searchInput = document.querySelector('input[placeholder="Service, company or specialist"]');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                // You can implement search functionality here
                console.log('Searching for:', this.value);
                // In a real app, you would send this to your Django backend
            }
        });
    }

    // Handle category selection
    const categoryItems = document.querySelectorAll('.category-item');
    categoryItems.forEach(item => {
        item.addEventListener('click', function() {
            // You can implement category selection here
            const categoryName = this.querySelector('.category-name').textContent.trim();
            console.log('Selected category:', categoryName);
            // In a real app, you would send this to your Django backend
        });
    });

    // Handle booking button clicks
    const bookButtons = document.querySelectorAll('button:contains("Book Now")');
    bookButtons.forEach(button => {
        button.addEventListener('click', function() {
            const serviceCard = this.closest('.service-card');
            const serviceName = serviceCard.querySelector('h3').textContent;
            console.log('Booking service:', serviceName);
            // In a real app, you would redirect to a booking page or open a modal
        });
    });
});