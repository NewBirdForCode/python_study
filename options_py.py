

class FactoryCar():
    def __init__(self):
        pass


def get_input():
    return input().lower()


while True:
    input_str = get_input()
    print(input_str)
    if input_str == 'q':
        break

