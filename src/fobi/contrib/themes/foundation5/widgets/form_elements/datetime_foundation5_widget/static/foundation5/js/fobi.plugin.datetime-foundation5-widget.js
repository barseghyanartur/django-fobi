/*
    Document   : fobi.plugin.datetime-foundation5-widget.js
    Created on : Apr 26, 2015, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `foundation5` datetime picker plugin scripts.
*/
;

$(document).ready(function() {
    $('input[type="datetime"]').fdatetimepicker({
        format: 'yyyy-mm-dd hh:ii:ss'
    });
});
