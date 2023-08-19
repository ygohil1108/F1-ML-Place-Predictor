window.addEventListener('DOMContentLoaded', () => {
    const driverImages = {
        "Albon": "../static/driver_images/albon.avif",
        "Alonso": "../static/driver_images/alonso.avif",
        "Bottas": "../static/driver_images/bottas.avif",
        "de Vries": "../static/driver_images/deVries.png",
        "Gasly": "../static/driver_images/gasly.avif",
        "Hamilton": "../static/driver_images/hamilton.avif",
        "Hülkenberg": "../static/driver_images/hulkenburg.avif",
        "Latifi": "../static/driver_images/latifi.png",
        "Leclerc": "../static/driver_images/leclerc.avif",
        "Magnussen": "../static/driver_images/magnussen.avif",
        "Norris": "../static/driver_images/norris.avif",
        "Ocon": "../static/driver_images/ocon.avif",
        "Pérez": "../static/driver_images/perez.avif",
        "Piastri": "../static/driver_images/Piastri.avif",
        "Ricciardo": "../static/driver_images/ricciardo.avif",
        "Russell": "../static/driver_images/russell.avif",
        "Sainz": "../static/driver_images/sainz.avif",
        "Sargeant": "../static/driver_images/sargeant.avif",
        "Schumacher": "../static/driver_images/schumacher.png",
        "Stroll": "../static/driver_images/stroll.avif",
        "Tsunoda": "../static/driver_images/tsunoda.avif",
        "Verstappen": "../static/driver_images/verstappen.avif",
        "Vettel": "../static/driver_images/Vettel.jpeg",
        "Zhou": "../static/driver_images/zhou.avif"
    };
    // Retrieve the prediction data from localStorage
    const storedPrediction = localStorage.getItem('prediction');
    const prediction = JSON.parse(storedPrediction);

    if (prediction) {
        // Update the results page elements with prediction data
        const resultsRaceYear = document.querySelector('.results_race_year');
        const driverName = document.querySelector('.driver-name');
        const statusText = document.querySelector('.status-text');

        resultsRaceYear.textContent = prediction.race_year;
        driverName.textContent = prediction.driver_name;
        statusText.textContent = prediction.status;

        const driverImageContainer = document.querySelector('.driver-image');
        const driverImage = document.createElement('img');

        if (driverImages[prediction.driver_name]) {
            driverImage.src = driverImages[prediction.driver_name];
            driverImage.alt = prediction.driver_name;
            driverImageContainer.appendChild(driverImage);
        }
    }
    // Add event listener to the "Predict New Result" button
    const homeButton = document.querySelector('.home-button');
    homeButton.addEventListener('click', () => {
        // Redirect back to the homepage (index.html)
        window.location.href = '/';
    });
});
