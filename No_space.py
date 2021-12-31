import re
def no_space(x):
    e = re.sub(r'\s+', '', x)
    return e