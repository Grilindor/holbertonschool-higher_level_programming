// select the element with the id add_item
const addElement = document.getElementById('add_item');

// add clic event
addElement.addEventListener('click', function() {
  // select ul with class my_list
  const selectElement = document.querySelector('ul.my_list');
  // create a new li
  const newItem = document.createElement('li')
  // set the content of the new li
  newItem.textContent = 'Item';
  // append the new li in the ul
  selectElement.appendChild(newItem);
});
