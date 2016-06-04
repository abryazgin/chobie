import random
import string


def rndstring(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))
