
def multiplying(a: int, b:int) -> int:
    # your code
    pass


def area_of_rectangle(a: int, b: int) -> int:
    # your code
    pass


def area_of_box(a: int, b: int, c: int) -> int:
    return multiplying(area_of_rectangle(a=a, b=b), c)


assert area_of_box(1, 2, 3) == 6
