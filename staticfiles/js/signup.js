/**
 * Handles race sign-up and unregistration functionality.
 *
 * This script listens for the 'DOMContentLoaded' event to ensure all DOM elements are loaded,
 * then attaches event listeners to the sign-up and unregistration buttons. When a user clicks
 * one of these buttons, a modal is displayed, and upon confirmation, the respective action is
 * performed by submitting a form with the appropriate data.
 *
 * The script utilizes Bootstrap's modal for user confirmation and dynamically creates a form
 * to handle the sign-up and unregistration actions securely using a CSRF token.
 */

document.addEventListener("DOMContentLoaded", () => {
    const signupModal = new bootstrap.Modal(document.getElementById("signupModal"));
    const signupConfirm = document.getElementById("signupConfirm");
    const actionType = document.getElementById("actionType");

    document.getElementById("signupButton")?.addEventListener("click", () => {
        actionType.innerText = "sign up";
        signupConfirm.setAttribute("data-action", "signup");
        signupModal.show();
    });

    document.getElementById("unregisterButton")?.addEventListener("click", () => { // Change to "unregisterButton"
        actionType.innerText = "unregister";
        signupConfirm.setAttribute("data-action", "unregister");
        signupModal.show();
    });

    signupConfirm.addEventListener("click", () => {
        const action = signupConfirm.getAttribute("data-action");
        const form = document.createElement("form");
        form.method = "post";
        form.style.display = "none";
        const csrfToken = document.querySelector("input[name='csrfmiddlewaretoken']").value;
        form.innerHTML = `
            <input type="hidden" name="csrfmiddlewaretoken" value="${csrfToken}">
            <input type="hidden" name="${action}" value="1">
        `;
        document.body.appendChild(form);
        form.submit();
    });
});
