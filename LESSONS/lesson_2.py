# def list_merg(list1, list2):
#     result_list = []
#     size1 = len(list1)
#     size2 = len(list2)
#     i = 0
#     j = 0
#
#     while i < size1 and j < size2:
#         if list1[i] <= list2[j]:
#             result_list.append(list1[i])
#             i +=1
#         else:
#             result_list.append(list2[j])
#             j += 1
#     # if size1 > size2:
#     #     while i < size1:
#     #         result_list.append(list1[i])
#     #         i += 1
#     # else:
#     #     while j < size2:
#     #         result_list.append(list2[j])
#     #         i += 1
#     result_list += list1[i:] + list2[j:]
#     return result_list
#
#
# def list_sort(list):
#     half = len(list) // 2 # деление на цело
#     result_list1 = list[:half]
#     result_list2 = list[half:]
#
#     if len(result_list1) > 1:
#         result_list1 = list_sort(result_list1)
#     if len(result_list2) > 1:
#         result_list2 = list_sort(result_list2)
#
#     return list_merg(result_list1, result_list2)
#
#
# my_list = [6, 3, 7, 1, 4, 2, 9, 8, 5]
# print(list_sort(my_list))



def a(z,b):
    sum =  z + b
    print(sum)
a(4, 5)


