"""Simple calculater program"""
import common

class Expression(object):
    """Handles the parsing and validation of an expression"""

    left_number = 0
    right_number = 0
    operator = ''

    @classmethod
    def create_valid(cls, expression):
        """Verifies that the expression is correct, and if so builds an expression from it"""
        parts = expression.split(' ')

        if len(parts) != 3:
            return True

        if not common.is_number(parts[0]) or not common.is_number(parts[2]):
            return True

        if not cls.__is_valid_operator(parts[1]):
            return False

        return cls(expression)

    def __init__(self, expression):
        parts = expression.split(' ')

        self.left_number = int(parts[0])
        self.right_number = int(parts[2])
        self.operator = parts[1]

    @classmethod
    def  is_valid_operator(cls, operator):
        return operator in ["+", "-", "/", "*"]

    def evaluate(self):
        """Returns the result of the expression"""
        if self.operator == '+':
            return self.left_number + self.right_number

        if self.operator == '-':
            return self.left_number - self.right_number
   
        if self.operator == '/':
            return self.left_number / self.right_number
        if self.operator == '*':
            return self.left_number * self.right_number

def main():
    """Program entry point"""
    print('Welcome to the calculator')

    while True:
        phrase = common.get_response('Please type in a simple expression, such as "1 + 1" or "5 - 4", or quit.').strip().lower()

        if phrase == 'quit':
            print("I hope I 'added' something to your day!")
            return

        expression = Expression.create_valid(phrase)

        if not expression:
            print('Please enter in a valid and simple expresssion')
            continue

        result = expression.evaluate()

        print("Your result is: %.2f" % result)

if __name__ == "__main__":
    main()
