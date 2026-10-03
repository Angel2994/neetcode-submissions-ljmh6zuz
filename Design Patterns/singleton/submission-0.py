class Singleton:
    uniqueInstance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls.uniqueInstance is None:
            cls.uniqueInstance = super(Singleton, cls).__new__(cls)
        return cls.uniqueInstance
    def getValue(self) -> str:
        return self.value
    def setValue(self, value: str):
        self.value = value