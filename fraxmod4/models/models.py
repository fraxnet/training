# -*- coding: utf-8 -*-

from odoo import models, fields, api


class fraxmod4(models.Model):
    _name = 'fraxmod4.fraxmod4'
    _description = 'fraxmod4.fraxmod4'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    start_datetime = fields.Datetime('Start time', default=lambda self: fields.Datetime.now())
    value3 = fields.Char()
    


    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100
