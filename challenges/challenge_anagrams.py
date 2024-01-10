def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    result = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def is_anagram(first_string, second_string):
    empty_string = ""

    if not first_string and not second_string:
        return (empty_string, empty_string, False)

    first = first_string.lower()
    second = second_string.lower()

    ordered_first_string = "".join(merge_sort(first))
    ordered_second_string = "".join(merge_sort(second))

    result = ordered_first_string == ordered_second_string

    return ordered_first_string, ordered_second_string, result
