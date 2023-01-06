def get_instructions(file):
    with open(file, "r") as f:
        lines = f.readlines()
        sep = lines.index('\n')
        # drawing = [strip_symbols(item) for item in lines[:sep-1]]
        drawing = lines[:sep-1]
        max_containers = int(len(max(drawing, key=len))/6)
        # procedure = [strip_letters(item) for item in lines[sep+1:]]
        # return drawing, procedure
        return drawing, max_containers


def strip_letters(list_input):
    return ''.join(i for i in list_input if i.isdigit())


def strip_symbols(list_input):
    return ''.join(i for i in list_input if i.isalpha())


def move_cranes(drawing, procedure):
    stacks = len(drawing[0].strip())
    for operation in procedure:
        move, to_stack, from_stack = int(operation[0]), int(operation[1]), int(operation[2])
        print(drawing)



if __name__ == "__main__":
    drawing, max_containers = get_instructions('test.txt')
    print(max_containers)
    # drawing, procedure = get_instructions('test.txt')
    # print(drawing)
    # print(procedure)
    # print(move_cranes(drawing, procedure))
