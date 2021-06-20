from odoo import models, fields, api
import logging
from odoo.http import request
_logger = logging.getLogger(__name__)

class User(models.Model):
        _inherit = "res.users"
        theme_select = fields.Selection(selection='_get_themes',string ="Select Themes")        
        def _get_themes(self):
                modules_list = self.env['ir.module.module'].search([]).filtered(lambda theme: theme.name.startswith('theme'))
                themes = []
                for theme in modules_list:
                    themes.append((theme.name,theme.shortdesc))
                _logger.info(themes)        
                return themes
                
        def go_to_website(self):
            selected_theme = self.theme_select
            _logger.info(selected_theme)
            theme_get = self.env['ir.module.module'].search([('name','=', selected_theme)])
            _logger.info(theme_get)
            return theme_get.button_choose_theme()