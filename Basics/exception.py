try:
    number = int(input("Enter the number: "))
    result = 10 / number
except ValueError:
    print("You put wrong data type! please put the number")
except ZeroDivisionError:
    print("You can't divide with 0")
except Exception as e:
    print(f"Something wrong! : {e}")
else:
    print(f"Result is: {result:.2f}")