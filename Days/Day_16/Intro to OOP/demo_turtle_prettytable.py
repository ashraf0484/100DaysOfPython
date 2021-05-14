# from turtle import Turtle, Screen
#
# ashraf = Turtle()
# print(ashraf)
#
# print(ashraf.shape("turtle"))
# print(ashraf.color("red", "black"))
# print(ashraf.left(90))
#
# ashraf.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
# print()
from prettytable import *

table = PrettyTable()

# Column no.1
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"], "l")
print(table)

x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
x.align["City name"] = "l"
# Left align city names
x.padding_width = 1
# One space between column edges and contents (default)
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])
print(x)

print(x.get_string(sortby="Annual Rainfall", reversesort=True))

print()
x.set_style(PLAIN_COLUMNS)
print(x)
