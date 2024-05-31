document.addEventListener("DOMContentLoaded", function() {
    const eventDateElement = document.getElementById('eventDate');
    const eventDate = new Date(eventDateElement.getAttribute('data-event-date')).getTime();
    const countdownElement = document.getElementById('countdown');

    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = eventDate - now;

        if (timeLeft < 0) {
            countdownElement.innerHTML = "Event has started!";
            return;
        }

        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
    }

    updateCountdown();
    setInterval(updateCountdown, 1000);
});