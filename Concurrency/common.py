def is_number(possible_number):
    """
    Check if a something is a number

    >>> is_number(5)
    True
    >>> is_number('-1.34')
    True
    >>> is_number('Hallo!')
    False
    """

    try:
        float(possible_number)
        return True
    except ValueError:
        return False

def get_response(message):
    """Prints message and returns the response"""
    print(message)
    return input()

def get_number_response(message):
    while True:
        response = get_response(message)
        if is_number(response):
            return float(response)

        print("Please enter in a valid number")

if __name__ == "__main__":
    #This is a utility file, so if it's ran as a program let's just run doctest
    import doctest
    doctest.testmod()
