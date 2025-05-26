document.getElementById('apiBtn').addEventListener('click', function() {
    fetch('/api')
        .then(response => response.json())
        .then(data => {
            const responseDiv = document.getElementById('apiResponse');
            responseDiv.style.display = 'block';
            responseDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        })
        .catch(error => {
            console.error('Error:', error);
        });
});