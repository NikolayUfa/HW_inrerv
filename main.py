class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def is_balanced_brackets(brackets):
    stack = Stack()
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for bracket in brackets:
        if bracket in opening_brackets:
            stack.push(bracket)
        elif bracket in closing_brackets:
            if stack.is_empty():
                return False
            elif closing_brackets.index(bracket) == opening_brackets.index(stack.peek()):
                stack.pop()
            else:
                return False

    return stack.is_empty()

balanced_examples = [
    "(((([{}]))))",
    "[([])((([[[]]])))]{()}",
    "{{[()]}}",
    "}{",
    "{{[(])]}}",
    "[[{())}]",
]

for example in balanced_examples:
    if is_balanced_brackets(example):
        print(f"{example} - Сбалансированно")
    else:
        print(f"{example} - Несбалансированно")



