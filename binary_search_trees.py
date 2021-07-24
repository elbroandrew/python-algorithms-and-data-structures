def build_bst(my_list):
    if len(my_list) == 0:
        return "No Child"

    # середина списка с округлением вниз
    middle_idx = len(my_list)//2

    middle_value = my_list[middle_idx]

    print(f"Middle index: {middle_idx}")
    print("Middle value: " + str(middle_value))
