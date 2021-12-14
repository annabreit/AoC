test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

def follow_command(current_horizontal, current_depth, command, value):
    if command =="down":
        current_depth += value
    elif command == "up":
        current_depth -= value
    elif command == "forward":
        current_horizontal += value
    else:
        raise ValueError
    return current_horizontal, current_depth

def follow_correcred_command(current_aim, current_horizontal, current_depth, command, value):
    if command =="down":
        current_aim += value
    elif command == "up":
        current_aim -= value
    elif command == "forward":
        current_horizontal += value
        current_depth += current_aim*value
    else:
        raise ValueError
    return current_aim, current_horizontal, current_depth


if __name__ == '__main__':
    #lines = test_input.split("\n")
    with open("input2.txt", "r") as f:
        lines = f.read().split("\n")
    command_tuples = [(line.split()[0], int(line.split()[1])) for line in lines]

    current_horizontal = current_depth = 0

    for command, value in command_tuples:
        current_horizontal, current_depth = follow_command(current_horizontal, current_depth, command, value)

    print(current_horizontal, current_depth)
    print(current_horizontal * current_depth)

    current_aim= current_horizontal = current_depth = 0

    for command, value in command_tuples:
        current_aim, current_horizontal, current_depth = follow_correcred_command(current_aim, current_horizontal, current_depth, command, value)

    print(current_horizontal, current_depth)
    print(current_horizontal * current_depth)

