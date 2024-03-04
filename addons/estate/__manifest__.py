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
    'views/estate_property_views.xml',
    'views/estate_property_type_views.xml',
    'security/ir.model.access.csv',
<<<<<<< HEAD
    'views/estate_menus.xml',],
=======
    'views/estate_menus.xml',
    'views/estate_property_form_inherit.xml'],
>>>>>>> 3968fe3090d94d4428d09da2512c15304e980457
}