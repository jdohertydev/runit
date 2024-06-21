/**
 * Automatically submits a form when the user selects a race type from a dropdown list.
 *
 * This script listens for the 'DOMContentLoaded' event to ensure all DOM elements are loaded,
 * then attaches an event listener to the dropdown list with ID 'race_type'. When the user
 * selects a race type, the script automatically submits the form with ID 'filterForm'.
 */

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('race_type').addEventListener('change', function() {
        document.getElementById('filterForm').submit();
    });
});