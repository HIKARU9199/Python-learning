def run():
    # my_dict = {}

    # for D in range(1, 1001):
    #     if D / 2 !=0:
    #         my_dict[D] = D**0.5

    my_dict = {D: D**0.5 for D in range(1, 1001)}#if D / 2 !=0}
    print(my_dict)

if __name__ == "__main__":
    run()