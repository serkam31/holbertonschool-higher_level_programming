document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(function(response) {
            return response.json()
        })
        .then(function(displays) {
            const hello = document.querySelector('#hello')
            hello.textContent = displays.hello
        })
})