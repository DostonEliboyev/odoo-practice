# -*- coding: utf-8 -*-
{
    'name': "Hospital",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',


        "views/patient_views.xml",
        "views/doctor_views.xml",
        "views/appointment_views.xml",
        "views/prescription_views.xml",
        "views/medicine_views.xml",

        "views/hospital_menus.xml",
    ],
    "installable": True,
    "application": True,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

