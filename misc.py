EPSILON = 0.00001
def equals(a, b):
    if abs(a-b) < 2*EPSILON:
        return True
    else:
        return False