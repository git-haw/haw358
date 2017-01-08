!(function () {
    // main.js
    require.config({
        baseUrl: "/static/primary/",
        paths:{
            "jquery" : "core/js/jquery-3.1.1.min",
            "jquery-ui" : "core/js/jquery-ui",
            "underscore" : "core/js/underscore",
            "backbone" : "core/js/backbone",
            "moment" : "core/js/moment",
            "ztree" : "plugins/zTree_v3/js/jquery.ztree.core",
            "excheck" : "plugins/zTree_v3/js/jquery.ztree.excheck",
            "jquery-validate" : "plugins/form/jquery-validate",
            "parsley" : "plugins/Parsley/dist/parsley.min",
            "Highcharts" : "plugins/Highcharts/code/highcharts.src",
            "Highcharts-more" : "plugins/Highcharts/code/highcharts-more",
            "form" : "plugins/form/jquery.form",
            "layer" : "plugins/layer/layer/layer",
            "icheck" : "plugins/icheck/icheck.min",
            "progressbar" : "plugins/progressbar/bootstrap-progressbar.min",
            "nicescroll" : "plugins/nicescroll/jquery.nicescroll.min",
            "datepicker" : "plugins/bootstrap-datepicker/js/bootstrap-datepicker",
            "demo" : "customer/js/demo",
            "vue" : "https://unpkg.com/vue/dist/vue.js"
        },
        map: {
            '*': {
                'css': 'core/js/css'
            }
        },
        shim:{
            'jquery':{
                exports: 'jquery'
            },
            'underscore':{
                exports: '_'
            },
            'backbone':{
                deps: ['underscore','jquery'],
                exports: 'Backbone'
            },
            'layer' : {
                deps : [ 'jquery' , 'css!plugins/layer/skin/layer'],
                exports : 'layer'
            },
            'excheck' : {
                deps : [ 'jquery', 'ztree' ],
                exports : 'excheck'
            },
            'Highcharts' : {
                exports : 'Highcharts'
            },
            'jquery-ui' : {
                deps : [ 'jquery'],
                exports : 'jqueryui'
            },
            "datetimepicker" : {
                deps : [ 'jquery' , "css!../../plugins/bootstrap-datetimepicker/dist/css/bootstrap-datetimepicker.min"],
                exports : 'datetimepicker'
            },
            "vue" : {
                exports : 'vue'
            }
        }
    });

})();