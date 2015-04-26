/*
    Document   : fobi.plugin.date-bootstrap3-widget.js
    Created on : Apr 26, 2015, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `bootstrap3` theme date picker plugin scripts.
*/
;

$(document).ready(function() {
    $('input[type="date"]').datetimepicker({
        format: 'YYYY-MM-DD'
    });
});
