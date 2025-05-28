// Initialize AOS animations
AOS.init({
  duration: 1000,
  once: true,
});

// Newsletter subscription logic
const form = document.querySelector('form');
form.addEventListener('submit', (e) => {
  e.preventDefault();
  const email = form.querySelector('input[type="email"]').value;
  
  if (email.trim() !== '') {
    alert(`Thank you for subscribing, ${email}!`);
    form.reset();
  } else {
    alert('Please enter a valid email address.');
  }
});

// Future: Add more dynamic behavior like dark mode toggle or counters here
