# -*- coding: utf-8 -*-
{
    'name': "Inherit CRM",

    'summary': """
        inherit_crm""",

    'description': """
        inherit_crm
    """,

    'author': "Melia",
    'website': "https://github.com/meliaprisca",

    'category': 'CRM',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
            'base',
            'crm',
            ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/segment_product_data.xml',
        'views/crm_lead.xml',
        'views/segment_product.xml',
    ],
}
