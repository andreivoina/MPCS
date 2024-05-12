import random
import time

# Start the timer to get the execution time
start_time = time.time()

# Generate a random list
list = random.sample(range(-2000000000, 2000000000), 10000)


def bubblesort(list):
    # Traverse through the list
    for i in range(len(list)):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, len(list)-i-1):
            # Traverse the list from the first element to n-i-1
            # Swap if left_element > right_element

            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swapped = True
        if not swapped:
            break
    return list

def insertionsort(list):
    # Traverse through the list excluding the first element
    for i in range(1, len(list)):
        aux = list[i]

        # Move the elements of list[0...i-1] to one
        # position ahead of their current position
        j = i - 1
        while j >= 0 and aux < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = aux
    return list

def mergesort(list):
    if len(list) > 1:
        # Split the array in two halves
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]

        # Recursively sort each half
        mergesort(left)
        mergesort(right)

        i = j = k = 0
        # Merge the temporary arrays back into the final array
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements of left[]
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        # Copy the remaining elements of right[]
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

    return list


# Partition function for Quick Sort
def partition(list, left, right):

    # Select the rightmost element as the pivot
    pivot = list[right]

    # Store the position of the greater element
    i = left - 1

    # Traverse through the elements
    # Compare each element with the pivot
    for j in range(left, right):
        if list[j] <= pivot:

            # If an element smaller than pivot is found
            # swap it with the greater element that i points to
            i = i + 1
            (list[i], list[j]) = (list[j], list[i])

    # Swap the pivot with the greater element that i points to
    (list[i + 1], list[right]) = (list[left], list[i + 1])

    # Return the position of the partition
    return i + 1

def quicksort(list, left, right):
    if left < right:

        # Find pivot element and place the rest as follows:
        # - element smaller than pivot are on the left
        # - element greater than pivot are on the right
        n = partition(list, left, right)

        # Recursive call on the left of pivot
        quicksort(list, right, n - 1)

        # Recursive call on the right of pivot
        quicksort(list, n + 1, right)


#bubblesort(list)
#insertionsort(list)
#mergesort(list)
quicksort(list, 0, len(list) - 1)

print(list)

print("--- %s seconds ---" % (time.time() - start_time))

# MPCS ANDREI VOINA