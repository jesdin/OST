newStack = []
postfix = []

def isOperand(x):
    if x == '/' or x == '*' or x == '+' or x == '-' or x == '^':
        return True
    else:
        return False

def getPr(x):
    if x == '/' or x == '*':
        return 2
    elif x == '+' or x == '-':
        return 1
    elif x == '^':
        return 3
    return 0

def notGreater(x):
    y = newStack[len(newStack)-1]
    if getPr(x) <= getPr(y):
        return True
    else:
        return False

infix = "(" + input('Enter the infix expression: ') + ")"
for i in infix:
    if i == '(':
        newStack.append(i)   
    elif i.isalpha():
        postfix.append(i)  
    elif i == ')':
        while len(newStack)!=0 and newStack[len(newStack)-1] != '(':
            postfix.append(newStack.pop())
        newStack.pop()
    else:
        while isOperand(i) and len(newStack)!= 0 and notGreater(i):
            postfix.append(newStack.pop())
        newStack.append(i)
while len(newStack) != 0:
    postfix.append(newStack.pop())
            
print('PostFix: ',"".join(postfix))
        
        
        


