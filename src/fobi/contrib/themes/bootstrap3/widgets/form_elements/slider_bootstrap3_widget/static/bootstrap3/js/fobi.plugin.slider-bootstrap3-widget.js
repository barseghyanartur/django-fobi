/*
    Document   : fobi.plugin.slider-bootstrap3-widget.js
    Created on : Oct 19, 2016, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `bootstrap3` theme slider plugin scripts.
*/
;

$(document).ready(function() {
    var selectElement = $('select.slider');
    var selectedValue = null;
    try {
        selectedValue = parseInt(selectElement.val());
    } catch(err) {
        selectedValue = parseInt(selectElement.data('data-slider-value'));
    }
    var sliderElement = $('.slider').bootstrapSlider();
    sliderElement.bootstrapSlider('setValue', selectedValue);
});
