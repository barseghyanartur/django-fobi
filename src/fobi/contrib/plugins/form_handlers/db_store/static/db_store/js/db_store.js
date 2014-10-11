/*
    Document   : fobi.plugins.form_hanlers.db_store
    Created on : Aug 2, 2014, 03:16:07 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Helper scripts for the listing view of saved form entries.
*/

;
$(document).ready(function() {
   $('.db-store-saved-form-data-entry-table td.content div, #result_list tbody tr td:nth-child(4)').each(function(e) {
        $(this).expander({
            slicePoint:       50,  // default is 100
            expandSpeed: 0,
            expandEffect: 'show',
            collapseSpeed: 0,
            collapseEffect: 'hide',
            expandPrefix:     ' ', // default is '... '
            expandText:       '[...]', // default is 'read more'
            userCollapseText: '[^]'  // default is 'read less'
        });
   });
});
