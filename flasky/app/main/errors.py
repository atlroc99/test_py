from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template(template_name_or_list='404.html', code=404)


@main.errorhandler(500)
def internal_server_error(e):
    return render_template(template_name_or_list='500.html', code=500)
