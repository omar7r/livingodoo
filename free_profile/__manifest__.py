# -*- coding: utf-8 -*-
{
    'name': 'Free profile',
    'version': '10.0.1.0.0',
    'category': 'Sales',
    'summary': 'Free Profile Livingodoo',
    'description': """
Creates new user groups that limit the sales ans invoice views for
livingodoo.com free profile.
Manage this profile from web.
    """,
    'website': 'http://comunitea.com',
    'depends': ['sales_team', 'account', 'calendar', 'sale',
                'auth_signup', 'website_partner', 'website_portal'],
    'data': ['security/free_profile_security.xml',
             'security/ir.model.access.csv',
             'data/free_profile_data.xml',
             'views/sale_view.xml',
             'views/partner_view.xml',
             'views/account_view.xml',
             'views/main_report_layout.xml',
             'views/website_portal_template.xml'],
    'demo': [],
    'css': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
