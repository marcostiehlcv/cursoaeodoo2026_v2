{
    'name': 'Real Estate MS',
    'version': '19.0.1.0.0',
    'summary': 'Real Estate MStiehl',
    'description': '',
    'author': 'Marco Stiehl',
    'website': '',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    "data": [
        "security/ir.model.access.csv",
        "views/estate_listing_type_views.xml",
        "views/estate_listing_views.xml",
        "views/property_category_views.xml",
        "views/property_offer_views.xml",
        "views/property_tag_views.xml",
        "views/property_type_views.xml",
        "views/property_views.xml",
        "menu/menu.xml"
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}