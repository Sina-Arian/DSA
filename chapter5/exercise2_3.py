from Stack import Stack

'''2.Implement the inflix-to-postfix algorithm ...
3.Write a function that accepts a valid ...'''

def reverse_polish(infix): #infix is a list
    stack =Stack()
    postfix =[]
    PEMDAS = ['**', '*', '/', '+', '-']
    PEMDASPlus = PEMDAS + [')', '(']
    for token in infix:
        if token not in PEMDASPlus:
            postfix.append(token)

        elif token is '(':
            stack.push(token)
        
        elif token in PEMDAS:
            while (stack.size() != 0) and (stack.top() in PEMDAS) and (PEMDAS.index(token) <= PEMDAS.index(stack.top())):
                postfix.append(stack.pop())
            stack.push(token)

        else:
            while stack.top() != '(':
                postfix.append(stack.pop())
            stack.pop()

            while stack.size() != 0:
                postfix.append(stack.pop())

    while stack.size() != 0:
                postfix.append(stack.pop())

    res = ''.join(postfix)
    return res


def calculate(postfix):
    stack = Stack()
    PEMDAS = ['**', '*', '/', '+', '-']
    for ch in postfix:
        if ch not in PEMDAS:
            ch = int(ch)
            stack.push(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            if PEMDAS.index(ch) == 0:
                stack.push(b**a)
            elif PEMDAS.index(ch) == 1:
                stack.push(b*a)
            elif PEMDAS.index(ch) == 2:
                stack.push(b/a)
            elif PEMDAS.index(ch) == 3:
                stack.push(b+a)
            elif PEMDAS.index(ch) == 4:
                stack.push(b-a)
        print(stack.LIFO_stack)
    return stack.pop()

def parensBalance(s):
    stack = Stack()
    for ch in s:
        if ch in "([{":
            stack.push(ch)
        elif ch in ")]}":
            if stack.size() == 0:
                return False
            else:
                if stack.pop() + ch not in ['()', '[]', r'{}']:
                    return False
    return stack.size == 0
    
def main():
    inEx = input("Enter the experesion:\n")

    if parensBalance(inEx) is not True:
        print('parenthesis is not balanced')

    inEx2 = []
    for ch in inEx:
        if ch != ' ':
            inEx2.append(ch)
    postfix = reverse_polish(inEx2)
    print(postfix)
    res = calculate(postfix)
    print(res)

main()