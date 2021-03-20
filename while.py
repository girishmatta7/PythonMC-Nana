def days_to_hours(num_of_days):
    return "{} days is {} hours!".format(num_of_days, (num_of_days * 24))


def validate_and_execute():
    "validate the input and execute the other function"
    try:
        user_input_num = int(num_of_days_element)
        if user_input_num > 0:
            print(days_to_hours(user_input_num))
        elif user_input_num == 0:
            print("You have entered 0. Please enter a posite number!")
        else:
            print("You have entered a negetive number. Please enter a positive number")
    except ValueError:
        print("You have entered an invalid number. Please enter a positive number!")


user_input = ""
while user_input != "exit":
    user_input = input(
        "Enter the number of days in a comma seperate list and you will get the number of hours: \n")
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):
        validate_and_execute()
