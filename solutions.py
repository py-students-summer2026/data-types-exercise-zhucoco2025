"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    sales_input = input("Enter the projected amount of total sales: ")
    sales = float(sales_input)
    
    # Calculate 23% profit
    profit = sales * 0.23
    
    # Format to 2 decimal places
    print(f"Profit: ${profit:.2f}")


def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    num1 = int(input("Enter number #1: "))
    num2 = int(input("Enter number #2: "))
    
    # // is floor division (quotient), % is modulo (remainder)
    quotient = num1 // num2
    remainder = num1 % num2
    
    print(f"{num2} goes into {num1} a total of {quotient} times with a remainder of {remainder}")


def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 4.0
    """
    miles = float(input("Miles driven: "))
    gallons = float(input("Gas used (gallons): "))
    
    mpg = miles / gallons
    
    print(f"Miles per gallon: {mpg}")


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price1 = float(input("Enter price #1: "))
    price2 = float(input("Enter price #2: "))
    price3 = float(input("Enter price #3: "))
    
    print("\nHere are your prices!\n")
    
    # :>7.2f means: right-aligned (>), width of 7 characters total (including the decimal), and 2 decimal places (.2)
    # Adjust width to 7 so that 9532.60 takes 7 spaces, matching the sample output alignment perfectly.
    print(f"Price #1: $ {price1:>7.2f}")
    print(f"Price #2: $ {price2:>7.2f}")
    print(f"Price #3: $ {price3:>7.2f}")