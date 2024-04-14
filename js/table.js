function createTable(data) {
    let table = '<table>';
    table += '<thead><tr><th>No</th><th>Judul</th><th>Kategori</th><th>Waktu Rilis</th><th>Waktu Scraping</th></tr></thead>';
    table += '<tbody>';
    let i = 0;
    data.forEach(item => {
      table += '<tr>';
      table += '<td>' + ++i + '</td>';
      table += '<td>' + '<a href="' + item.url + '">' + item.judul + '</a>' + '</td>';
      table += '<td>' + item.kategori + '</td>';
      table += '<td>' + item['waktu publish'] + '</td>';
      table += '<td>' + item['waktu scrape'] + '</td>';
      table += '</tr>';
    });
    table += '</tbody></table>';
    return table;
  }
  
  $(document).ready(function() {
    $.getJSON('republika_scraped_data.json', function(data) {
      console.log(data);
      const table = createTable(data);
      $('#table-container').append(table);
    })
    .fail(function(jqXHR, textStatus, errorThrown) {
      console.log('Error: ' + textStatus + ' - ' + errorThrown);
    });
  });
  