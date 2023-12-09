class Employee :
    def __init__(self,fn:str,ln:str):
        self.first_name=fn
        self.last_name=ln
        self.full_name=f"{fn} {ln}"
        self.email=f"{fn.lower()}.{ln.lower()}@company.com"