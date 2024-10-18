list_of_sublists = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]

def print_list():
    filtered_sublists = []

    for sublist in list_of_sublists:
        if sublist[0] != 0:
            new_sublist = [item for item in sublist if item != 0]
            filtered_sublists.append(new_sublist)
        else:
            filtered_sublists.append([])

    return filtered_sublists

def list_to_dict(items_list):
    keys = ["A", "B", "C", "D"]

    my_dict = {keys[key]: items_list[key] for key in range(len(keys))}

    return my_dict

def run():
    print(f"La lista original es: {list_of_sublists}")
    new_list = print_list()
    print(f"La nueva lista es: {new_list}")
    new_dict = list_to_dict(new_list)
    print(f"El nuevo diccionario es: {new_dict}")

if __name__ == "__main__":
    run()