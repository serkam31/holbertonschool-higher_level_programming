const list = document.querySelector('#list_movies')
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json()
    })
    .then(function(data) {
        data.results.forEach(function(film) {
            const li = document.createElement('li')
            li.textContent = film.title
            list.appendChild(li)
        })
    })