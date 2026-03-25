# Task 3.3

my_list1 = [21, 22, 23, 34, 17, 20]
my_list2 = [7, 8, 9, 10, 11]
my_list3 = []

def split_list(lst):
    if not lst:
        return []
    mid = (len(lst) + 1) // 2
    return [lst[:mid], lst[mid:]]

print(split_list(my_list1))
print(split_list(my_list2))
print(split_list(my_list3))