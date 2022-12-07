# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '1.0.0',
    'category': 'Real Estate',
    'sequence': -1000,
    'summary': 'A module for managing your real estate properties',
    'description': "This is the odoo 16 tutorial module",
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}