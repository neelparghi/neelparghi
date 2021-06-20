from odoo import http
from odoo.http import request
import logging
import random
import wdb
from ..models.lib.ml_base import Connection
from ..models.lib.building_block_ml_model_base import Buildingblocks
_logger = logging.getLogger(__name__)


class Builder(http.Controller):

    @http.route('/builder/register', auth='user', type='http', website=True)
    def data_details(self, **kwargs):

        data = request.env['mldata'].search([])
        main = request.env['mldatamain'].search([])
        sub = request.env['mldatasub'].search([])
        nav = request.env['mldatanav'].search([])

        _logger.info(main.mapped('main_id'))
        _logger.info(type(main.mapped('main_id')))
        _logger.info(sub.mapped('sub_id'))
        _logger.info(sub.mapped('main_id'))

        values = {
            'data': data,
            'main': main,
            'sub': sub,
            'nav': nav,
        }

        return request.render('ea_website_ml.data_details', values)

    @http.route('/builder/register/process', auth='user', type='http', website=True)
    def processed_data(self,**kwargs):       
        _logger.info(kwargs)
        obj = Connection()
        browse_res = request.env['mldata'].search([])
        _logger.info(browse_res)
        # wdb.set_trace()
        
        ml_data = []
        block_data = []
        for record in browse_res:
            ml_data.append((record.mlwebsite_category, record.mlwebsite_subcategory, record.mlwebsite_navbar, record.selected_theme))

            block_data.append((record.mlwebsite_subcategory, record.pos1, record.pos2, record.pos3, record.pos4, record.pos5))

        obj.setMlData(ml_data)
        inp = obj.predict_theme(kwargs['mlwebsite_category'], kwargs['mlwebsite_subcategory'], kwargs['mlwebsite_navbar'])

        _logger.info(inp)
        
        res = "".join(inp).lower()

        _logger.info(res)

        theme_get = request.env['ir.module.module'].sudo().search([('name', '=', "theme_" + res)])

        _logger.info(theme_get)

        # wdb.set_trace()   
    
        # Take this to new controller
        theme_get.sudo().button_choose_theme()
        #  
        website_default = request.env['website'].sudo().search([], limit=1)
        request.env['website'].sudo()._force_website(website_default)

        if 'add_feature1' in kwargs or kwargs['mlwebsite_subcategory'] == '12':
            if kwargs['mlwebsite_subcategory'] == '12' or kwargs['add_feature1'] == "on":
                getModule = request.env['ir.module.module']
                getModule.update_list()
                moduleIds = getModule.search(
                    [
                        ('state', '!=', 'installed'),
                        ('name', '=', 'website_blog')
                    ]
                )
                if moduleIds:
                    moduleIds[0].button_immediate_install()
        if kwargs['mlwebsite_subcategory'] == '30':
            getModule1 = request.env['ir.module.module']
            getModule1.update_list()
            moduleIds1 = getModule1.search(
                [
                    ('state', '!=', 'installed'),
                    ('name', '=', 'crm')
                ]
            )
            if moduleIds1:
                moduleIds1[0].button_immediate_install()

        if 'add_feature2' in kwargs or kwargs['mlwebsite_subcategory'] == '31':
            if kwargs['mlwebsite_subcategory'] == '31' or kwargs['add_feature2'] == "on":
                getModule2 = request.env['ir.module.module']
                getModule2.update_list()
                moduleIds2 = getModule2.search(
                    [
                        ('state', '!=', 'installed'),
                        ('name', '=', 'website_sale')
                    ]
                )
                if moduleIds2:
                    moduleIds2[0].button_immediate_install()

        if 'add_feature3' in kwargs:
            if kwargs['add_feature3'] == "on":
                getModule3 = request.env['ir.module.module']
                getModule3.update_list()
                moduleIds3 = getModule3.search(
                    [
                        ('state', '!=', 'installed'),
                        ('name', '=', 'im_livechat')
                    ]
                )
                if moduleIds3:
                    moduleIds3[0].button_immediate_install()

        # new ml model starts here
        obj2 = Buildingblocks()
        obj2.setMlDatasub_category(block_data)
        blocks_pos1 = obj2.predict_blocks(kwargs['mlwebsite_subcategory'])

        block_ps = list(blocks_pos1)
        _logger.info(blocks_pos1)
        _logger.info(block_ps)
        block_part1 = random.choice(blocks_pos1[0])
        block_part2 = random.choice(blocks_pos1[1])
        block_part3 = random.choice(blocks_pos1[2])
        block_part4 = random.choice(blocks_pos1[3])
        block_part5 = random.choice(blocks_pos1[4])
        block_part1 = block_part1.split(',')
        block_part2 = block_part2.split(',')
        block_part3 = block_part3.split(',')
        block_part4 = block_part4.split(',')
        block_part5 = block_part5.split(',')
        
        blocks = []
        
        block1 = random.choice(block_part1)
        blocks.append("website.s_" + block1.lower())
        block2 = random.choice(block_part2)
        blocks.append("website.s_" + block2.lower())
        block3 = random.choice(block_part3)
        blocks.append("website.s_" + block3.lower())
        block4 = random.choice(block_part4)
        blocks.append("website.s_" + block4.lower())
        block5 = random.choice(block_part5)
        blocks.append("website.s_" + block5.lower())
        blocks = blocks[::-1]
        
        snippet_string = ""
        for i in blocks:
            snippet_arch = request.env.ref('' + i + '').arch_base
            
            first_section = snippet_arch.find('<section')
            last_section = snippet_arch.rfind('</section')
            snippet_sub = snippet_arch[first_section:last_section + 10]
            
            snippet_string = snippet_sub + snippet_string
            
        IDS = website_default.homepage_id.view_id.id
        website_default.homepage_id.view_id.save("""
            
        <div id="wrap" class="oe_structure oe_empty" data-oe-model="ir.ui.view" data-oe-id=""" + str(IDS) + """ data-oe-field="arch" data-oe-xpath="/t[1]/t[1]/div[1]" data-editor-message="DRAG BUILDING BLOCKS HERE" data-note-id="1">
        """ + snippet_string + """
        <div id="drag" class="o_wevent_index"/>
        </div>
        """, "/t[1]/t[1]/div[1]")

        request.env.ref('base.main_company').write({
            'name': kwargs['bname'],
            'email' : kwargs['email'],
            'street': kwargs['address'],
            'phone' : kwargs['contact']
        })

        # taking inputs and storing in record
        theme_name = " ".join(inp).upper()
        user_selected_input = [
            {'mlwebsite_category': kwargs['mlwebsite_category'], 'mlwebsite_subcategory': kwargs['mlwebsite_subcategory'], 'mlwebsite_navbar': kwargs['mlwebsite_navbar'],
             'selected_theme': theme_name, 'pos1': block1, 'pos2': block2, 'pos3': block3, 'pos4': block4,
             'pos5': block5}]
        request.env['mldata'].create(user_selected_input)
        return request.redirect('/')

    @http.route(['/builder/getSubCategory/<int:mlwebsite_category>'], type='json', auth="public", methods=['POST'], website=True)
    def sub_number(self, **kwargs):
        _logger.info(kwargs)
        _logger.info(kwargs['mlwebsite_category'])
        sub = request.env['mldatasub'].search([('main_id', '=', kwargs['mlwebsite_category'])])

        sub_category = []
        for record in sub:
            sub_category.append((record.name, record.sub_id))

        _logger.info(sub_category)
        _logger.info(type(sub_category))

        return {'sub_category': sub_category}