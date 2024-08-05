def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]


class Human:
    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r})"


class Man(Human):
    def __init__(self, name="Adam"):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name="Eve"):
        super().__init__(name)