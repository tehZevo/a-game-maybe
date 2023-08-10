
def dict_op(a, b, op):
  return {k: op(v, b[k]) for k, v in a.items()}
