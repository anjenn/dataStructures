class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()



# WRITE IS_BALANCED_PARENTHESES FUNCTION HERE #
#                                             #
#    This is a separate function that is      #
#    not a method within the Stack class.     #
#    Indent all the way to the left.          #
#                                             #
###############################################
def is_balanced_parentheses(checked_string):
    # if len(checked_string) < 0:
        # return False
    # if len(checked_string) == 0:
        # return True
    # if len(checked_string)%2 == 1:
        # return False
    # result = None
    # lparen = 0
    # rparen = 0
    # for i in range(int(len(checked_string)/2)):
        # if checked_string[i] == ')':
            # rparen+=1
        # if checked_string[i] == '(':
            # lparen+=1
        # if (checked_string[i] != checked_string[len(checked_string)-i-1]):
            # result = True
        # else:
            # result = False
    # if rparen > lparen:
        # return False
    # return result
    stack = Stack()
    for i in checked_string:
        if i == '(':
            stack.push(i)
        elif i == ')':
            if stack.is_empty() or stack.pop() != '(':
               return False
    return stack.is_empty()
        
        
        



def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

test_is_balanced_parentheses()
