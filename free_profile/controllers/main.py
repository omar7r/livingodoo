# -*- coding: utf-8 -*-
from odoo.addons.website_portal.controllers.main import website_account


class website_account_sequences(website_account):

    OPTIONAL_BILLING_FIELDS = website_account.OPTIONAL_BILLING_FIELDS + \
        ['invoice_seq_pref', 'invoice_seq_suff', 'invoice_seq_padd',
         'invoice_seq_curr_num_next', 'refund_seq_curr_num_next',
         'sale_seq_pref', 'sale_seq_suff', 'sale_seq_padd',
         'sale_seq_curr_num_next']
