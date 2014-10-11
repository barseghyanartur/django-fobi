/*
    Document   : bootstrap3_fobi_extras.js
    Created on : June 18, 2014, 01:08:12 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `bootstrap3` theme-specific scripts.
*/
;

/**
 * Replaces "-" with "_". For the rest is the jQuery-Slugify-Plugin package is used.
 * @param <string> str:
 * @return <string>
 */
  
$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });

  // Additional handler info popover
  $('.popover-link').popover({placement: 'bottom', html: true, trigger: 'hover'});

  fobiCore.init({
    // Configure?
  });

  // Choosing which tab is active on click
  fobiCore.handleTabs('.nav-tabs li');
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
        $('.form-horizontal .form-group').css({ 'cursor': 'move' });

        $('.form-horizontal').sortable({
            axis: 'y',
            items: ".form-group",
            update: function(){
                $.each($('.form-horizontal .form-group'), function(i){
                    $(this).find('input:regex(name, .*-position)').val(i + 1);
                });

                $(this).find('.form-group').removeClass('row1').removeClass('row2');

                $(this).find('.form-group:odd').addClass('row2');
                $(this).find('.form-group:even').addClass('row1');
            }
        });
    }
});
