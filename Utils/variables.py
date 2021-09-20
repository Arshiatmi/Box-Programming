from .enums import *


class Variable:
    def __init__(self,name: str,Type: Types):
        self.name = name
        self.type = Type
        if self.type == Types.boolean:
            self._value = False
        elif self.type == Types.number:
            self._value = 0
        elif self.type == Types.string:
            self._value = ""
    
    # Value Property
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        if type(value) == self.type.value:
            self._value = value
        else:
            raise ValueError(f"Value Must Be Type Of {self.type}")
    
    # ==
    def __eq__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.type:
                if o.value == self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.type}")
        else:
            if self.value == o:
                return True
    
    # <
    def __lt__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.type:
                if o.value < self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.type}")
        else:
            if self.value == o:
                return True

    # >
    def __gt__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.type:
                if o.value > self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.type}")
        else:
            if self.value == o:
                return True

    # <=
    def __le__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.type:
                if o.value <= self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.type}")
        else:
            if self.value == o:
                return True

    # >=
    def __ge__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.type:
                if o.value >= self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.type}")
        else:
            if self.value == o:
                return True