# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'version': '1.0.0',
    'category': 'Real Estate',
    'sequence': -100,
    'summary': 'A module for managing your real estate properties',
    'description': "This is the odoo 16 tutorial module",
    'depends': [
        'base',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}