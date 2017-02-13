# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    product_id = fields.\
        Many2one(default=
                 lambda self: self.env.ref('free_profile.by_default_product'))

    @api.multi
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        if res.get('warning'):
            del res['warning']

        self.name = ""
        self.tax_id = [(6, 0, [])]
        return res
