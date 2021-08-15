def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname" : "Carlos", "Lastname":"Botero"}

    super_list =[
        {"firstname" : "Carlos", "Lastname":"Botero"},
        {"firstname" : "Juan", "Lastname":"Valencia"},
        {"firstname" : "Carolina", "Lastname":"Forero"},
        {"firstname" : "Daniel", "Lastname":"Velasquez"},
        {"firstname" : "luisa", "Lastname":"Lopez"},
        {"firstname": "Miguel", "lastname": "Rodriguez"},
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-3, -2, -1, 0, 1, 2],
        "floating_nums": [1.1, 4.55, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)   


if __name__== '__main__':
    run()
