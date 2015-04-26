/*
    Document   : fobi.plugin.date-foundation5-widget.js
    Created on : Apr 26, 2015, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `foundation5` theme date picker plugin scripts.
*/
;

$(document).ready(function() {
    $('input[type="date"]').fdatepicker({
        format: 'yyyy-mm-dd'
    });
});
