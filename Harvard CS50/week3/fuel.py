

def main():
    fuel_amount  = fraction_input("Fraction? ")
    
    if fuel_amount <= 1:
        print("E")
    elif fuel_amount >= 99:
        print("F")
    else:
        print(f"{fuel_amount}%")


def fraction_input(prompt):

    while True:
        try:
            # get input from the user
            fuel_fraction = input(prompt)
            
            # divides input 'fuel_fraction' into 2 different variables - 'x' and 'y'
            x, y = fuel_fraction.split('/')

            # Converts 'x' and 'y' to integers
            x = int(x)
            y = int(y)

            # Converts fuel amount into integer number and rounds it up
            fuel_amount = round(x / y * 100)

            # Check if fuel_amount is greater than 100
            if fuel_amount > 100:
                print("Above full tank")
                continue

        except ValueError:
            print("This isnt a fraction")
        except ZeroDivisionError:
            print("Cant divide by 0")
        else:
            return fuel_amount
        

main()