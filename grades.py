def average(grades_list):
    assert len(grades_list) > 0
    sum_grades = 0
    for i in grades_list:
        sum_grades = sum_grades + i
    return sum_grades / len(grades_list)

def show(grades_list):
    if len(grades_list) == 0:
        print('You have no grades.')
    else:
        print("The grades are: ", grades_list)
        print("The average of all grades is: ", average(grades_list))
        print("The highest grade is: ", max(grades_list), " and the lowest is: ", min(grades_list))


def save(grades_list, filename):
    """ (list, str) -> none
    Saves the list of grades in the given file, one grade per line.
    """
    with open(filename, 'w') as file:
        for grade in grades_list:
            file.write(str(grade) + '\n')

def load(filename):
    """ (str) -> list
    Returns list of grades loaded from file
    """
    arr = []
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return arr
    for line in file:
        arr.append(int(line))
    file.close()
    return arr

def main_grades():
    all_grades = load('/Users/hilaTal/somefile')
    command = input("What do you want to do? (add|show|quit|reset): ")
    while command != 'quit':
        if command == 'add':
            g = 0
            while g != -1:
                try:
                    g = int(input("Enter next grade: "))
                    if g != -1:
                        all_grades.append(g)
                except ValueError:
                    print('Invalid input!')

        elif command == 'show':
            show(all_grades)
        elif command == 'reset':
            all_grades = []
        else:
            print('This is not a valid input!')
        command = input("What do you want to do? (add|show|quit|reset): ")

    save(all_grades, "/Users/hilaTal/somefile")


if __name__ == '__main__':
    main_grades()
