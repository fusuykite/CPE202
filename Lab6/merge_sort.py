# list -> none
# merge sort the given list
def merge_sort(lst):
    merge_sort_helper(lst, 0, len(lst), [None] * len(lst)) #0 start and len is where to stop


# list int int list -> none
# merge sort a segment of the given list
def merge_sort_helper(lst, left, right, temp_array): # merge sort list only including left and not including right -> one bigger
    if right - left > 1:  # function mutates we dont need if else
        # do the merge sort
        mid = (left + right) // 2
        merge_sort_helper(lst, left, mid, temp_array)
        merge_sort_helper(lst, mid, right, temp_array)

        merge(lst, mid, right, temp_array)


# list int int int list -> None
# merge the two halves together
def merge(lst, start, mid, end, temp_array):
    left = start
    right = mid

    for index in range(start, end):
        if left < mid and (right >= end) or lst[left] < lst[right]:  # pick the left value
            temp_array[index] = lst[left]  # left does left of list, right is right of list
            left += 1
        else:
            temp_array[index] = lst[right]
            right += 1

    for index in range(start, end):
        lst[index] = temp_array[index]  # copy and mutate original list

