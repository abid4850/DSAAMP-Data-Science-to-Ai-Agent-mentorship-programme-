AOS.init();

function subscribe(event) {
  event.preventDefault();
  const email = event.target.querySelector('input').value;
  if (email) {
    alert(`Subscribed with ${email}!`);
    event.target.reset();
  }
}
