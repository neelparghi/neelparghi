odoo.define('ea_website_ml.feedback', function (require) {
    'use strict';
    
    var publicWidget = require('web.public.widget');
    publicWidget.registry.FeedBackPopup = publicWidget.Widget.extend({
        selector: '.feedbackform',
        start: function () {
            $(".ps-4").hide();
            $('.ps-3').click(function(event){
                $(".ps-1").hide();
                $(".ps-4").show();
            });
            $(".ps-2").click(function(event){
                $(".feedbackform").hide();
            });
        }
        
    })
    });
    