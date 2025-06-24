import random

def dict_op(a, b, op):
  return {k: op(v, b[k]) for k, v in a.items()}

#TODO: constants
JOIN_CODE_LENGTH = 5
JOIN_CODE_CHARS = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"

def create_join_code(length=JOIN_CODE_LENGTH):
  return "".join(random.choice(JOIN_CODE_CHARS) for _ in range(length))
