/*
    Document   : fobi.plugin.content_markdown.js
    Created on : Dec 21, 2017, 03:30:35 AM
    Author     : Artur Barseghyan (artur.barseghyan@gmail.com)
    Description:
        Markdown plugin init scripts.
*/
;

$(document).ready(function() {
    var markdownConverter = new Remarkable();
    var markdownTextarea = $('div.markdown-widget-wrapper textarea');
    var markdownPreview = $('div.markdown-widget-wrapper .markdown-preview');

    function generateMarkdownPreview() {
        var markdownText = markdownTextarea.val();
        var markdownHtml = markdownConverter.render(markdownText);
        markdownPreview.html(markdownHtml);
    }
    markdownTextarea.bind('keyup', generateMarkdownPreview);
    generateMarkdownPreview();
});
