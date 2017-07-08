
# DuongKien - PowerGate
def includeme(config):

    config.add_route('home', '/')
    config.add_route('cities', '/cities')
    config.add_route('city', '/cities/{name}')
    config.add_route('api', '/api')
