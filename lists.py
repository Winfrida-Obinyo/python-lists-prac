#  Given two lists, write a function to find the 
# common elements between them and return them in a new list.

def common_elements(list1,list2):
    empty_element = []
    for elements in list1:
        if elements in list2 and  elements not in empty_element:
            empty_element.append(elements)
    return empty_element
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = common_elements(list1, list2)
print(common_elements)

# Given a list of integers, write a function that 
# returns the smallest element in the list.

def find_smallest(numbers):
    smallest = numbers[0]  
    
    for num in numbers:
        if num < smallest:
            smallest = num
    
    return smallest
numbers = (30,40,56,2,65)
find_smallest=find_smallest(numbers)
print(find_smallest)

# Write a Python function to reverse a list of integers in 
# place (i.e., without creating a new list).

def reverse_list(numbers):
    print(numbers.reverse())
    # start, end = 0, len(numbers) - 1
    # while start < end:
    #     numbers[start], numbers[end] = numbers[end], numbers[start]
    #     start += 1
    #     end -= 1
# numbers = ([4,7,8,10,1,3])
reverse_list([4,7,8,10,1,3])
# print(reverse_list)

# Write a function to remove all duplicates from a list.        
        
def remove_duplicates(lst):
    seen = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen:
            lst.pop(i)
        else:
            seen.add(lst[i])
            i += 1
                    