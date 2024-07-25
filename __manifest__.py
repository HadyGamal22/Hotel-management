{
    'name': 'Practice',
    'description': 'practice ',
    'author': 'Hady Gamal',
    'depends': ['base','crm','sale_management','account_accountant','mail','contacts'],
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/base_menu.xml',
        'data/sequence.xml',
        'views/property_view.xml',
        'views/account_move.xml',
        'views/building.xml',
        'views/property_history_view.xml',
        'views/owner_view.xml',
        'views/sale_order.xml',
        'views/res_partner.xml',
        'wizard/change_state_wizard.xml',
        'reports/property_report.xml',

    ],
    'assets': {
        'web.assets_backend':['practice/static/src/css/property.css',],
        'web.report_assets_common':['practice/static/src/css/font.css',],
    }
    #F:\odoo\assuit_2023\hms\security
}
