const my_list = document.querySelector('.my_list')
const item = document.querySelector('#add_item')
item.addEventListener('click', function() {
    const li = document.createElement('li')
    li.textContent = 'Item'
    my_list.appendChild(li)
})