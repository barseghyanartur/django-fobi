;
$(document).ready(function(){
    // Menu toggling
    $(".dropdown .dropdown-menu").hide();
    $(".dropdown .dropdown-toggle").click(function(){
        var parent = $(this).parent('li').parent('ul');
        parent.find(".dropdown .dropdown-menu").toggle();
    });

    // Handling tabs
    $("#tabs").tabs({heightStyle: "auto"});

    fobiCore.init({
        // Configure?
    });
    fobiCore.handleTabs('#tabs ul.tab-links li');
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
        $('.form-horizontal .form-row').css({ 'cursor': 'move' });

        $('.form-horizontal').sortable({
            axis: 'y',
            items: ".form-row",
            update: function(){
                $.each($('.form-horizontal .form-row'), function(i){
                    $(this).find('input:regex(name, .*-position)').val(i + 1);
                });

                //$(this).find('.form-row').removeClass('row1').removeClass('row2');

                //$(this).find('.form-row:odd').addClass('row2');
                //$(this).find('.form-row:even').addClass('row1');
            }
        });
    }
});
