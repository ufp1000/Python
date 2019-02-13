def divide(a,b):
    try:
        return(a/b)
    except ZeroDivisionError:
        return "Cannot divide by Zero1"
    except:
        return "Cannot divide by Zero2"


a = int(input("Enter numberator"))
b = int(input("Enter denomiator"))
print(divide(a,b))
