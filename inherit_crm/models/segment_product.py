from odoo import models, fields, api

class SegmentProduct(models.Model):
    _name = 'segment.product'

    name = fields.Char(string='Nama Product')