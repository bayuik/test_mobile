{
    'name': 'WOW',
    'version': '1.1',
    'summary': 'Mobile',
    'license': 'LGPL-3',
    'description': "",
    'category': 'bayuik',
    'author': 'bayuik',
    'website': 'bayuik.com',
    'depends': ['base', 'web', 'portal', 'sale', 'stock'],
    'data': [
        'views/index.xml',
    ],
    'assets': {
        'test_mobile.assets': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',

            # pos
            ("include", "web._assets_helpers"),
            ("include", "web._assets_backend_helpers"),
            ("include", "web._assets_primary_variables"),
            "web/static/src/scss/pre_variables.scss",
            "web/static/lib/bootstrap/scss/_functions.scss",
            "web/static/lib/bootstrap/scss/_variables.scss",
            'web/static/lib/bootstrap/scss/_variables-dark.scss',
            'web/static/lib/bootstrap/scss/_maps.scss',
            ("include", "web._assets_bootstrap"),
            ("include", "web._assets_bootstrap_backend"),
            ('include', 'web._assets_core'),
            ("remove", "web/static/src/core/browser/router.js"),
            ("remove", "web/static/src/core/debug/**/*"),
            "web/static/src/libs/fontawesome/css/font-awesome.css",
            "web/static/src/views/fields/formatters.js",
            "web/static/lib/odoo_ui_icons/*",
            'web/static/src/legacy/scss/ui.scss',
            'bus/static/src/services/bus_service.js',
            'bus/static/src/bus_parameters_service.js',
            'bus/static/src/multi_tab_service.js',
            'bus/static/src/workers/*',
            'web/static/src/scss/functions.scss',

            # JS boot
            # 'web/static/src/module_loader.js',
            # # libs (should be loaded before framework)
            # 'point_of_sale/static/lib/**/*',
            # 'web/static/lib/luxon/luxon.js',
            # 'web/static/lib/owl/owl.js',
            # 'web/static/lib/owl/odoo_module.js',
            # 'web/static/lib/zxing-library/zxing-library.js',
            #
            # 'web/static/src/core/colorlist/colorlist.scss',
            # 'web/static/src/webclient/webclient_layout.scss',
            #
            # 'web/static/src/webclient/icons.scss',
            #
            # # scss variables and utilities
            # 'web/static/src/scss/bootstrap_overridden.scss',
            # 'web/static/src/scss/fontawesome_overridden.scss',
            # 'web/static/fonts/fonts.scss',
            #
            # ('remove', 'web/static/src/core/errors/error_handlers.js'),
            # # error handling in PoS is different from the webclient
            # ('remove', '/web/static/src/core/dialog/dialog.scss'),
            # 'web/static/src/core/currency.js',
            # # barcode scanner
            # 'barcodes/static/src/barcode_service.js',
            # 'barcodes/static/src/js/barcode_parser.js',
            # 'barcodes_gs1_nomenclature/static/src/js/barcode_parser.js',
            # 'barcodes_gs1_nomenclature/static/src/js/barcode_service.js',
            # 'web/static/src/views/fields/parsers.js',
            # # report download utils
            # 'web/static/src/webclient/actions/reports/utils.js',
            # # PoS files
            # ('remove', 'point_of_sale/static/src/backend/**/*'),
            # ('remove', 'point_of_sale/static/src/customer_display/**/*'),
            # 'point_of_sale/static/src/customer_display/utils.js',
            # # main.js boots the pos app, it is only included in the prod bundle as tests mount the app themselves
            # ('remove', 'point_of_sale/static/src/app/main.js'),
            # # account
            # 'account/static/src/helpers/*.js',
            # 'account/static/src/services/account_move_service.js',
            #
            # 'mail/static/src/core/common/sound_effects_service.js',
            # "web/static/src/core/browser/router.js",
            # "web/static/src/core/debug/**/*",
            # 'web/static/src/model/**/*',
            # 'web/static/src/views/**/*',
            # 'web/static/src/search/**/*',
            # 'web/static/src/webclient/actions/**/*',
            # ('remove', 'web/static/src/webclient/actions/reports/layout_assets/**/*'),
            # ('remove', 'web/static/src/webclient/actions/**/*css'),
            # 'web/static/src/webclient/company_service.js',

            # 'web/static/src/scss/import_bootstrap.scss',
            # 'web/static/src/scss/utilities_custom.scss',
            # 'web/static/lib/bootstrap/scss/utilities/_api.scss',
            # 'web/static/src/scss/bootstrap_review.scss',
            # ('include', 'web._assets_bootstrap'),
            # ('include', 'web.assets_backend'),
            # ('include', 'web.assets_frontend_minimal'),
            # ('include', 'web.assets_frontend'),
            # ('include', 'web._assets_primary_variables'),
            # ('include', 'web._assets_secondary_variables'),
            # ('include', 'web._assets_jquery'),
            # ('include', 'web._assets_bootstrap_frontend'),
            # ('include', 'web._assets_bootstrap_backend'),
            # ('include', 'web._assets_backend_helpers'),
            # ('include', 'web._assets_frontend_helpers'),
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),

            'test_mobile/static/src/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
