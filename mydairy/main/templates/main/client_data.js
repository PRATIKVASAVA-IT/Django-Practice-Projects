
    // Attach event listeners to all three input fields
    const inputs = ['id_weigth', 'id_fate', 'id_price'];
    inputs.forEach(id => {
        document.getElementById(id).addEventListener('input', handleInputs);
    });

    // Function to handle the inputs and update the amount
    function handleInputs() {
        // Get the values of all three inputs
        const value1 = parseFloat(document.getElementById('id_weigth').value) || 0;
        const value2 = parseFloat(document.getElementById('id_fate').value) || 0;
        const value3 = parseFloat(document.getElementById('id_price').value) || 0;

        // Only calculate after the third input is filled
        if (document.getElementById('id_price').value) {
            // Perform the calculation
            const result = calculateAmount(value1, value2, value3);

            // Populate the amount field with the result
            document.getElementById('id_amount').value = result.toFixed(2);
        }
    }

    // Function to calculate the result based on input values
    function calculateAmount(a, b, c) {
        // Example calculation: a * b + c
        return (a * b) + c;
    }

