const update_headert = document.getElementById('update_header');

update_headert.addEventListener('click', function() {
  const selectElement = document.querySelector('header');
  selectElement.textContent = 'New Header!!!';
})
