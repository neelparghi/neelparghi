odoo.define('website.theme_preview_form_test', function (require) {
"use strict";

var FormController = require('web.FormController');
var FormView = require('web.FormView');
var viewRegistry = require('web.view_registry');
var core = require('web.core');
var qweb = core.qweb;

var publicWidget = require('web.public.widget');
    publicWidget.registry.FeedBackPopup = publicWidget.Widget.extend({
        selector: '.gif',
        start: function () {
            
            $(".gifbtn").click(function(event){
                this._super(...arguments);
                this.$loader = $(qweb.render('website.ThemePreview.Loader'));
                actionCallback = result => this.do_action(result);
            });
        }
        
    })
    });
        
        
            
        