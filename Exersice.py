def run():
    # my_dict = {}

    # for i in range(1, 1001):
    #     if i % 3 !=0:
    #          my_dict[i] = i**0.5
    # print(my_dict)
    
 #Segundo ejercicio ------ #2
    # my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # squares = [i**2 for i in my_list]
    # print(squares)

                     # USO CON MAP
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares= list(map(lambda x: x**2, my_list))
# print(squares)
                 #Reduce'
        # my_list = [2, 2, 2, 2, 2, 2]

        # all_multiplied = 1

        # for i in my_list:
        #      all_multiplied = all_multiplied * i

        # print(all_multiplied)

 #uso con 'reduce'
        from functools import reduce
        my_list = [2, 2, 2, 2, 2, 2]
        all_multiplied = reduce (lambda a, b: a * b, my_list)
        print(all_multiplied)


if __name__ == '__main__':
    run()