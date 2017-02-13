# -*- coding: utf-8 -*-

from odoo import fields, models


class ResPartner(models.Model):

    _inherit = "res.partner"

    user_id = fields.Many2one(default=lambda self: self.env.user.id)
