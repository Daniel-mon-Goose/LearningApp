def lowercase(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs).lowercase()

    return wrapper
