# # # def linear_search(arr, target):
# # #     for i in range(len(arr)):
# # #         if arr[i] == target:
# # #             return i
# # #     return -1
# # #
# # # # Example Usage
# # # arr = [4, 2, 7, 1, 9, 5]
# # # target = 7
# # # result = linear_search(arr, target)
# # # print(f"Target {target} found at index {result}." if result != -1 else f"Target {target} not found.")
# # # # def binary_search(arr, target):
# # # #     low, high = 0, len(arr) - 1
# # # #     while low <= high:
# # # #         mid = (low + high) // 2
# # # #         if arr[mid] == target:
# # # #             return mid
# # # #         elif arr[mid] < target:
# # # #             low = mid + 1
# # # #         else:
# # # #             high = mid - 1
# # # #     return -1
# # # #
# # # # # Example Usage
# # # # arr = [1, 2, 4, 5, 7, 9]
# # # # target = 7
# # # # result = binary_search(arr, target)
# # # # print(f"Target {target} found at index {result}." if result != -1 else f"Target {target} not found.")
# # def bubble_sort(arr):
# #     n = len(arr)
# #     for i in range(n):
# #         swapped = False
# #         for j in range(0, n-i-1):
# #             if arr[j] > arr[j+1]:
# #                 arr[j], arr[j+1] = arr[j+1], arr[j]
# #                 swapped = True
# #         if not swapped:
# #             break
# #     return arr
# #
# # # Example Usage
# # arr = [4, 2, 7, 1, 9, 5]
# # sorted_arr = bubble_sort(arr)
# # print("Sorted Array:", sorted_arr)
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
#
# # Example Usage
# arr = [4, 8, 6, 1, 9, 5]
# sorted_arr = insertion_sort(arr)
# print("Sorted Array:", sorted_arr)
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
    merged_arr = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_arr.append(left[left_index])
            left_index += 1
        else:
            merged_arr.append(right[right_index])
            right_index += 1
    merged_arr.extend(left[left_index:])
    merged_arr.extend(right[right_index:])
    return merged_arr

# Example Usage
arr = [6, 15, 7, 18, 95, 5]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)

from basic import addition
addition.add2(9,10)

