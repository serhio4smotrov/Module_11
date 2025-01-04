import inspect


def introspection_info(obj):
    methods = []
    attribute = []
    a = str(type(obj))
    a = a[8:len(a)-2]
    dir_obj = dir(obj)
    for i in dir_obj:
        if '__' in i:
            methods.append(i)
        else:
            attribute.append(i)
    inspect.getmodule(obj)
    return {'type':a,'attribute':attribute,'methods':methods,'module':inspect.getmodule(obj)}

print(introspection_info(5))