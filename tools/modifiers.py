import string


def lowercase(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs).lowercase()

    return wrapper


def format_check(filename_attr: string, format: string):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            filename = getattr(self, filename_attr)
            if not filename.endswith(format):
                raise ValueError(f'Wrong format for {filename}, expected {format}')
            return func(self, *args, **kwargs)

        return wrapper

    return decorator
