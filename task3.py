def is_self_dividing(number):
    number_to_string = str(number)
    length = len(number_to_string)
    for i in range(length):
        digit = int(number_to_string[i])
        if digit == 0:
            return False
        if (number % digit != 0):
            return False
    return True


def rang(left, right):
    answer = []
    for each in range(left, right + 1, 1):
        if is_self_dividing(each):
            answer.append(each)
    return answer


if __name__ == '__main__':
    print(rang(int(input("left = ")), int(input("right = "))))
