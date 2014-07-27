__options = {
    'p': '\033[95m',
    'c': '\033[94m',
    'y': '\033[93m',
    'g': '\033[92m',
    'r': '\033[91m',
    'b': '\033[1m',
    'x': '\033[0m'
}


def prettify(thing):
    if type(thing) is dict:
        pass
    return str(thing)


def log(thing, options):
    prefix = ''.join([__options[option] for option in options if option in __options])
    print prefix + prettify(thing) + __options['x']