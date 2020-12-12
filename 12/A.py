import turtle

with open('input.txt') as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

command_map = {
    'N': lambda delta: turtle.sety(turtle.ycor() + delta),
    'S': lambda delta: turtle.sety(turtle.ycor() - delta),
    'E': lambda delta: turtle.setx(turtle.xcor() + delta),
    'W': lambda delta: turtle.setx(turtle.xcor() - delta),
    'L': turtle.left,
    'R': turtle.right,
    'F': turtle.forward
}

turtle.speed('fast')
for command, arg in instructions:
    command_map[command](arg)

print(abs(turtle.xcor()) + abs(turtle.ycor()))
turtle.exitonclick()
