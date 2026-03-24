# Task 3.2

my_list = [1, 3, 4, 7]

def move_last_to_first(lst):
    if len(lst) > 1:
        lst.insert(0, lst.pop())
    return lst

move_last_to_first(my_list)

print(my_list)