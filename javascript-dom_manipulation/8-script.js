function fetchHelloTranslation() {
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  fetch(url)
    .then(response => response.json())
    .then(data => {
      const helloTranslation = data.hello;
      const helloElement = document.getElementById('hello');
      helloElement.textContent = helloTranslation;
    })
    .catch(error => console.error('Error:', error));
}
