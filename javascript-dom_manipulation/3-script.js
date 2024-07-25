// select the element with the id red_header
const headerColorButton = document.getElementById('toggle_header');

// add clic event
headerColorButton.addEventListener('click', function() {
    // select element header
    const headerElement = document.querySelector('header');

    if (headerElement.classList.contains('red')) {
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
