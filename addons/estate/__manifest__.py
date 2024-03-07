{
    'name': 'ESTATE',
    'depends' : [
        'base_setup',
        'sales_team',
        'mail',
        'calendar',
        'resource',
        'utm',
        'web_tour',
        'contacts',
        'digest',
        'phone_validation',
    ],
    'application': True,
    'data' : [
        'views/estate_property_tag_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_property_views.xml',
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        ],
}