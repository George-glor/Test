# This is our super secret key:
Privet = 'this is privet informations'

class Error:
     def __init__(self):
        pass


user_input = '{error.__init__.__globals__[SECRET]}'


err = Error()
user_input.format(error=err)