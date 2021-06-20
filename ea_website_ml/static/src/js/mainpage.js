odoo.define('ea_website_ml.mainpage', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    publicWidget.registry.MainPage = publicWidget.Widget.extend({
        selector: '#footer',
        start: function () {
            $('.o_footer_copyright_name').replaceWith("Copyright@easeness.in")
            $("p").eq(17).text("CG ROAD AHMEDABAD *GUJARAT *INDIA")
            $('[href="tel:1 (650) 691-3277"]').replaceWith("9264236678")
            $('[href="mailto:info@yourcompany.example.com"]').replaceWith("easeness.in")
            $('[href="tel:1(650)691-3277"]').replaceWith("9264236678")
        }


    })
})