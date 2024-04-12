class ToLatin:
    def __init__(self, is_login):
        self.is_login = is_login

    def __call__(self, func):
        def wrapper(args, **kwargs):
            result = func(args, **kwargs)
            result = result.lower()
            if self.is_login:
                result = result.replace(' ', '_')
            else:
                t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh', 'з': 'z',
                     'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                     'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
                     'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
                result = ''.join(t.get(c, c) for c in result)
            return result
        return wrapper
@ToLatin(is_login=False)
def some_func(name, surname):
    return f'{surname} {name}'

print(some_func('Айбек', 'Бакиев'))

@ToLatin(is_login=True)
def some_func(name, surname):
    return f'{surname} {name}'

print(some_func('Айбек', 'Бакиев'))