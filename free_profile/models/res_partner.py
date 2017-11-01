# -*- coding: utf-8 -*-

from odoo import fields, models, api


class ResPartner(models.Model):

    _inherit = "res.partner"

    @api.depends('invoice_seq_pref', 'invoice_seq_suff', 'invoice_seq_padd',
                 'invoice_seq_num_next', 'refund_seq_num_next')
    @api.multi
    def _get_inv_seq_example(self):
        for part in self:
            part.invoice_seq_example = (part.invoice_seq_pref or '') + \
                '%%0%sd' % part.invoice_seq_padd % part.invoice_seq_num_next +\
                (part.invoice_seq_suff or '')
            part.refund_seq_example = u'AB' + (part.invoice_seq_pref or '') + \
                '%%0%sd' % part.invoice_seq_padd % part.refund_seq_num_next +\
                (part.invoice_seq_suff or '')

    @api.depends('sale_seq_pref', 'sale_seq_suff', 'sale_seq_padd',
                 'sale_seq_num_next')
    @api.multi
    def _get_sale_seq_example(self):
        for part in self:
            part.sale_seq_example = (part.sale_seq_pref or '') + \
                '%%0%sd' % part.sale_seq_padd % part.sale_seq_num_next +\
                (part.sale_seq_suff or '')

    user_id = fields.Many2one(default=lambda self: self.env.user.id)
    invoice_seq_pref = fields.Char("Invoice seq. prefix")
    invoice_seq_suff = fields.Char("Invoice seq. suffix")
    invoice_seq_padd = fields.Integer("Invoice seq. padding", required=True,
                                      default=0)
    invoice_seq_num_next = fields.Integer("Invoice seq. num. next",
                                          default=1, required=True)
    invoice_seq_example = fields.Char("Invoice seq. example",
                                      compute="_get_inv_seq_example",
                                      readonly=True, multi=True)
    invoice_sequence_id = fields.Many2one("ir.sequence", "Invoice seq.",
                                          readonly=True)
    sale_seq_pref = fields.Char("Sale seq. prefix")
    sale_seq_suff = fields.Char("Sale seq. suffix")
    sale_seq_padd = fields.Integer("Sale seq. padding", required=True,
                                   default=0)
    sale_seq_num_next = fields.Integer("Sale seq. num. next",
                                       default=1, required=True)
    sale_seq_example = fields.Char("Sale seq. example",
                                   compute="_get_sale_seq_example",
                                   readonly=True)
    sale_sequence_id = fields.Many2one("ir.sequence", "Sales seq.",
                                       readonly=True)
    refund_seq_num_next = fields.Integer("Refund invoice seq. num. next",
                                         default=1, required=True,
                                         help="Same prefix and suffix that "
                                              "invoice sequence adding 'AB' "
                                              "in the prefix")
    refund_sequence_id = fields.Many2one("ir.sequence", "Refund seq.",
                                         readonly=True)
    refund_seq_example = fields.Char("Refund seq. example",
                                     compute="_get_inv_seq_example",
                                     readonly=True, multi=True)

    @api.multi
    def write(self, vals):
        res = super(ResPartner, self).write(vals)
        if 'invoice_seq_pref' in vals or 'invoice_seq_suff' in vals or \
                'invoice_seq_padd' in vals or 'invoice_seq_num_next' in vals \
                or 'refund_seq_num_next' in vals:
            for part in self:
                if 'invoice_seq_pref' in vals:
                    prefix = vals['invoice_seq_pref'] or ''
                else:
                    prefix = part.invoice_seq_pref or ''
                if 'invoice_seq_suff' in vals:
                    suffix = vals['invoice_seq_suff'] or ''
                else:
                    suffix = part.invoice_seq_suff or ''
                if 'invoice_seq_padd' in vals:
                    padding = int(vals['invoice_seq_padd'] or 0)
                else:
                    padding = part.invoice_seq_padd or 0
                if not part.invoice_sequence_id:
                    if 'invoice_seq_num_next' in vals:
                        number_next = int(vals['invoice_seq_num_next'] or 1)
                    else:
                        number_next = 1
                    seq_pool = self.env["ir.sequence"]
                    seq = seq_pool.create({'name': u'Invoice seq. ' +
                                           part.name,
                                          'prefix': prefix,
                                          'suffix': suffix,
                                          'number_next': number_next,
                                          'padding': padding})
                    part.invoice_sequence_id = seq.id
                else:
                    if 'invoice_seq_num_next' in vals:
                        number_next = int(vals['invoice_seq_num_next'] or 1)
                    else:
                        number_next = part.invoice_sequence_id.number_next
                    part.invoice_sequence_id.\
                        write({'name': u'Invoice seq. ' + part.name,
                               'prefix': prefix,
                               'suffix': suffix,
                               'number_next': number_next,
                               'padding': padding})
                if not part.refund_sequence_id:
                    if 'refund_seq_num_next' in vals:
                        number_next = int(vals['refund_seq_num_next'] or 1)
                    else:
                        number_next = 1
                    seq_pool = self.env["ir.sequence"]
                    seq = seq_pool.create({'name': u'Refund seq. ' +
                                           part.name,
                                          'prefix': u'AB' + prefix,
                                          'suffix': suffix,
                                          'number_next': number_next,
                                          'padding': padding})
                    part.refund_sequence_id = seq.id
                else:
                    if 'refund_seq_num_next' in vals:
                        number_next = int(vals['refund_seq_num_next'] or 1)
                    else:
                        number_next = part.refund_sequence_id.number_next
                    part.refund_sequence_id.\
                        write({'name': u'Refund seq. ' + part.name,
                               'prefix': u'AB' + prefix,
                               'suffix': suffix,
                               'number_next': number_next,
                               'padding': padding})
        if 'sale_seq_pref' in vals or 'sale_seq_suff' in vals or \
                'sale_seq_padd' in vals or 'sale_seq_num_next' in vals:
            for part in self:
                if 'sale_seq_pref' in vals:
                    prefix = vals['sale_seq_pref'] or ''
                else:
                    prefix = part.sale_seq_pref or ''
                if 'sale_seq_suff' in vals:
                    suffix = vals['sale_seq_suff'] or ''
                else:
                    suffix = part.sale_seq_suff or ''
                if 'sale_seq_padd' in vals:
                    padding = int(vals['sale_seq_padd'] or 0)
                else:
                    padding = part.sale_seq_padd or 0
                if not part.sale_sequence_id:
                    if 'sale_seq_num_next' in vals:
                        number_next = int(vals['sale_seq_num_next'] or 1)
                    else:
                        number_next = 1
                    seq_pool = self.env["ir.sequence"]
                    seq = seq_pool.create({'name': u'Sale seq. ' +
                                           part.name,
                                           'code': 'sale.order',
                                           'prefix': prefix,
                                           'suffix': suffix,
                                           'number_next': number_next,
                                           'padding': padding})
                    part.sale_sequence_id = seq.id
                else:
                    if 'sale_seq_num_next' in vals:
                        number_next = int(vals['sale_seq_num_next'] or 1)
                    else:
                        number_next = part.sale_sequence_id.number_next
                    part.sale_sequence_id.\
                        write({'name': u'Sale seq. ' + part.name,
                               'prefix': prefix,
                               'suffix': suffix,
                               'number_next': number_next,
                               'padding': padding})

        return res
