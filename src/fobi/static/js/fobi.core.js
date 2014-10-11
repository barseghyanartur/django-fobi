/*
    Document   : fobi.core.js
    Created on : Dec 26, 2013, 17:41:09 PM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        `django-fobi` core scripts.
*/
;
var FobiCore = function() {};
FobiCore.prototype = {
    GET: {},
     /**
     * List/array of configurable properties (to avoid accidental mistakes).
     */
    configurable: [],

    /**
     * Init the app.
     *
     * @param {Dictionary} options:
     */
    init: function(options) {
        // Configure
        this.config(options);

        // Makes the GET variables to be available in ``GET``.
        this.prepareGETVariables();
    },

    /**
     * Configure the app defaults. All default settings that are allowed to be
     * overridden are listed in ``configurable`` array. Of course,
     * this doesn't protect us from overriding the settings explicitly.
     *
     * @param {Dictionary} options:
     */
    config: function(options) {
        // Handling settings override
        if (options) {
            for (key in options) {
                if ((key in this) && (this.configurable.indexOf(key) !== -1)) {
                    this[key] = options[key];
                }
            }
        }
    },

    /**
     * Replaces "-" with "_". For the rest is the jQuery-Slugify-Plugin package is used.
     * @param {String} str:
     * @return {String}
     */
    slugify: function(str) {
        return str.replace(/[\-]+/g, '_');
    },

    /**
     * Fills the ``GET`` property with values from GET.
     *
     * @return {Array}
     */
    prepareGETVariables: function() {
        var self = this;
        var split = location.search.replace('?', '').split('&').map(function(val){
            var vars = val.split('=');
            self.GET[vars[0]] = vars[1];
        });
        return self.GET;
    },

    /**
     * Active the tab set as active in GET variable ``active_tab``.
     * Available options are: 'tab-form-elements', 'tab-form-handlers' and
     * 'tab-form-properties'.
     *
     * @param {String} activeTabSelector
     */
    handleTabs: function(activeTabSelector) {
        var activeTab = this.GET['active_tab'];
        if (activeTab) {
            $(activeTabSelector + ' a[href="#' + activeTab + '"]').trigger('click');
        } else {
            $(activeTabSelector + ' a:first').trigger('click');
        }
    }
    
};


/**
 * Replaces "-" with "_". For the rest is the jQuery-Slugify-Plugin package is used.
 * @param <string> str:
 * @return <string>
 */
//var fobiSlugify = function(str) {
//    return str.replace(/[\-]+/g, '_');
//};

var fobiCore = new FobiCore();

$(document).ready(function() {
  
  
  // Slugify form element name from label
  $('#form_element_entry_form #id_name').slugify(
    '#form_element_entry_form #id_label',
    {
        slugFunc: function(str, originalFunc) {
            return fobiCore.slugify(originalFunc(str));
        }
    }
  );
});

//window.fobiCore = fobiCore;