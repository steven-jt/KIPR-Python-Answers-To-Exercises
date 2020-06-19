import math

def update(dict, l_sys_str):
    new_str = ""
    for char in l_sys_str:
        if char in dict:
            new_str += dict[char]
        else:
            new_str += char
    return new_str

def iterate(dictionary, n):
    k0 = dict(dictionary)['start']
    k1 = k0
    if n >= 0:
        for i in range(n):
            k1 = update(dictionary, k1)
    return k1

def lsystemToDrawingCommands(dict, l_sys_str):
    commands = []
    for c in l_sys_str:
        commands.append(dict[c])
    return commands

def nextLocation(x, y, curr_direction, drawing_command):
    str_com = str(drawing_command).split(" ")
    action = str_com[0]
    magnitude = int(str_com[1])
    if action == 'L' or action == 'R':
        if action == 'L':
            curr_direction = (curr_direction + magnitude) % 360
        else:
            curr_direction = (curr_direction - magnitude) % 360
    else:
        angle_in_rad = curr_direction * math.pi / 180
        x += math.cos(angle_in_rad) * magnitude
        y += math.sin(angle_in_rad) * magnitude
    return x, y, curr_direction

def bounds(commands):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    x = y = direction = 0
    for command in commands:
        x, y, direction = nextLocation(x, y, direction, command)
        if x < x_min:
            x_min = x
        elif x > x_max:
            x_max = x
        if y < y_min:
            y_min = y
        elif y > y_max:
            y_max = y
    return x_min, x_max, y_min, y_max
