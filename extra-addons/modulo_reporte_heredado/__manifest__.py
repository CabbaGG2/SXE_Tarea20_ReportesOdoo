# -*- coding: utf-8 -*-
{
    'name': "modulo_reporte_heredado",

    'summary': "Modulo que realiza una modificación menor en el reporte de ventas.",

    'description': """
Modulo que realizar una modificación en el reporte de Ventas heredandolo y añadiendo los cambios en la zona correcta.
    """,

    'author': "CabbaGG Corp.",
    'website': "https://cabbagg.github.io/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/report_presupuesto_firma.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

