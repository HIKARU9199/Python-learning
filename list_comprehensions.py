from typing import Sequence


def run():
    squares = []
    # for i in range(1, 100):
    #     if i % 3 != 0:
    #       squares.append(i**2)

    #squares = [i**2 for i in range(1, 101)if i % 3 != 0]
    
    # ejercicio
    squares = [i for i in range(1, 10000)if i % 4 ==0 and i % 6 == 0 and i % 9 == 0]

    # # squares = []
    # # for i in range(1, 100000):
    # #     if i % 4 !=0:
    # #         squares.append(i**2)


    print(squares)


if __name__ == "__main__":
    run()