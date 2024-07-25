function fetchCharacterName() {
  const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const characterName = data.name;
      const characterElement = document.getElementById('character');
      characterElement.textContent = characterName;
    })
    .catch(error => console.error('Error:', error));
}
