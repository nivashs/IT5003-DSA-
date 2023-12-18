# # def find_next_greatest_element(arr, target):
# #     left, right = 0, len(arr) - 1
# #     next_greatest_index = None  # Initialize to None
# #
# #     while left <= right:
# #         mid = left + (right - left) // 2  # Calculate the middle index
# #         if arr[mid] > target:
# #             next_greatest_index = mid  # Update the index
# #             right = mid - 1  # Adjust the right bound to search to the left
# #         else:
# #             left = mid + 1  # Adjust the left bound to search to the right
# #
# #     if next_greatest_index is not None:
# #         return next_greatest_index
# #     else:
# #         return None  # If no greater element is found, return None
# #
# # # Example usage
# # # my_list = [3,4,5,6,7,8,10,10,10,10,10,10,10]
# # # target_element =2
# # my_list = [2,2,2,2,2,4,4,4,4,4]
# # target_element =3
# # next_greatest_index = find_next_greatest_element(my_list, target_element)
# #
# # if next_greatest_index is not None:
# #     next_greatest_element = next_greatest_index
# #     print(f"The next greatest element index is {next_greatest_element}")
# # else:
# #     print("The target element is not present, so there is no next greatest element.")
# def insert2s_twice(l):
#     count=0
#     for i in range(1,len(l)):
#         if count==2:
#             break
#         x=l[i]#number to be inserted
#         j=i-1
#         while(j>=0 and x==2):
#             l[j+1]=l[j]
#             j-=1
#             if j==-1:
#                 count+=1
#         l[j+1]=x
#     return l
# test=[3,3,3,3,2,2,2,2,2]
# print(insert2s_twice(test[2:]))
# print(test)

arr=[1,3,4]
lst=[99,99]
arr[1:]=lst
print(arr)