# '''74 Triangle Patterns
# *
# * *
# * * *
# * * * *
# * * * * *'''
# for i in range(0,5):
#     print("* "* (i+1))

# '''
#     *
#    * *
#   * * *
#  * * * *
# * * * * *'''
# for i in range(1,6):
#     print(f"{"* "* i:^10}")

# '''
#         *
#       * *
#     * * *
#   * * * *
# * * * * * '''
# for i in range(1,6):
#     print(f"{"* "* i:>10}")

'''
* * * * * *
* * * * *
* * * *
* * *
* *
*'''
# for i in range(1,7)[::-1]:
#     print(f"{"* "* i}")

# * * * * * *
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *
# for i in range(1,7)[::-1]:
#     print(f"{"* "* i:^12}")

# Number Pattern in triangle (Left Justified)
# 1
# 12
# 123
# 1234
# 12345

# store = ""
# for i in range(1,6):
#     store += str(i)
#     print(store)

# Number Pattern in triangle (Centre)
#     1
#    1 2
#   1 2 3
#  1 2 3 4
# 1 2 3 4 5
#
# store = ""
# for i in range(1,6):
#     store += str(i) + " "
#     print(f"{store:^10}")

# Number Pattern in triangle (Right Justified)
#         1
#       1 2
#     1 2 3
#   1 2 3 4
# 1 2 3 4 5

# store = ""
# for i in range(1,6):
#     store += str(i) + " "
#     print(f"{store:>10}")

# 88 Write a program to get the below output
# *
# * *
# *
# * * *
# *
# * * * *
# *
# * * * * *

# for i in range(2,6):
#     print("* ")
#     print("* " * i )

# 143 write a program to get the below output using while loop
# 1
# 12
# 123
# 1234
# i = 1
# j = ""
# while i<5:
#     j += str(i)
#     print(j)
#     i += 1

# 148 write a program to print the below pattern
# 1 2 3 *
# 1 2 * 4
# 1 * 3 4
# * 2 3 4

# for i in range(1,5)[::-1]:
#     for j in range(1,5):
#         if(i == j):
#             print("*", end=" ")
#         else:
#             print(j, end= " ")
#     print()