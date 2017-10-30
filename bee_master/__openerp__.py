# __openerp__.py
{
    'name': "Bee master",
    'version': '8.0',
    'description': """
        Bee master with following features:
        - Bee master data
        """,
    'author': 'Leo',
    'website': 'http://www.leo-guggenberger.at',
    'category': 'Generic Modules/Others',
    'depends': ['web'],
    'data': ['static/src/xml/animals_view.xml'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
}
