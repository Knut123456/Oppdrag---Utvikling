def generate_password_def(length=8): #gjør slik at vis jeg ikke gir noe paramter så er den defult 8
    #lage en key
    #TODO make it send a email so it verifys the account 
    import secrets
    import string
    number = string.digits #tar alle string
    return ''.join(secrets.choice(number) for number in range(length)) # gjør slik at sercet libary velger random ord 
    # gjør det 8 ganger