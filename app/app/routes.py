
def includeme(config):
    config.add_route('home', '/')
    config.add_route('cities', '/cities')
    config.add_route('city', '/cities/{name}')
    config.add_route('api', '/api')
    config.add_route('user_login', '/user/login')
    config.add_route('forgot_password', 'user/forgotPassword')
