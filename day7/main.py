def get_directories(file):

    directories = []

    with open(file, "r") as f:
        for idx, line in enumerate(f.readlines()):
            entry = line.split()
            print(idx, entry)

            if entry[1] == 'cd':
                print(entry[1], entry[2])
                current_dir = entry[2]
                if current_dir.isalpha():
                    count_size(file, idx, current_dir)


def count_size(file, idx, current_dir):
    values = []
    with open(file, "r") as f:
        input = f.read().splitlines()
        for i in input[idx:]:
            size = i.split()[0]
            if '$' in size:
                break
            elif 'dir' in size:
                values.append(i.split()[1])
            else:
                values.append(i.split()[0])
        return values

        # file = f.read().splitlines()[idx]
        # file_size = int(file.split()[0])
        print(input)

if __name__ == "__main__":

    print(count_size('test.txt', 3, 'a'))
    # get_directories('test.txt')
