// select the element with the id red_header
const headerredButton = document.getElementById('red_header');

// add clic event
headerredButton.addEventListener('click', function() {
    // select element header
    const headerElement = document.querySelector('header');

    // change the color of header for read
    headerElement.classList.add('red');
});
