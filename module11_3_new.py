


def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = dir(obj)
    methods = [method for method in attributes if callable(getattr(obj, method))]
    module = obj.__class__.__module__
    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module},
    return info

    method_list = []
    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        print(f'Имя: {attr_name:<20} Тип: {str(type(attr)):<40} Исполняемый: {callable(attr)}')
        if callable(attr):
            method_list.append(attr_name)
    info_dic['methods'] = method_list
    print('Модуль, к которому объект принадлежит:', inspect.getmodule(obj), sep='\n\t')
    info_dic['module'] = inspect.getmodule(obj)
    if inspect.isfunction(obj):
        sign = inspect.signature(obj)
        print('Передаваемый в функцию параметры:', sign.parameters, sep='\n\t')
        param_list = []
        for p_name, param in sign.parameters.items():
            param_list.append([param.name, param.default])
        info_dic['signature'] = param_list
        print('-' * 50)
    return info_dic

# Интроспекция числа
number_info = introspection_info(42)
print(number_info)

# Интроспекция строки
string_info = introspection_info('Hello')
print(string_info)

# Интроспекция списка
list_info = introspection_info([1, 20, 4.0, 'word'])
print(list_info)