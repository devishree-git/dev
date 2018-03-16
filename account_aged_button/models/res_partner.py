# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import timedelta


class ResPartner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    def open_partner_aged(self):
        return {'type': 'ir.actions.client',
            'name': _('Partner Aged'),
            'tag': 'account_report',
            'options': {'partner_id': self.id},
            'ignore_session': 'both',
            'context': "{'model':'account.aged.partner'}"}

