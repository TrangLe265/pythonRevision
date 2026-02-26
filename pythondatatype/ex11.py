"""
Write a function to combine two lists
Write a function named combine_lists that accepts two lists of integers as parameters. Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number). Your function should return a list that combines the two lists and at the same time is itself also sorted. To be clear all elements of the input lists should be in the output list and len(input_list1)+len(input_list2) == len(output_list). Notice that your function should return the list, not print it.

You can use whatever you want as the name of the parameters. You don't need to use any special function or functionality to complete the task. Specially don't use any kind of sorting function of lists or Python in general. Just normal Python list actions are enough for this task. Iterate over the lists adding one by one the the smallest of the remaining elements of the two lists. When one of the lists have been exhausted, you can just add the remaining elements of the other list to the output list.
"""
def combine_lists(list_1,list_2):
    combined = []

    # account for cases where lists are both empty
    if (len(list_1) == 0 and len(list_2) == 0): 
        return combined
    
    i = 0
    j = 0
    
    # use 2 pointers, start by comparing number one by one
    # append the smaller number to the combined list 
    # increase the counter on the list that the smaller number is from
    # continue compare the larger number in the next loop to the next number of the other list
    while i < len(list_1) and j < len(list_2):
        if list_1[i] < list_2[j]:
            combined.append(list_1[i])
            i += 1
        else: 
            combined.append(list_2[j])
            j += 1

    # add any remaining elements
    combined += list_1[i:]
    combined += list_2[j:]

    return combined

print(combine_lists([3], [1, 2, 3, 4, 5]))
