def generate_password_def(length=8):
    import secrets
    import string
    number = string.digits 
    return ''.join(secrets.choice(number) for number in range(length))