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

  // Some sort of a solution for the nasty bootstrap3 problem
  // with drop-downs cut if parent container isn't long enough.
  // Thus, it's checked whether the drop-down menu height 
  // exceeds the height of the content container, the
  // {'height': 'auto', 'overflow-x', 'hidden'} css is applied to the
  // "dropdown-menu" element. Default "max-height" value of the 
  // "dropdown-menu" is then 200 (px). If content container can fit more, 
  // the css property "max-height" is changed accordingly.
  $('.dropdown-toggle').click(function() {
      var dropDownToggle = $(this);
      var dropDownParent = dropDownToggle.parents('.tab-pane');
      var dropDownMenu = dropDownParent.find('.dropdown-menu');
      if (dropDownMenu.height() > dropDownParent.height()) {
          //dropDownMenu.addClass('scrollable-menu');
          dropDownMenu.css('height', 'auto');
          dropDownMenu.css('overflow-x', 'hidden');
          var dropDownMenuMinHeiht = (dropDownParent.height() > 200) ? dropDownParent.height() : 200;
          dropDownMenu.css('max-height', dropDownMenuMinHeiht + 'px');
      }
  });
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
        $('#fobi-form .form-group').css({ 'cursor': 'move' });

        $('#fobi-form').sortable({
            axis: 'y',
            items: '.form-group',
            update: function(){
                $.each($('#fobi-form .form-group'), function(i){
                    $(this).find('input:regex(name, .*-position)').val(i + 1);
                });

                $(this).find('.form-group').removeClass('row1').removeClass('row2');

                $(this).find('.form-group:odd').addClass('row2');
                $(this).find('.form-group:even').addClass('row1');
            }
        });
    }
});
