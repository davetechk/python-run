def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    user_input = d.replace("$", "")
    return(float(user_input))

def percent_to_float(p):
    user_input = p.replace("%","")
    result = (int(user_input))/100
    return(float(result))


main()