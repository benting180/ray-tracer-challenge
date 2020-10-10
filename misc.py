def equals(a, b):
    epsilon = 0.00001
    if abs(a-b) < epsilon:
        return True
    else:
        return False
