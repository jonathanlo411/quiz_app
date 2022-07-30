
// To change the height of quiz_select so overflow is at the bottom of the page
var topDivHeight = $("#title_wrapper").height()
var totalHeight = $(document).height()
$('#quiz_select').height(totalHeight  - topDivHeight );