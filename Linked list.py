def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Take user input for the first sorted list
list1 = list(map(int, input("Enter the first sorted list (space-separated): ").split()))

# Take user input for the second sorted list
list2 = list(map(int, input("Enter the second sorted list (space-separated): ").split()))

merged_list = merge_sorted_lists(list1, list2)

print(f"Merged Sorted List: {merged_list}")
