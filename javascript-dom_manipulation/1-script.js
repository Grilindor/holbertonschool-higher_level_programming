// select the element with the id red_header
const headerredbutton = document.getElementById('red_header');

// add clic event
headerredbutton.addEventListener('clic', function() {
  // select element header
  const header = document.querySelector('header');

  // change the color of header for read
  header.style.color = '#FF0000';
});
