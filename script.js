$(document).ready(function(){
    $('#dateRangePicker').daterangepicker({
        opens: 'left', // Adjust the calendar's position
        locale: {
            format: 'YYYY-MM-DD'
        }
    }, function(start, end, label) {
        // Handle the selected date range, if needed
        console.log("Selected date range: " + start.format('YYYY-MM-DD') + ' to ' + end.format('YYYY-MM-DD'));
    });
});
