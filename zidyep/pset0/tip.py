def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dolls = d.replace("$", "")

    return(float(dolls))


def percent_to_float(p):
    per = p.replace("%", "")

    result = int(per) / 100


    return(float(result))


main()