def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name, l_name

first_name = input("Enter your first name: ")
second_name = input("Enter your second name: ")

print(format_name(first_name, second_name))
