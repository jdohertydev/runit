var togglePasswordChangeButton = document.getElementById('toggle-password-change');
var toggleAccountDeleteButton = document.getElementById('toggle-account-delete');
var passwordSection = document.getElementById('password-change-section');
var accountDeleteSection = document.getElementById('account-delete-section');

if (togglePasswordChangeButton) {
    togglePasswordChangeButton.addEventListener('click', function() {
        if (passwordSection.style.display === 'none' || passwordSection.style.display === '') {
            passwordSection.style.display = 'block';
        } else {
            passwordSection.style.display = 'none';
        }
    });
}

if (toggleAccountDeleteButton) {
    toggleAccountDeleteButton.addEventListener('click', function() {
        if (accountDeleteSection.style.display === 'none' || accountDeleteSection.style.display === '') {
            accountDeleteSection.style.display = 'block';
        } else {
            accountDeleteSection.style.display = 'none';
        }
    });
}
