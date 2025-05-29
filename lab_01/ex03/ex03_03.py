def tao_tuple_tu_list(lst):
    return tuple(lst)
input_list = input("Nhập một danh sách số nguyên (cách nhau bởi dấu phẩy): ")
numbers = list(map(int, input_list.split(",")))
tuple_result = tao_tuple_tu_list(numbers)
print("Tuple được tạo từ danh sách là:", tuple_result)