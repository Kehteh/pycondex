def login(password: str):
    """Only users who enter the password "quartzgleam?1" can log in successfully.

    Arguments:
        - password: a string representing the user's password input.

    Returns:
        - a boolean representing whether or not the user's password was correct.
    """
    if password == "quartzgleam?1":
        return True 
    else:
        return False
print(login(password="code_ thief21"))
