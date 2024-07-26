class polygon():
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

class rectangle(polygon):
    def square(self):
        return(f"Rectangle square: {self.arg1 * self.arg2}")
        
r = rectangle(3, 6)
print(r.square())