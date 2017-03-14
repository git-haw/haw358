/**
 * Created by Administrator on 2017-1-10.
 */
define(['jquery', 'summernote'], function ($, summernote) {
    $(function () {
        $('#summernote').summernote({
            height: 800,                 // set editor height
            minHeight: null,             // set minimum height of editor
            maxHeight: null,             // set maximum height of editor
            focus: true                  // set focus to editable area after initializing summernote
        });
    });

});