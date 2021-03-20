my_list = ["January", "February", "March"]
print(type(my_list))
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
my_list.append("April")
print(my_list)
print(my_list[3])
# print(my_list[4]) # IndexError: list index out of range

# for is generally used with lists to iterate though the elements
for item in my_list:
    print(item)
