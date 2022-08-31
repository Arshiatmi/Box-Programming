from Utils.functions import make_id_from_name
from .enums import *
from Utils.global_vars import variables, options


class Variable:
    VariableTypes = [Types.number, Types.boolean, Types.text]

    def __init__(self, name: str, Type: Types):
        global variables
        self.id = make_id_from_name(name)
        variables[self.id] = self
        self.name = name
        self.Type = Type

    @staticmethod
    def is_number(number):
        if type(number) in [float, int]:
            return True
        return False

    # Value Property
    @property
    def value(self):
        if self.Type.value == float:
            if int(self._value) == self._value:
                return int(self._value)
        return self._value

    @value.setter
    def value(self, value):
        if self.Type.value == float and Variable.is_number(value):
            self._value = float(value)
        elif type(value) == self.Type.value:
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
            if type(o) == self.Type:
                if o == self.value:
                    return True
            elif type(o) == type(self):
                if o.value == self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.Type}")
        else:
            if self.value == o:
                return True
        return False

    # <
    def __lt__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.Type:
                if o < self.value:
                    return True
            elif type(o) == type(self):
                if o.value < self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.Type}")
        else:
            if self.value < o:
                return True
        return False

    # >
    def __gt__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.Type:
                if o > self.value:
                    return True
            elif type(o) == type(self):
                if o.value > self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.Type}")
        else:
            if self.value > o:
                return True
        return False

    # <=
    def __le__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.Type:
                if o <= self.value:
                    return True
            elif type(o) == type(self):
                if o.value <= self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.Type}")
        else:
            if self.value <= o:
                return True
        return False

    # >=
    def __ge__(self, o: object) -> bool:
        if o.__class__ == Variable:
            if type(o) == self.Type:
                if o >= self.value:
                    return True
            elif type(o) == type(self):
                if o.value >= self.value:
                    return True
            else:
                raise ValueError(f"Value Must Be Type Of {self.Type}")
        else:
            if self.value >= o:
                return True
        return False

    def __str__(self) -> str:
        return f"Variable({self.value})"

    def __repr__(self) -> str:
        return f"Variable({self.value})"


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
