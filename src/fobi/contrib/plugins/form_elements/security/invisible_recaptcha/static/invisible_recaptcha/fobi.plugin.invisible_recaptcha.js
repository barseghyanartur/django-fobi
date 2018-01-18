/*
    Document   : fobi.plugin.invisible_recaptcha.js
    Created on : January 18, 2018, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Invisible recaptcha plugin init scripts.
*/
;

function g_recaptcha_onSubmit(token) {
    console.log("g_recaptcha_onSubmit")
//    document.getElementById("fobi-form").submit();
//    document.getElementsByClassName("form-horizontal").submit();
//    $('form.form-horizontal').submit();
    $('form#fobi-form').submit();
}

$(document).ready(function() {
    var siteKey = window.InvisibleRecaptchaSiteKey || "";
    if (siteKey) {
//        var submitFormButton = $('form.form-horizontal button[type=submit]');
        var submitFormButton = $('form#fobi-form button[type=submit]');
        submitFormButton.addClass('g-recaptcha');
        submitFormButton.attr('data-sitekey', siteKey);
        submitFormButton.attr('data-callback', 'g_recaptcha_onSubmit');
        submitFormButton.removeAttr('type');
    }
});
