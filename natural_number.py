def run():
#     num_list = {}

#     for l in range (1, 101):
#         if l % 3 !=0:9
#          num_list[l] = l**3
    


    num_list = {i: i**3 for i in range(1, 101)if i % 3 != 0}

    print(num_list)



if __name__ == "__main__":
    run()

