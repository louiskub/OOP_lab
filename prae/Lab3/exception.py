x = 1
y = 0
try :
    print(x/y)
    print("Hello World")
except NameError:
    print("Variable x is not defined")
except ZeroDivisionError:
    print("Zero is not a good idea.")
except SyntaxError:
    print("Syntax Error")
except:
    print("Something else went wrong")
else:
    print("Nothing went wrong")
finally:
    print("Always run this code.")