from typing import List


def evaluate(operators: List[str]):
    stack = []
    for operator in operators:
        if operator == "+":
            stack.append(stack.pop() + stack.pop())
        elif operator == "*":
            stack.append(stack.pop() * stack.pop())
        elif operator == "-":
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif operator == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(b / a)
        else:
            stack.append(int(operator))

    return stack.pop()
