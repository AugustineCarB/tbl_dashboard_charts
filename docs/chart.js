fetch('data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const trace = {
            x: data.timestamps,
            y: data.prices,
            type: 'scatter',
            mode: 'lines',
            name: 'BTC Price',
            line: { color: '#f7931a' } // Bitcoin orange
        };
        const layout = {
            title: 'Bitcoin Price Over Time',
            xaxis: { title: 'Date' },
            yaxis: { title: 'Price (USD)' },
            hovermode: 'closest'
        };
        Plotly.newPlot('chart', [trace], layout);
    })
    .catch(error => {
        console.error('Error loading data:', error);
        document.getElementById('chart').innerHTML = '<p>Error loading chart data.</p>';
    });
