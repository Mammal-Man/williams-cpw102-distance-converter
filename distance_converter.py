
def main():
    print("Welcome to the Distance Converter!\nI am going to ask for your measured distance in miles, feet, and inches and return the value to you in inches.")
    ToInches()
    print("\nNow, we will convert inches to miles, feet, and inches.")
    ToLargestUnits()
    
def ToInches():
    miles = float(input("Input miles: "))
    feet = float(input("Input feet: "))
    inches = float(input("Input inches: "))
    totalInches = (miles * 63360) + (feet * 12) + inches
    print(f"{miles} miles, {feet} feet, and {inches} inches is {totalInches} inches")

def ToLargestUnits():
    inches = float(input("Input inches: "))
    miles = inches // 63360
    feet = (inches % 63360) // 12
    leftoverInches = inches % 12
    print(f"{inches} inches is {miles} miles, {feet} feet, {leftoverInches} inches")

main()