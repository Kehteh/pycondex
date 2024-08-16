# SOLVED

def can_climb(has_helmet: bool, has_rope: bool):
    if has_helmet is True and has_rope is True:
        return True
    else:
        return False
print(can_climb(True, True))