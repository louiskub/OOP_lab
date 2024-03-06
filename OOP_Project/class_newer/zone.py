class Zone:
    def __init__(self, name):
        self.__name = name
        self.__cabana_list = []

    @property
    def name(self):
        return self.__name
    
    @property
    def cabana_list(self):
        return self.__cabana_list 