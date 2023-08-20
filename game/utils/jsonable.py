# from enum import Enum
# import json
#
# # class JSONable:
# #   def __init__(self):
# #     pass
# #
# #   def __from_json__(obj):
# #     return
# #
# #   def __json__(self):
# #     return self.__dict__
#
# # def jsonable(cls):
# #   def __to_json__(self):
# #     return self.__dict__
# #
# #   def __from_json__(obj):
# #     return cls(**obj)
#
# def dictable(cls):
#   if not hasattr(cls, "__to_dict__"):
#     def __to_dict__(self):
#       return self.__dict__
#     setattr(cls, "__to_dict__", __to_dict__)
#
#   if hasattr(cls, "__from_dict__"):
#     def __from_dict__(d):
#       return cls(**d)
#     setattr(cls, "__from_dict__", __from_dict__)
#
#   return cls
#
# @dictable
# class Foo:
#   def __init__(self, a, b):
#     self.a = a
#     self.b = b
#
# # @dictable
# class DictableEnum(Enum):
#   def __init__(self):
#     super().__init__()
#
#   def __dict__(self):
#     return {"type": self.}
#
# # print(Foo(1, 2).__to_dict__())
# print(DictableEnum.__dict__)
# # print(json.dumps(DictableEnum.A, default=lambda o:o.__dict__))

from dataclasses import dataclass
from enum import Enum
from dacite import from_dict, Config

class E(Enum):
    X = 1
    Y = 2
    Z = 3

@dataclass
class A:
    e: E


data = {
    'e': 1,
}

#TODO: write handler for dict that just maps to value
json.dumps(event, default=lambda o: o.__dict__)

# result = from_dict(data_class=A, data=data, config=Config(cast=[E]))

# or

result = from_dict(data_class=A, data=data, config=Config(cast=[Enum]))
print(result)
# assert result == A(e=E.X)
