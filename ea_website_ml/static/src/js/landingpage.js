odoo.define('ea_website_ml.landing_page', function (require) {
    "use strict";

    var publicWidget = require('web.public.widget');
    publicWidget.registry.HelloWorldPopup = publicWidget.Widget.extend({
        selector: '.mldata',
        events: {   
            'change select[name="mlwebsite_category"]': '_ChangeMain',
        },
    
        start: function () {
            $('.step-1,.step-2,.step-3').click(function(event){
                var self = $(this);
                var val = $(this).find("i").length
                $("i").removeClass("bg-info");
                
                var step_class = this.classList[this.classList.length-1];

                if(val > 0){
                    $(this).find("i").addClass('bg-info');
                }
                else{
                    var process_class = ".s_process_step"
                    process_class += "."+step_class;
                    var i_selector = process_class+" i";
                    $(i_selector).addClass('bg-info');

                }

                if (step_class != "step-1" && step_class != "step-2" && step_class != "step-3" )
                {
                    var sub_class = ['step-1','step-2','step-3'];
                    $.each(sub_class,function(index, item){
                        if(self.hasClass(item))
                        {
                            step_class = item;
                        }
                    });
                    var process_class = ".s_process_step"
                    process_class += "."+step_class;
                    var i_selector = process_class+" i";
                    $(i_selector).addClass('bg-info');
                }                


                var step_number = step_class.replace("step-","");
                var new_container_number = ".container_content-"+step_number;
                $(".container_content").hide();
                $(new_container_number).show();
                // $('a').click(function(){
                //     $(this).scrollTop(0)
                // })
                $("a").click(function() {
                    $('html, body').animate({
                        scrollTop: $("#Row").offset().top
                    }, 200);
                });
            
                
 
                $("#add_feature").change(function() {
                    $(this).find('input[type=checkbox]:not(:checked)').prop('checked', true).val(0);
                })
                


                event.preventDefault();
               
            });
          
            
            $('.s_process_step.step-1').click();
            
        },
        /**
        * @private
        * @param {Event} ev
        */
        _ChangeMain: function (ev) {
            this._rpc({
                route: "/builder/getSubCategory/" + $("#mlwebsite_category").val(),    
        }).then(function (data) {
            console.log(data['sub_category'])
            console.log(jQuery.type(data['sub_category']))

            var a = data['sub_category']
            $('#mlwebsite_subcategory').html("");
            $('#mlwebsite_subcategory').one('click',(function () { 
                
                for (var i = 0; i<a.length;i++){
                    
                    $('#mlwebsite_subcategory').append("<option value='"+a[i][1]+"'> "+a[i][0]+"</option>");
                }       
                
            
                        
            }))
            
            
        });
    }
    });
});