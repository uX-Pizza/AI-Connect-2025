"""
Feel free to change, I used this for demonstration only.
"""

class Constraint:
    def __init__(self):
        self.a = None
        self.b = None
        self.type = None


    def __repr__(self):
        return f"<{self.a}, {self.b} --> {self.type}>"


    def complete(self):
        return self.a is not None and self.b is not None