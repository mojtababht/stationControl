$(document).ready(function () {
  
  
  $("select").chosen({
    no_results_text: "Oops, nothing found!",
    disable_search_threshold: 10
  });
  
  $('#id_piece_chosen').css('width', '10rem');
  $('.chosen-search-input').css('width', '8rem');
  // $("#id_station").chosen({
  //   no_results_text: "Oops, nothing found!"
  // });
  




  $("#id_date").pDatepicker({
    initialValueType: 'persian',
    format: 'YYYY-MM-DD',
    calendar:{
      persian:{
        locale:'en'
      }
    }
    
  });


});
