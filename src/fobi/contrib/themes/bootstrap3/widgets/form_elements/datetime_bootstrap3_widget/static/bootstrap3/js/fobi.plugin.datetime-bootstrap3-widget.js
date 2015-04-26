/*
    Document   : fobi.plugin.datetime-bootstrap3-widget.js
    Created on : Apr 26, 2015, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `bootstrap3` theme datetime picker plugin scripts.
*/
;

$(document).ready(function() {
    $('input[type="datetime"]').datetimepicker({
        format: 'YYYY-MM-DD HH:mm:ss'
    });
});
