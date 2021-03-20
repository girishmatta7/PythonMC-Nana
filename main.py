print("10 days are " + str(240) + " hours")
print(f"10 days are {240} hours")
to_hours = 10 * 24
print("10 days are {} hours".format(10 * 24))
print("10 days are {} hours".format(to_hours))
print(type(to_hours))

# functions

calculation_to_units = 24
name_of_unit = "hours"


def days_to_hours(num_of_days, sample_text):
    print("{} days are {} {}. ".format(num_of_days,
          num_of_days * calculation_to_units, name_of_unit))
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(f"{sample_text}")


days_to_hours(20, "This is all good!")

# User inputs

user_input = input("Enter your name: ").title()
print(user_input)
