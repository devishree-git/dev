# -*- coding: utf-8 -*-
{
    'name' : 'Partner Aged Reports',
    'summary': 'View and create reports',
    'category': 'Accounting',
    'description': """
Accounting Reports
==================
    """,
    'depends': ['account_reports'],
    'data': [
        'views/partner_view.xml',
    ],
    'qweb': [ ],
    'auto_install': False,
    'installable': True,
}
