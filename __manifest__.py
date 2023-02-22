# -*- coding: utf-8 -*-
{
    'name': 'Mercado Pago Chile',
    'description': "Addon para recibir pagos a través del sitio web de comercio electrónico chile",
    'author': "Israel Ubeda Bravo",
    'website': "https://israelubeda.github.io/",
    'summary': "Mercado Pago para sitio web de comercio electrónico Chile",
    'version': '14.0.1.0.1',
    "license": "OPL-1",
    'price':'15',
    'currency':'USD',
    'support': 'israel.ubedabravo@gmail.com',
    'category': 'Website',
    "images": ["images/banner_mercado.png"],
    'depends': ['base','website_sale','payment','account'],
    'data': [
                'views/templates.xml',
                'views/payment_acquirer.xml',
                'views/sale_order.xml',
                'views/payment_transaction.xml',
                'views/ir_cron.xml',
                'data/mercadopago.xml',
            ],
    'qweb': [
              
            ],
    'installable': True,
}