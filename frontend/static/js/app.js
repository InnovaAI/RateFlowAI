document.addEventListener('DOMContentLoaded', function() {
    // Fetch prediction data from API
    fetch('/api/predict/USD/TZS/')
        .then(response => response.json())
        .then(data => {
            const forecast = data.forecast;
            const dates = generateNext7Days();  // Helper function
            
            // Render Chart.js
            const ctx = document.getElementById('forecastChart').getContext('2d');
            new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dates,
                    datasets: [{
                        label: 'USD to TSH Forecast',
                        data: forecast,
                        borderColor: '#4e73df',
                        tension: 0.4
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { display: true },
                        title: { 
                            display: true,
                            text: '7-Day Exchange Rate Forecast'
                        }
                    }
                }
            });
        });
});

// Helper: Generate next 7 days as labels (e.g., "Oct 5")
function generateNext7Days() {
    const days = [];
    const date = new Date();
    for (let i = 0; i < 7; i++) {
        date.setDate(date.getDate() + 1);
        days.push(date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }));
    }
    return days;
}