import turtle
from math import sqrt

with open('input.txt') as f:
    instructions = [(line[0], int(line[1:])) for line in f.readlines()]

waypoint = turtle.Turtle()
waypoint.setposition(10, 1)
waypoint.speed('fastest')
waypoint.color('red')
waypoint.shape('circle')
ship = turtle.Turtle()
ship.speed('fastest')


def get_deltas():
    return waypoint.xcor() - ship.xcor(), waypoint.ycor() - ship.ycor()


def get_delta():
    x, y = get_deltas()
    return sqrt(x**2 + y**2)


move_waypoint = {
    'N': lambda delta: waypoint.sety(waypoint.ycor() + delta),
    'S': lambda delta: waypoint.sety(waypoint.ycor() - delta),
    'E': lambda delta: waypoint.setx(waypoint.xcor() + delta),
    'W': lambda delta: waypoint.setx(waypoint.xcor() - delta),
}

for command, arg in instructions:
    if command == 'F':
        delta_x, delta_y = get_deltas()
        for obj in [ship, waypoint]:
            obj.setposition(obj.xcor() + arg * delta_x, obj.ycor() + arg * delta_y)
    elif command in ['L', 'R']:
        delta = get_delta()
        waypoint.setheading(waypoint.towards(ship))
        waypoint.forward(delta)
        waypoint.left(180 - arg) if command == 'R' else waypoint.right(180 - arg)
        waypoint.forward(delta)
    else:
        move_waypoint[command](arg)
    print(f'{command}, {arg} => ship: {ship.pos()}, waypoint: {waypoint.pos()}')

print(abs(ship.xcor()) + abs(ship.ycor()))
turtle.exitonclick()
