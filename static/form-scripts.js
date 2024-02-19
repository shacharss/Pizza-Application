document.addEventListener('DOMContentLoaded', function() {
    async function handleSubmitForm(e, route, responseMessageElementId, updateListDataCallback) {
        e.preventDefault();
        const formData = new FormData(e.target);

        try {
            const response = await fetch(route, {
                method: 'POST',
                body: formData
            });

            updateListDataCallback();
            loadToppingCheckboxes();
            if (response.ok) {
                // Display success message
                const successMessage = await response.text();
                document.getElementById(responseMessageElementId).textContent = successMessage;
            } else {
                // Display error message
                const errorMessage = await response.text();
                document.getElementById(responseMessageElementId).textContent = errorMessage;
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            document.getElementById(errorMessageElementId).textContent = 'An error occurred while submitting the form';
        }
    }

    // Add toppings form handling
    document.getElementById('add-topping-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/add-topping', 'add-topping-response-message', updateToppingListData);
    });

    // Remove toppings form handling
    document.getElementById('remove-topping-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/remove-topping', 'remove-topping-response-message', updateToppingListData);
    });

    // Update toppings form handling
    document.getElementById('update-topping-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/update-topping', 'update-topping-response-message', updateToppingListData);
    });

    // Add pizza form handling
    document.getElementById('add-pizza-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/add-pizza', 'add-pizza-response-message', updatePizzaListData);
    });

    // Remove pizza form handling
    document.getElementById('remove-pizza-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/remove-pizza', 'remove-pizza-response-message', updatePizzaListData)
    });

    // Update pizza name form handling
    document.getElementById('update-pizza-name-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/update-pizza-name', 'update-pizza-name-response-message', updatePizzaListData);
    });

    // Update pizza toppings form handling
    document.getElementById('update-pizza-toppings-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/update-pizza-toppings', 'update-pizza-toppings-response-message', updatePizzaListData);
    });
});
