

# print('what is __name__:', __name__)


def count_words(input_str):
    new_str = input_str.split(' ')
    return len(new_str)


def count_alpha(input_str):
    result_counter = {}
    for i in input_str:
        if i in result_counter:
            continue

        if i.isalpha():
            result_counter[i] = input_str.count(i)

    return result_counter


def charge_num():
    while True:
        input_str = input('input a num:')

        if input_str.strip().lower() == 'q':
            break

        if not input_str.isalnum():
            continue

        ori_num = input_str
        invert_num = input_str[::-1]
        print(ori_num == invert_num)


def main():
    print(__name__)
    test_str = 'hello world, Tom'
    print(count_words(test_str))

    counter = count_alpha(test_str)
    for i in counter:
        print(i, counter[i])

    charge_num()

# print("I'm a reboot")

# main()


if __name__ == '__main__':
    main()