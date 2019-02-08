try:
    from collections import UserDict
except ImportError:
    from UserDict import UserDict


class Registry(UserDict):
    def register(self, key, function=None):
        if function is not None:
            # Called as Registry.register('key', function)
            self.data[key] = function
            return

        def decorator(func):
            self.data[key] = func

        return decorator
