from odoo import models, fields
import logging
_logger = logging.getLogger(__name__)

class MlData(models.Model):
    _name = 'mldata'
    _description = 'data record'
    mlwebsite_category= fields.Integer(string="Main_category")
    mlwebsite_subcategory = fields.Integer(string="Sub_category")
    mlwebsite_navbar = fields.Integer(string = "Nav_bar")
    feedback = fields.Integer(string="Feedback")
    selected_theme = fields.Text(string ="Selected_theme")
    pos1 = fields.Text(string ="Position_1")
    pos2 = fields.Text(string ="Position_2")
    pos3 = fields.Text(string ="Position_3")
    pos4 = fields.Text(string ="Position_4")
    pos5 = fields.Text(string ="Position_5")


class Main(models.Model):
    _name = 'mldatamain'
    _description="maincat"

    name = fields.Char(string="name")
    main_id = fields.Integer(string = "main_id")

class Sub(models.Model):
    _name = 'mldatasub'
    _description="sub cat"

    name = fields.Char(string="name")
    sub_id = fields.Integer(string = "sub_id")
    main_id = fields.Integer(string = "main_id")

class Nav(models.Model):
    _name = 'mldatanav'
    _description="nav bar"
    
    name = fields.Char(string="name")
    nav_id = fields.Integer(string = "ID")
    
