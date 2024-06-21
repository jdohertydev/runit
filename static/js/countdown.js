/**
 * Initializes and updates a countdown timer for an event based on a specified date.
 *
 * This script calculates the time remaining until a specified event date and updates
 * the countdown timer on the web page in real-time. It uses the 'DOMContentLoaded' event
 * to ensure all DOM elements are loaded before performing calculations and updates.
**/

document.addEventListener("DOMContentLoaded", function() {
    const eventDateElement = document.getElementById('eventDate');
    const eventDate = new Date(eventDateElement.getAttribute('data-event-date')).getTime();
    const countdownElement = document.getElementById('countdown');

    function updateCountdown() {
        const now = new Date().getTime();
        const timeLeft = eventDate - now;

        if (timeLeft < 0) {
            countdownElement.innerHTML = "Event has finished.";
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