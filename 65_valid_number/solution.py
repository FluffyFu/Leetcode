def is_number(s):
    met_e, met_digit, met_dot = False, False, False

    for i, c in enumerate(s):
        if c == '+' or c == '-':
            # if the previous is not e, return False
            if i > 0 and s[i-1] not in ['e', 'E']:
                return False
        elif c == '.':
            if met_e or met_dot:
                return False
            met_dot = True

        elif c == 'e' or c == 'E':
            # start with e, met_e twice or haven't seen a digit.
            if i == 0 or met_e or (not met_digit):
                return False
            met_e = True
            # reset met digit after E
            met_digit = False
        elif c.isdigit():
            met_digit = True
        else:
            return False
    return met_digit

