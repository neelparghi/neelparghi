# -*- coding: utf-8 -*-
{
    'name': "website builder ml",

    'summary': "Build and customize website",

    'description': "it gives the details of database record",
        

    'author': "tushilpawar",
    'website': "http://www.dreambits.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0',

    # any module necessary for this one to work correctly
    'depends': ['base','website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'security/website_sec.xml',
        # 'data/mldatamain.csv',
        # 'data/mldatasub.csv',
        # 'data/mldatanav.csv',
        # 'data/mldata.csv',
        'views/templates.xml',
        'views/mldata_views.xml',
        'views/data_input_views.xml',
        'views/mldata_website.xml',
        # 'views/feedback_form.xml',
        'views/res_user.xml',
        'views/custom_footer.xml'
    ], 
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'Installable': True,
 
    'auto_install': True,
}
