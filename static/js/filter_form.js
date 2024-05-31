document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('race_type').addEventListener('change', function() {
        document.getElementById('filterForm').submit();
    });
});