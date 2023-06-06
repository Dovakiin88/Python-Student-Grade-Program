import math

# Functions

# Average function


def average(valid):
    addvalid = []

    for x in valid:
        addvalid.append(float(x[3]))

    total = sum(addvalid)
    avg = total/len(addvalid)
    a = math.ceil(avg)
    return f'The overall average grade for all students is {a}'


# Find average per program

def average_per_program(valid):
    program = input("Which Program? MSCM or MSIT: ")
    temp = []
    if program.upper() not in ['MSCM', 'MSIT']:
        raise ValueError('Please either input MSCM or MSIT. Please try again')

    try:
        for x in valid:
            if x[4] == program.upper():
                temp.append(float(x[3]))

        total = sum(temp)
        avg = total/len(temp)
        return f'The average grade for {program} is: {avg:.2f} or {math.ceil(avg)}%'

    except ValueError:
        print('Please either input MSCM or MSIT')


# Find highest grade


def highgrade(valid):
    temp = []

    for x in valid:
        temp.append(float(x[3]))

    mx = max(temp)

    return f'The highest grade of all student is: {mx}'

# Find lowest grade


def lowgrade(valid):
    temp = []

    for x in valid:
        temp.append(float(x[3]))
    mn = min(temp)

    return f'The lowest grade of all students is: {mn}'

# Displays students associated with a particular program


def students_per_program(valid):
    program = "MSIT"  # input('Which program? ')
    temp = []
    for x in valid:
        if x[4] == program:
            temp.append(x)
    for y in temp:
        print(f'{y[1]} {y[2]}')
    return f'These are the students assiciated with program {program}'


def students_per_program1(valid):
    program = "MSCM"  # input('Which program? ')
    temp = []
    for x in valid:
        if x[4] == program:
            temp.append(x)
    for y in temp:
        print(f'{y[1]} {y[2]}')
    return f'These are the students assiciated with program {program}'

# display sorted list of students by id


def students(valid):
    valid.sort(key=lambda valid: int(valid[0]))
    for x in valid:
        print(f'ID:{x[0]} Name:{x[1]} {x[2]}')
    return f'The above listed are students sored by ID'


# Create new file with invalid records called BADRECORDS.TXT

def createNewFileWithInvalidRecords():
    try:
        f = open("BADRECORDS.txt", 'w+')

        for x in bad_records:
            f.write(str(x))  # items must be in string form!

        f.close()
        print("BADRECORDS.TXT has been created.")
        return "Process complete"
    except FileExistsError:
        print('File already exists')

# Display all invalid records


def displayInvalidRecords():
    for x in bad_records:
        print(
            f'ID: {x[0]} First Name: {x[1]} Last Name: {x[2]} Grade: {x[3]} Program: {x[4]}')
    return f'Records returned'


# Lists
bad_records = []
valid = []


def main():
    # Primary sorting

    print('Welcome. Please input a file to be pocessed')
    file_to_be_processed = input("Enter file name here: ")
    print()

    with open(file_to_be_processed, 'r+') as file:
        f = file.read()

    lines = f.split('\n')
    temp = [line.split(',')for line in lines]

    # Sorted into valid and invalid records
    for x in temp:
        if x[2] == '' or float(x[3]) > 100 or x[1] == '' or len(x[2]) > 10 or len(x[1]) > 10 or x[4] == 'BSIT':
            bad_records.append(x)
        else:
            valid.append(x)

    while True:

        # Display Main Menu options

        print("1. Display average grade for all students")
        print("2. Display average grade for each program")
        print("3. Display Highest grade record")
        print("4. Display Lowest grade record")
        print("5. Display students in MSIT")
        print("6. Display students in MSCM")
        print("7. Display all students in sorted order by Student ID")
        print("8. Display Invalid records")
        print("9. Create new file with invalid records")
        print("0. Exit")

        # Get input from user
        zinput = input("Make selection: ")
        # to ensure that the user inputs a single digit
        zinput = zinput[:1]

        # options
        if zinput == "1":
            print('Running function: Average Grade for all students')
            print()
            print(average(valid))
            print()

        elif zinput == "2":
            print('Running function: Average grade for each program')
            print()
            print(average_per_program(valid))
            print()

        elif zinput == "3":
            print('Running function: Highest grade record')
            print()
            print(highgrade(valid))
            print()

        elif zinput == "4":
            print('Running function: Lowest grade record')
            print()
            print(lowgrade(valid))
            print()

        elif zinput == "5":
            print('Running function: Display students in MSIT')
            print()
            print(students_per_program(valid))
            print()

        elif zinput == "6":
            print('Running function: Display students in MSCM')
            print()
            print(students_per_program1(valid))
            print()

        elif zinput == "7":
            print('Running function: Students in sorted order by Student ID')
            print()
            print(students(valid))
            print()

        elif zinput == "8":
            print('Running function: Display Invalid records')
            print()
            print(displayInvalidRecords())
            print()

        elif zinput == "9":
            print('Running function: Create new file with invalid records')
            print()
            print(createNewFileWithInvalidRecords())
            print()

        # Exit program
        elif zinput == "0":
            print()
            print('Exiting')
            print()
            break

        # Invalid choice
        else:
            if zinput not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                print('Invalid Selection')

    # End of program
    print('Thank you for using our program. Goodbye!')


main()

