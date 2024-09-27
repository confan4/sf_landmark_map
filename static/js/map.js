document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([37.7749, -122.4194], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    fetch('/api/landmarks')
        .then(response => response.json())
        .then(landmarks => {
            landmarks.forEach(landmark => {
                const marker = L.marker(landmark.coordinates).addTo(map);
                marker.bindPopup(`<b>${landmark.name}</b>`);
                marker.on('click', () => showLandmarkInfo(landmark));
            });
        });
});

function showLandmarkInfo(landmark) {
    const infoDiv = document.getElementById('landmark-info');
    const nameElement = document.getElementById('landmark-name');
    const descriptionElement = document.getElementById('landmark-description');

    nameElement.textContent = landmark.name;
    descriptionElement.textContent = landmark.description;
    infoDiv.classList.remove('hidden');
}
