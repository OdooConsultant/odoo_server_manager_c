# -*- coding: utf-8 -*-
{
    'name': "Start, Stop, Restart | Odoo Server Manager",

    'summary': """
        This module allows you to control the odoo server through the odoo interface, including starting, stopping, and restarting the server.""",

    'description': """
You can use a URL, username, password, and commands to manage the details of your server. You can also start, stop, and restart the Odoo server through the Odoo interface. A history of these actions will be maintained, including information on who performed the action and when it was performed.

    """,

    'author': "Medconsultantweb@gmail.com",
    'category': 'Extra Tools',
    'license': 'OPL-1',
    'price': 35,
    'currency': 'EUR',
    'version': '15.0.0.0',
    'depends': ['base'],
    'external_dependencies': {'python' : ["pexpect"]},
    'data': [
        'security/ir.model.access.csv',
        'security/odoo_restart_security.xml',
        'views/odoo_restart.xml',
        'views/warning_box.xml',

    ],

    'images': [
        'static/description/module_image.jpg',
    ],
}
