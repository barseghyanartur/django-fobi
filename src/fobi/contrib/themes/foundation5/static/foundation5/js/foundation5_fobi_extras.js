/*
    Document   : foundation5_fobi_extras.js
    Created on : July 5, 2014, 01:26:09 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `foundation5` theme-specific scripts.
*/
;

// Run the foundation scripts.
$(document).foundation();

$(document).ready(function() {
    fobiCore.init({
        // Configure?
    });
    fobiCore.handleTabs('.tabs dd');
});

/**
 * Draggable form elements.
 */
$(function() {
	// Matching regex with jQuery
	$.expr[':'].regex = function(elem, index, match) {
	    var matchParams = match[3].split(','),
	        validLabels = /^(data|css):/,
	        attr = {
	            method: matchParams[0].match(validLabels) ?
	                        matchParams[0].split(':')[0] : 'attr',
	            property: matchParams.shift().replace(validLabels,'')
	        },
	        regexFlags = 'ig',
	        regex = new RegExp(matchParams.join('').replace(/^\s+|\s+$/g,''), regexFlags);
	    return regex.test($(elem)[attr.method](attr.property));
	}

    formElementPositionElements = $('.form-element-position');
    if (formElementPositionElements.length) {
        $('.form-horizontal .row').css({ 'cursor': 'move' });

        $('.form-horizontal').sortable({
            axis: 'y',
            items: ".row",
            update: function(){
                $.each($('.form-horizontal .row'), function(i){
                    $(this).find('input:regex(name, .*-position)').val(i + 1);
                });

                $(this).find('.row').removeClass('row1').removeClass('row2');

                $(this).find('.row:odd').addClass('row2');
                $(this).find('.row:even').addClass('row1');
            }
        });
    }
});
