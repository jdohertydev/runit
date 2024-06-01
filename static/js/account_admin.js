var togglePasswordChangeButton = document.getElementById('toggle-password-change');
var passwordSection = document.getElementById('password-change-section');

if (togglePasswordChangeButton) {
    togglePasswordChangeButton.addEventListener('click', function() {
        if (passwordSection.style.display === 'none' || passwordSection.style.display === '') {
            passwordSection.style.display = 'block';
        } else {
            passwordSection.style.display = 'none';
        }
    });
}
