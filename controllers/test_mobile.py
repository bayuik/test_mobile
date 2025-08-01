from odoo.http import request, route, Controller

class YourController(Controller):
    @route("/standalone_app", auth="public")
    def standalone_app(self):
        return request.render(
            'test_mobile.standalone_app',
            {
                'session_info': request.env['ir.http'].get_frontend_session_info(),
            }
        )