from datetime import datetime
import re


def dateCheck(date: str):
    '''
    Checks if date is in correct format. Accepted formats are mm-dd-yyyy and mm/dd/yyyy

    Args:
        date (str): The date to check
    '''
    result = True
    try:
        result = bool(datetime.strptime(date, '%m-%d-%Y'))
    except ValueError:
        try:
            result = bool(datetime.strptime(date, '%m/%d/%Y'))
        except ValueError:
            result = False
    return result


def emailCheck(email: str):
    '''
    Checks if email is correctly formatted. Accepted format is a@b.c (any amount of .c, like a@b.c.d.e)

    Args:
        email (str): The email to validate
    '''
    # To match email patterns. Broken up this reads:
    # The pattern for everything before the @. Match at least 1-unlimit alphanumeric
    # followed by 0-unlimit of + or . or any alphanumeric or -. Then have @
    reg1 = r'^\w+[\+\.\w-]*@'
    # Pattern for domain. First have a group that matches 1-unlimit alphanumeric or -,
    # then must have . char. This group can be repeated 0-unlimit times. Then match a word 1-unlimit,
    # then 0-unlimit an alphanumeric or - followed by a .
    reg2 = r'([\w-]+\.)*\w+[\w-]*\.'
    # Pattern for extension. A group that matches lowercase letters 2-4 times OR matches 1-unlimit digit
    reg3 = r'([a-z]{2,4}|\d+)$'
    regex = reg1+reg2+reg3
    return re.match(regex, email)


def phoneCheck(phone: str):
    '''
    Checks for valid phone numbers using pattern matching. Note the number could be fake...
    Valid phone numbers potentially start with +, followed by the whole number including area code
    If international, can use 44 as well, but no spaces or - within number

    Args:
        phone (str): The phone number to check
    '''
    # Replace unwanted characters
    phone = phone.strip('-')
    phone = phone.strip()
    # Start with 0-1 +, then 1-15 numbers after
    regex = r'^[+]?([0-9]{1,15})$'
    return re.match(regex, phone)
