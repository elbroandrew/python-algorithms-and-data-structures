def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    # середина списка с округлением вниз
    middle_idx = len(my_list)//2

    middle_value = my_list[middle_idx]

    print(f"Middle index: {middle_idx}")
    print("Middle value: " + str(middle_value))

    # создаю ноду дерева с срединным значением
    tree_node = {"data" : middle_value}

    # создаю левую и правую ноды рекурсивно
    tree_node["left_child"] = build_bst(my_list[:middle_idx])  # исключает середину
    tree_node["right_child"] = build_bst(my_list[middle_idx + 1:])  # исключает середину

    return tree_node


# только сортированный массив использую
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

