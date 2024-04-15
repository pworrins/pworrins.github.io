$(document).ready(function(){
  $.getJSON("republika_scraped_data.json", function(data){
      $.each(data, function(index, item){
          var row = "<tr>";
          row += "<td>" + item.judul + "</td>";
          row += "<td>" + item.kategori + "</td>";
          row += "<td>" + item.waktu_publish + "</td>";
          row += "<td>" + item.waktu_scraping + "</td>";
          row += "</tr>";
          $("#jsonTable tbody").append(row);
      });
  });
});
