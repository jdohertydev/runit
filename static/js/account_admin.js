
/**
 * Initialize event listeners for toggling sections on DOMContentLoaded.
 * 
 * This script listens for the DOMContentLoaded event to ensure the DOM elements
 * are fully loaded and then sets up event listeners for toggling visibility
 * of 'Update Account' and 'Change Password' sections.
 */

document.addEventListener("DOMContentLoaded", function() {
    // Toggle Update Account section
    const toggleAccountButton = document.getElementById("toggle-account-update");
    const accountUpdateSection = document.getElementById("account-update-section");

    toggleAccountButton.addEventListener("click", function() {
        if (accountUpdateSection.style.display === "none" || accountUpdateSection.style.display === "") {
            accountUpdateSection.style.display = "block";
        } else {
            accountUpdateSection.style.display = "none";
        }
    });

    // Toggle Change Password section
    const togglePasswordButton = document.getElementById("toggle-password-change");
    const passwordChangeSection = document.getElementById("password-change-section");

    togglePasswordButton.addEventListener("click", function() {
        if (passwordChangeSection.style.display === "none" || passwordChangeSection.style.display === "") {
            passwordChangeSection.style.display = "block";
        } else {
            passwordChangeSection.style.display = "none";
        }
    });
});
