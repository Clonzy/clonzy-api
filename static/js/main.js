// static/js/main.js

function fetchData() {
  fetch('/api/data')
    .then(response => response.json())
    .then(data => {
      const tableBody = document.getElementById('token-table-body');
      let rows = '';
      data.forEach(record => {
        rows += `
          <tr>
            <td class="py-2 px-4 border">${record.id}</td>
            <td class="py-2 px-4 border">${record.name}</td>
            <td class="py-2 px-4 border">${record.symbol}</td>
            <td class="py-2 px-4 border">${record.volume}</td>
            <td class="py-2 px-4 border">${record.holders_count}</td>
            <td class="py-2 px-4 border">${record.cur_liq_usd}</td>
          </tr>
        `;
      });
      tableBody.innerHTML = rows;
    })
    .catch(error => console.error('Error fetching data:', error));
}

// Initial fetch and subsequent update every 10 seconds
fetchData();
setInterval(fetchData, 10000);
