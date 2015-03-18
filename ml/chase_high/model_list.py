__author__ = 'zhanyingbo'

from dataScript import model

NOT_METHOD_FUNCTION = (
    'performance_evaluation',  '__doc__', '__file__', '__name__', '__package__', 'array',
)

def get_model_methods():
    methods = dir(model)
    for method in methods:
        if method[0:2] != 'm_':
            methods.remove(method)
    return methods


