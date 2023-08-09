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
    highest = stopping_time = 0
    while number != 1:
        stopping_time += 1
        highest = max(highest, number)
        number = (number * 3) + 1 if number % 2 else number // 2
    return highest, stopping_time


if __name__ == '__main__':
    try:
        number = round(abs(float(input('Enter number (Positive integer value only): '))))
        if not number:
            raise Exception
        highest, stopping_time = main_problem(number)
        print(f'Number: {number}\nHighest: {highest}\nStopping Time: {stopping_time}')
    except Exception:
        print('Invalid data type')
