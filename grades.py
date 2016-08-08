def average(all_grades):
    sum_grades = 0
    count = 0
    for i in all_grades:
        sum_grades = sum_grades + i
        count += 1
    return sum_grades / count

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
    command = input("What do you want to do? (add|show|quit): ")
    while command != 'quit':
        if command == 'add':
            g = int(input("Enter first grade: "))
            all_grades = []
            while g != -1:
                all_grades.append(g)
                g = int(input("Enter next grade: "))
            save(all_grades, "/Users/hilaTal/somefile")
        elif command == 'show':
            print("The grades are: ", load("/Users/hilaTal/somefile"))
            print("The average of all grades is: ", average(all_grades))
            print("The most high grade is: ", max(all_grades), " and the lower is: ", min(all_grades))
        else:
            print('This is not a valid input!')
        command = input("What do you want to do? (add|show|quit): ")

    save(all_grades, "/Users/hilaTal/somefile")


if __name__ == '__main__':
    main_grades()
