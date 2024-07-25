// Select the element with the id red_header
const redHeaderButton = document.getElementById('red_header');

// Add click event
redHeaderButton.addEventListener('click', function() {
    // Select element header
    const headerItem = document.querySelector('header');

    // Change the color of header to red
    headerItem.style.color = '#FF0000';
});
