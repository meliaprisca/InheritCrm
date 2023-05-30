from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_pelanggan_baru = fields.Boolean(string='Pelanggan Baru ?')
    segment_pelanggan = fields.Selection([
        ('konstruksi','Konstruksi'),
        ('perbankan','Perbankan'),
        ('pemerintah','Pemerintah'),
        ('bum','BUMD/BUMN'),
        ('kementrian','Kementrian'),
        ('swasta','Swasta'),
        ('lainnya','Lainnya'),
        ], string='Segment Pelanggan')
    segment_product = fields.Many2one('segment.product', string='Segment Product')
    task_ids = fields.One2many('task.progress', 'lead_id', string='Task Progress Ids')
