document.addEventListener('DOMContentLoaded', () => {
    const fetchLatestSensorValues = () => {
        const spinner = document.getElementById('loading-spinner');
        spinner.style.display = 'block';
        fetch('/latest-sensor-values')
            .then(response => response.json())
            .then(data => {
                spinner.style.display = 'none';
                if (data.error) {
                    document.getElementById('temperature-status').textContent = "Error";
                    document.getElementById('humidity-status').textContent = "Error";
                    document.getElementById('light-status').textContent = "Error";
                } else {
                    document.getElementById('temperature-value').textContent = `${data.temperature}°C`;
                    document.getElementById('humidity-value').textContent = `${data.humidity}%`;
                    document.getElementById('light-value').textContent = `${data.light} lux`;
                }
            });
    };

    const fetchRecommendations = () => {
        fetch('/get-recommendations')
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    document.getElementById('recommendation-text').textContent = "Error: " + data.error;
                } else {
                    document.getElementById('recommendation-text').textContent = data.recommendation;
                }
            });
    };

    fetchLatestSensorValues();
    fetchRecommendations();
    setInterval(fetchLatestSensorValues, 30000); // Refresh sensor values every 30 seconds
    setInterval(fetchRecommendations, 300000); // Refresh recommendations every 300 seconds
});
