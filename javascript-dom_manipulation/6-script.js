let character = document.querySelector('#character');
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(function(data) {
      const characterName = data.name;
      const characterElement = document.getElementById('character');
      characterElement.textContent = characterName;
    })
    .catch(error => console.error('Error:', error));
