def print_positive_numbers(input_list, list_name):
    positive_numbers = [num for num in input_list if num > 0]
    print(f"Input: {list_name} = {input_list}")
    if list_name == "list1":
        print("Output:", ", ".join(map(str, positive_numbers)))
    else:
        print("Output:", positive_numbers)
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]
print_positive_numbers(list1, "list1")
print_positive_numbers(list2, "list2")
