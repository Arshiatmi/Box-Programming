from .enums import *
from .global_vars import variables


class Variable:
    VariableTypes = [Types.number, Types.boolean, Types.text]

    def __init__(self, name: str, Type: Types):
        global variables
        variables[name] = self
        self.name = name
        self.Type = Type

    # Value Property
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) == self.Type.value:
            self._value = value
        else:
            raise ValueError(f"Value Must Be Type Of {self.Type}")

    # Type Property
    @property
    def Type(self):
        return self._type

    @Type.setter
    def Type(self, target_type):
        self._type = target_type
        if self._type == Types.boolean:
            self._value = False
        elif self._type == Types.number:
            self._value = 0.0
        elif self._type == Types.text:
            self._value = ""
        elif self._type == Types.executable:
            self._value = None
        elif self._type == Types.variable:
            raise ValueError("Variable Type Cannot Be Used As A Value")
        else:
            raise ValueError(
                "Invalid Type. Type Must Be boolean, number or text")

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
            if self.value < o:
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
            if self.value > o:
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
            if self.value <= o:
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
            if self.value >= o:
                return True


def detect_variable_type(value: object, return_variable_type=True) -> Types:
    if value.__class__ == Variable:
        if value.Type in Variable.VariableTypes or value.Type == Types.variable:
            return value.Type
        else:
            raise ValueError("Invalid Type")
    if type(value) == bool:
        if return_variable_type:
            return Types.variable
        return Types.boolean
    elif type(value) == int or type(value) == float:
        if return_variable_type:
            return Types.variable
        return Types.number
    elif type(value) == str:
        if return_variable_type:
            return Types.variable
        return Types.text
    else:
        raise ValueError("Invalid Type")
