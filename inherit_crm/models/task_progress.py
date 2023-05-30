from odoo import models, fields, api

class TaskProgress(models.Model):
    _name = 'task.progress'

    name = fields.Char(string='Task')
    deadline_date = fields.Date(string='Deadline')
    status = fields.Selection([
        ('todo','To Do'),
        ('progress','Progress'),
        ('done','Done'),
        ], string='Status')
    lead_id = fields.Many2one('crm.lead', string='Lead')