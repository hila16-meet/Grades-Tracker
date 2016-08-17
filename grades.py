def average(grades_list):
    assert len(grades_list) > 0
    sum_grades = 0
    for i in grades_list:
        sum_grades = sum_grades + i
    return sum_grades / len(grades_list)

def show(grades_sheet):
    if len(grades_sheet) == 0:
        print('You have no grades.')
    else:
        for subject in sorted(grades_sheet.keys()):
            print(subject)
            g_list = grades_sheet[subject]
            for grade in g_list:
                print(grade)
            print("The average of all grades is: ", average(g_list))
            print("The highest grade is: ", max(g_list), " and the lowest is: ", min(g_list))

def save(grades_sheet, filename):
    """ (dict, str) -> none
    Saves the list of grades in the given file, one grade per line.
    """
    with open(filename, 'w') as file:
        for sub, grades in grades_sheet.items():
            file.write('*' + sub + '\n')
            for g in grades:
                file.write(str(g) + '\n')

def load(filename):
    """ (str) -> dict
    Returns list of grades loaded from file
    """
    grades_sheet = dict()
    g_list = []
    sub = 'default'
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        return arr
    for line in file:
        if line[0] == '*':
            sub = line[1:].strip()
            grades_sheet[sub] = []
        else:
            g_list = grades_sheet.get(sub)
            g_list.append(int(line))
    file.close()
    return grades_sheet

def main_grades():
    all_grades = load('/Users/hilaTal/somefile')
    command = input("What do you want to do? (add|show|quit|reset): ")
    while command != 'quit':
        if command == 'add':
            #TODO you need to get subject and grade, and insert into dict.
            sub = 'default'
            g = -1
            the_list = []
            while sub != 0:
                try:
                    sub = input("Enter subject: ")
                    g = int(input("Enter next grade: "))
                    if sub in all_grades:
                        the_list = all_grades.get(sub) #or all_grades[sub]
                        the_list.append(g)
                        all_grades[sub] = the_list
                    else:
                        the_list.append(g)
                        all_grades += {sub: the_list}
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
