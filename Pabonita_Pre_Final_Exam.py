print("Problem: A python program that displays all prime numbers within a range")


def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                return False
        return True


exit_program = False
while not exit_program:
    print("\n\n")
    while True:
        start = int(input("Enter a number [start]: "))
        if start < 0:
            print("Enter a non-negative number")
        elif start == 0:
            print("Program terminated")
            exit_program = True
            break
        else:
            break

    if exit_program:
        break
    while True:
        end = int(input("\nEnter a number [end] "))
        if end == 0:
            print("Program terminated")
            exit_program = True
            break
        elif end <= start:
            print("End must be greater than " + str(start))
        else:
            break
    if exit_program:
        break
    print("\nPrime numbers between " + str(start) + " and " + str(end) + " are: ", end=' ')
    for i in range(start, end + 1):
        if is_prime(i):
            print(i, end=' ')
