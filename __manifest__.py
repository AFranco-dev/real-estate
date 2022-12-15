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
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/res_users_views.xml',
        'views/estate_menus.xml',
    ],
    'demo': [
        'data/estate_demo.xml',],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}