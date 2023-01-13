# This file will contain all models we will be using.


class ShipAddr:
    '''
    A shipping address for a customer. Each customer will have 1 shipping address tied to them
    At the moment, only US addresses are supported
    '''

    streetAddr = ''
    'Street address, ex: 123 season ave'

    city = ''
    'City, ex: Providence'

    state = ''
    "State's 2 letter abbreviation, ex: RI"

    zipCode = ''
    'The Zip code, ex: 02907'

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            if key in dir(ShipAddr):
                setattr(self, key, value)


# A customer
class Customer:
    '''
    A customer, also a user of the site. Customers can login with their email and password.
    Passwords are then hashed and authenticated.
    '''

    fname = ''
    'First name'

    lname = ''
    'Last name'

    password = ''
    'Password, must be 8 chars, at least 1 lower and upper, number, and symbol'

    email = ''
    'Email'

    phone = ''
    'Phone number without dashes, spaces etc'

    def __init__(self, **kwargs: dict) -> None:
        for key, value in kwargs.items():
            if key in dir(Customer):
                setattr(self, key, value)
