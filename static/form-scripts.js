document.addEventListener('DOMContentLoaded', function() {
    // Function to handle form submission
    async function handleSubmitForm(e, route, successMessageElementId, errorMessageElementId, updateListDataCallback) {
        e.preventDefault();
        const formData = new FormData(e.target);

        try {
            const response = await fetch(route, {
                method: 'POST',
                body: formData
            });

            updateListDataCallback();
            if (response.ok) {
                // Display success message
                const successMessage = await response.text();
                document.getElementById(successMessageElementId).textContent = successMessage;
            } else {
                // Display error message
                const errorMessage = await response.text();
                document.getElementById(errorMessageElementId).textContent = errorMessage;
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            document.getElementById(errorMessageElementId).textContent = 'An error occurred while submitting the form';
        }
    }

    // Add toppings form handling
    document.getElementById('add-topping-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/submit', 'add-topping-response-message', 'add-topping-response-message', updateToppingListData);
    });

    // Add pizza form handling
    document.getElementById('add-pizza-form').addEventListener('submit', function(e) {
        handleSubmitForm(e, '/submitp', 'add-pizza-response-message', 'add-pizza-response-message', updatePizzaListData);
    });

    // Add more form handling here as needed...
});
