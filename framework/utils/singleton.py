class singleton:
    def __init__(self, _class):
        self.__class = _class
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = self.__class(*args, **kwargs)
        return self.__instance
