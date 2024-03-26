class D():
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return f"D('{self.name}')"

d=D('123')

b=eval(repr(d))