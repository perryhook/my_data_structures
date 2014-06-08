from stack import Stack
from stack import EmptyStackError


def check_parens(str):
    """check_parens takes a string and:
        returns 0 if the number of parentheses is balanced and matched.
        returns 1 if more left parentheses than right.
        returns -1 if string has broken (unmatched) parentheses.
        """

    stack = Stack()
    for i in range(len(str)):
        if str[i] == '(':
            stack.push(i)
        elif str[i] == ')':
            try:
                stack.pop()
            except EmptyStackError:
                return -1
    try:
        stack.pop()
        return 1
    except EmptyStackError:
        return 0
