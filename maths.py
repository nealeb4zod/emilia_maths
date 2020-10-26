import cowsay

from random import randint
from sum import Sum
from os import system


def clear():
    system("clear")


def add(number_1, number_2):
    return number_1 + number_2


def subtract(number_1, number_2):
    return number_1 - number_2


def multiply(number_1, number_2):
    return number_1 * number_2


def input_sum_choice():
    clear()
    a = """
    What kind of sums would you like?
    1. Adding
    2. Subtracting
    3. Multiplying
    4. A mixture
    """
    print(a)
    sum_choice = int(input("Enter 1, 2, 3 or 4: "))
    return sum_choice


def get_sum_type(sum_choice):
    if sum_choice == 1:
        sum_type = "+"
        return sum_type
    elif sum_choice == 2:
        sum_type = "-"
        return sum_type
    else:
        sum_type = "x"
        return sum_type


def create_addition_subtraction(sum_type):
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    if sum_type == 1:
        sum_answer = add(number_1, number_2)
    else:
        if number_1 >= number_2:
            sum_answer = subtract(number_1, number_2)
        else:
            sum_answer = subtract(number_2, number_1)
            sum = Sum(number_2, number_1, sum_type, sum_answer)
            return sum
    sum = Sum(number_1, number_2, sum_type, sum_answer)
    return sum


def create_multiplication(sum_type):
    number_1 = randint(1, 10)
    number_2 = randint(1, 10)
    sum_answer = multiply(number_1, number_2)
    sum = Sum(number_1, number_2, sum_type, sum_answer)
    return sum


def get_sum_list(sum_type):
    if sum_type == 4:
        random_list = [randint(1, 3) for iteration in range(10)]
        return get_list_of_sums(random_list)
    else:
        same_list = [sum_type for i in range(10)]
        return get_list_of_sums(same_list)


def get_list_of_sums(list_of_sum_types):
    list_of_sums = []
    for sum_type in list_of_sum_types:
        if sum_type == 1 or 2:
            list_of_sums.append(create_addition_subtraction(sum_type))
        elif sum_type == 3:
            list_of_sums.append(create_multiplication(sum_type))
    return list_of_sums


def ask_questions(list_of_sums):
    answered_questions = []
    for sum in list_of_sums:
        clear()
        maths_symbol = get_sum_type(sum.sum_type)
        formatted_sum = f"{sum.number_1} {maths_symbol} {sum.number_2} = ?"
        cowsay.cow(formatted_sum)
        user_answer = input("Please enter your answer: ")
        sum.user_answer = user_answer
        answered_questions.append(sum)
    return answered_questions


def print_completed_sum_list(list_of_completed_sums):
    for sum in list_of_completed_sums:
        maths_symbol = get_sum_type(sum.sum_type)
        formatted_sum = f"{sum.number_1} {maths_symbol} {sum.number_2} = {sum.sum_answer}  Your answer: {sum.user_answer}"
        print(formatted_sum)


def display_results(answered_questions):
    clear()
    right_answers = []
    wrong_answers = []
    for sum in answered_questions:
        if sum.user_answer == str(sum.sum_answer):
            right_answers.append(sum)
        else:
            wrong_answers.append(sum)
    no_of_right_answers = len(right_answers)
    print(f"You got {no_of_right_answers} out of 10!\n")
    if len(right_answers) > 0:
        print("Right Answers:\n")
        print_completed_sum_list(right_answers)
    if len(wrong_answers) > 0:
        print("\nWrong Answers:\n")
        print_completed_sum_list(wrong_answers)


def main():
    sum_choice = input_sum_choice()
    list_of_sums = get_sum_list(sum_choice)
    list_of_answers = ask_questions(list_of_sums)
    display_results(list_of_answers)


if __name__ == "__main__":
    main()
