
from pyramid.view import view_config
from pyramid_mailer.message import Message
from bson import json_util
from bson import ObjectId
from bson.json_util import dumps
import json
from pyramid.response import Response
from uuid import uuid4
import secrets

# @view_config(
#     route_name='api',
#     renderer='json'
# )
# def api(request):
#     users = request.db['users'].find()
#     arr = []
#
#     for data in users:
#         data['_id'] = data['_id']
#         arr.append(data)
#
#     return {"message": "success", "data": json.encode(arr, cls=JSONEncoder)}

@view_config(
    route_name='user_login',
    request_method='POST',
    renderer='json'
)
def user_login(request):
    data = request.json_body
    rand_token = secrets.token_urlsafe(50)
    result = {
        "status": 1,
        "message": "Success",
        "data": {
            "id": "1",
            "email": data['email'],
            "password": data['password'],
            "name": "Tester Name",
            "login_token": rand_token,
            "first_name": "Le",
            "last_name": "Tuan",
            "CDL": "?",
            "license": "98454513262",
            "drive_phone_number": "0984345062",
            "picture": "http://api.drive-qa.uat.pgtest.co/upload/resource/profile/avatar.jpg",
            "carier_name": "DEV",
            "main_office_address": "HN",
            "carier_office_phone_number": "0984345062",
            "usdot_number": "120694",
            "truck_number": "123456",
            "license_plate_number": "159753",
            "odometer_unit": "Miles",
            "pick_duty_cycle": "1",
            "vehicle_type": "2",
            "30_minute_break_exempt": "true",
            "24h_cycle_reset": "true",
            "oilfield_waiting_time": "true",
            "100_air": "true",
            "16h_short_haul": "true",
            "tank_vehicle": "true",
            "150_air_mile": "true"
        }
    }
    return {
        "status": 1,
        "message": "Success",
        "data": result
    }

@view_config(
    route_name='forgot_password',
    request_method='POST',
    renderer='json'
)
def forgot_password(request):
