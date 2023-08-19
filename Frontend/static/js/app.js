// Function to populate dropdown options
let requestData;
function populateDropdown(dropdownId, options) {
    const dropdown = document.getElementById(dropdownId);

    dropdown.innerHTML = ''; // Clear existing options

    options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option;
        optionElement.textContent = option;
        dropdown.appendChild(optionElement);
    });
}

// Function to fetch data for dropdowns
async function fetchData(url) {
    const response = await fetch(url);
    return await response.json();
}

// Populate dropdowns on page load
window.addEventListener('DOMContentLoaded', async () => {
    const data = await fetchData('/api/data');
    populateDropdown('grand-prix-dropdown', data.grandPrix);
    populateDropdown('driver-dropdown', data.drivers);
});

/* Fix */
document.getElementById('grand-prix-dropdown').addEventListener('change', async (event) => {
    const selectedGrandPrix = event.target.value;

    // Fetch the data for the selected grand prix
    const data = await fetchData('/api/data'); // Fetch all data for now, you might want to modify this endpoint
    const driverDataForGrandPrix = data.drivers.filter(driver => {
        return data.grandPrix.includes(selectedGrandPrix) && data.drivers.includes(driver);
    });

    // Populate the driver dropdown with filtered driver data
    populateDropdown('driver-dropdown', driverDataForGrandPrix);
});

// Handle form submission
    document.querySelector('.image-button').addEventListener('click', async () => {
    const grandPrixDropdown = document.getElementById('grand-prix-dropdown');
    const driverDropdown = document.getElementById('driver-dropdown');

    const grandPrixQuery = grandPrixDropdown.value;
    const driverNameQuery = driverDropdown.value;

    requestData = {
        grand_prix: grandPrixQuery,
        driver_name: driverNameQuery,
    };

    const response = await fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(requestData),
    });

    const prediction = await response.json();
    console.log(prediction)
    localStorage.setItem('prediction', JSON.stringify(prediction));

    // Redirect to results page
    window.location.href = '/results';
});
