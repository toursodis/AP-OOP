class Employee:
    def __init__(self,fn,**kwargs):
        self.full_name=fn
        for key,value in kwargs.items():
            setattr(self, key, value)
