import functools

if 'DEBUG' not in globals():
    DEBUG = True

def printc(func):
    if not DEBUG:
        return func

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        sarg = ', '.join(map(repr, args))
        kformat = lambda x: '{}={}'.format(x[0], repr(x[1]))
        skwarg = ', '.join(map(kformat, kwargs.items()))

        paramaters = sarg
        if sarg and skwarg:
            paramaters += ', '
        paramaters += skwarg

        print('{}{}({})'.format(printc.indent * printc.depth, func.__name__, paramaters))
        printc.depth += 1
        ret = func(*args, **kwargs)
        printc.depth -= 1
        if ret != None:
            print('{}{}({}) => {}'.format(printc.indent * printc.depth, func.__name__, paramaters, repr(ret)))
        return ret

    return wrapper

printc.depth = 0
printc.indent = '| '
