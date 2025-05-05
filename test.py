def print_pyramid(amount):
    print("*" * amount)
    _print_pyramid(amount - 2, 1)

def _print_pyramid(amount, spaces):

    if amount > 0:
        print(" " * spaces + "*" *amount)
        _print_pyramid(amount - 2, spaces + 1)


def print_tree(height):
    if height > 0:
        _print_tree(height, 1)
        if height > 10:
            print("]\n]")
        else:
            print("]")

def _print_tree(max, height):
    if height <= max:
        print("*" * height)
        _print_tree(max, height + 1)
    

print_pyramid(11)