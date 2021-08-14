'''
3x+1 Problem:
The 3x+1 problem, also known as the Collatz problem, the Syracuse problem, Kakutani's problem, Hasse's algorithm, and 
Ulam's problem, concerns the behavior of the iterates of the function which takes odd integers n to 3n+1 and even 
integers n to n/2. The 3x+1 Conjecture asserts that, starting from any positive integer n, repeated iteration of this 
function eventually produces the value 1.

Watch this to understand the problem and other terms: https://www.youtube.com/watch?v=094y1Z2wpJg


A simple Python program that takes a positive integer as input, then calculates the `highest value` and total 
`stopping time` of the integer of 3x+1.
'''


def main_problem(number: int):
    number_copy = number
    highest = 0
    stopping_time = 0
    while True:
        stopping_time += 1
        if number > highest:
            highest = number
        if number % 2 == 1:
            number = (number * 3) + 1
        else:
            number = number // 2
        if number == 1:
            break
    return number_copy, highest, stopping_time


def take_proper_input():
    try:
        number = round(abs(float(input('Enter number (Positive integer value only): '))))
        # If the number is float, it is rounded off to the nearest integer
        # If the number is negative, it gets converted to positive
        # 0 not accepted
        if number == 0:
            raise Exception
        return number
    except Exception:
        print('Invalid data type')
        input('Press enter to exit. ')
        quit()


if __name__ == '__main__':
    data = main_problem(take_proper_input())
    print(f'Number: {data[0]}\nHighest: {data[1]}\nStopping Time: {data[2]}')
    input('\n\nPress enter to exit. ')
    quit()
