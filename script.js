var map = L.map("map").setView([54.526, -2.255], 5);

L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Fetch GeoJSON data from the backend server
geoJson = fetch("/geojson").then((response) => response.json());

// The data will contain data for 180 countries so iterate over them and
// Create a GeoJSON layer with the fetched data for each of the cpuntries
// // Fetch GeoJSON data from your backend
fetch('url_to_your_geojson_endpoint')
  .then(response => response.json())
  .then(data => {
    // Create a GeoJSON layer with styling function
    L.geoJSON(data, {
      style: function(feature) {
        return {
          fillColor: 'green',  // Example fill color
          weight: 1,
          opacity: 1,
          color: 'white',
          dashArray: '3',
          fillOpacity: 0.7
        };
      },
      onEachFeature: function(feature, layer) {
        // Bind popup or other interactions if needed
        layer.bindPopup('<b>' + feature.properties.name + '</b><br>' + 'Some additional info');
      }
    }).addTo(map);
  })
  .catch(error => {
    console.error('Error fetching GeoJSON:', error);
  });
