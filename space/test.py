class Manet:
    #class attribute
    shape="round"
    def __init__(self, name):
        self.name=name
    
    @classmethod
    def common(cls):
            return f"All planet are {cls.shape}"
    
    @staticmethod
    def spin(speed="2000 mph"):
        return f"This planet spins at {speed}!"


