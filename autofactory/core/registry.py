try:
    from collections import UserDict
except ImportError:
    # PORT: Python 2.
    from UserDict import UserDict


class Registry(UserDict):
    def register(self, key, value=None):
        """A convenience method to register values.

        Can be used as a function or as a decorator:

            r.register('key', as_a_function)

            @r.register('key')
            def as_a_decorator():
                ...

        """
        if value is not None:
            self._register(key, value)
            return

        def decorator(func):
            self._register(key, func)

        return decorator

    def unregister(self, key):
        self.pop(key, None)

    def _register(self, key, value):
        self.data[key] = value
