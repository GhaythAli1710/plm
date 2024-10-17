{
    'name': 'PLM',

    'version': '17.0.1.0.0',

    'summary': """PLM, ECOs, Versions""",

    'description': """" 
    - Product Lifecycle Management
    - Manage engineering change orders on products and bills of materials.
    - Versioning of Bill of Materials and Products.
     """,

    'category': 'Manufacturing',

    'author': 'Apollo Solutions',

    'website': 'https://www.apollo-solutions.net/',

    'depends': [
        'base',
        'mrp',
    ],

    'data': [
        'security/plm_security.xml',
        'security/ir.model.access.csv',
        'data/mail_activity_type_data.xml',
        'data/plm_data.xml',
        'views/mrp_bom_views.xml',
        'views/mrp_eco_views.xml',
        'views/mrp_document_views.xml',
        'views/product_views.xml',
        'views/mrp_production_views.xml',
    ],

    'installable': True,

    'application': True,
}
