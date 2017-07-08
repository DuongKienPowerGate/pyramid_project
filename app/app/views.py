from pyramid.view import view_config
from bson.json_util import dumps
import json
from bson import json_util

@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'app'}


CITIES = {
    'paris': {
        'name': 'Paris',
        'population': '2,234,105'
    },
    'sf': {
        'name': 'San Francisco',
        'population': '812,826'
    }
}

@view_config(route_name='city', renderer='json')
def get_city(request):
    name = request.matchdict['name']
    return CITIES[name]

@view_config(route_name='cities', renderer='json')
def list_cities(request):
    return CITIES

@view_config(route_name='api',renderer='json')
def api(request):
    users = request.db['users'].find()
    return {"data": dumps(users)}
