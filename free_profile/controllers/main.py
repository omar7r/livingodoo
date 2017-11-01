# -*- coding: utf-8 -*-
from odoo.addons.website_portal.controllers.main import website_account
#~ from odoo import http
#~ from odoo.http import request


class website_account_sequences(website_account):

    #~ SEQUENCE_FIELDS = ['invoice_seq_pref', 'invoice_seq_suff',
                       #~ 'invoice_seq_padd', 'invoice_seq_num_next',
                       #~ 'refund_seq_num_next', 'sale_seq_pref', 'sale_seq_suff',
                       #~ 'sale_seq_padd', 'sale_seq_num_next']

    OPTIONAL_BILLING_FIELDS = website_account.OPTIONAL_BILLING_FIELDS + \
        ['invoice_seq_pref', 'invoice_seq_suff', 'invoice_seq_padd',
         'invoice_seq_num_next', 'refund_seq_num_next', 'sale_seq_pref',
         'sale_seq_suff', 'sale_seq_padd', 'sale_seq_num_next']

    #~ @http.route()
    #~ def details(self, redirect=None, **post):
        #~ partner = request.env.user.partner_id
        #~ if post:
            #~ error, error_message = self.details_form_validate(post)
            #~ if not error:
                #~ values ={key: post[key] for key in self.SEQUENCE_FIELDS
                         #~ if key in post}
                #~ partner.sudo().write(values)
        #~ return super(website_account_sequences, self).\
            #~ details(redirect=redirect, **post)
