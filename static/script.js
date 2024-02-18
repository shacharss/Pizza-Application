// Toggle appropriate menus
document.addEventListener('DOMContentLoaded', function() {
    const toppingsOption = document.getElementById('toppings-option');
    const pizzaOption = document.getElementById('pizza-option');
    const toppingsMenu = document.getElementById('toppings-menu');
    const pizzaMenu = document.getElementById('pizza-menu');
    const pizzaList = document.getElementById('pizza-list');
    const toppingList = document.getElementById('topping-list');

    toppingsOption.addEventListener('click', function() {
        updateToppingListData();
        toppingsMenu.classList.toggle('active');
        pizzaMenu.classList.remove('active');
        toppingList.classList.toggle('active');
        pizzaList.classList.remove('active');
    });

    pizzaOption.addEventListener('click', function() {
        updatePizzaListData();
        pizzaList.classList.toggle('active');
        toppingList.classList.remove('active');
        pizzaMenu.classList.toggle('active');
        toppingsMenu.classList.remove('active');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const optionMenus = document.querySelectorAll('.options-menu');

    optionMenus.forEach(function(optionMenu) {
        optionMenu.addEventListener('click', function(event) {
            const clickedItem = event.target.closest('li');

            if (!clickedItem || !clickedItem.nextElementSibling.classList.contains('submenu')) {
                return;
            }

            const submenu = clickedItem.nextElementSibling;
            submenu.classList.toggle('active');
            clickedItem.classList.toggle('no-bottom-border');
            clickedItem.classList.toggle('background-color-grey');
        });
    });
});

//Fetch updated pizzas list
async function updatePizzaListData() {
    try {
        const response = await fetch('/get-updated-pizza-list'); 
        const data = await response.json();

        const pizzaList = document.getElementById('pizza-list');
        pizzaList.innerHTML = ''; 
        
        const pizzaHeader = document.createElement('h2');
        pizzaHeader.textContent = 'Available Pizzas';
        pizzaList.appendChild(pizzaHeader);

        const pizzaUl = document.createElement('ul');
        pizzaList.appendChild(pizzaUl);

        data.forEach(function(item) {
            const listItem = document.createElement('li');
            const nameStrong = document.createElement('strong');
            nameStrong.textContent = 'Name:';
            const nameText = document.createTextNode(` ${item.name} `);
            listItem.appendChild(nameStrong);
            listItem.appendChild(nameText);

            const toppingStrong = document.createElement('strong');
            toppingStrong.textContent = 'Toppings:';
            const toppingText = document.createTextNode(` ${item.toppings.join(', ')} `);
            listItem.appendChild(toppingStrong);
            listItem.appendChild(toppingText);
            pizzaUl.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error updating pizza list data:', error);
    }
}

//Fetch updated toppings list
async function updateToppingListData() {
    try {
        const response = await fetch('/get-updated-topping-list');
        const data = await response.json(); 

        const toppingList = document.getElementById('topping-list');
        toppingList.innerHTML = '';
        
        const toppingHeader = document.createElement('h2');
        toppingHeader.textContent = 'Available Toppings';
        toppingList.appendChild(toppingHeader);

        const toppingUl = document.createElement('ul');
        toppingList.appendChild(toppingUl);

        data.forEach(function(item) {
            const listItem = document.createElement('li');

            const nameStrong = document.createElement('strong');
            nameStrong.textContent = 'Name:';
            const nameText = document.createTextNode(` ${item.name}`);
            listItem.appendChild(nameStrong);
            listItem.appendChild(nameText);
            toppingUl.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error updating topping list data:', error);
    }
}
