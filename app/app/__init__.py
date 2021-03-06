
from pyramid.config import Configurator
from pyramid.renderers import JSON

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Connect database
    config.include('.db')

    # Routes
    config.include('.routes')

    # Mailer
    config.include('pyramid_mailer')

    config.scan()
    return config.make_wsgi_app()
